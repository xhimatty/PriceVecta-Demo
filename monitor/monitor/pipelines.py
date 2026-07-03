# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from pathlib import Path
import sys

root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path))

from itemadapter import ItemAdapter
from models import db, PriceMonitor
from app import app


class MonitorPipeline:
    def process_item(self, item, spider):
        with app.app_context():
            previous_record = PriceMonitor.query.filter_by(
                store=item["store"], product=item["product"]
            ).order_by(PriceMonitor.scraped_at.desc()).first()

            incoming_price = float(item['price'])
            if previous_record:
                previous_price = previous_record.new_price
                if incoming_price < previous_price:
                    status = 'Price Drop'
                elif incoming_price > previous_price:
                    status = 'Price Increase'
                else:
                    status = 'No Change'

            else:
                previous_price = incoming_price
                status = 'New'

            new_record = PriceMonitor(
                store=item['store'],
                brand=item['brand'],
                product=item['product'],
                price=previous_price,
                new_price=incoming_price,
                status=status,
                url=item['url'],
                scraped_at=item['scraped_at']
            )
            
            try:
                db.session.add(new_record)
                db.session.commit()
                spider.logger.info(f"Successfully logged {item['product']} ({status})")
            except Exception as e:
                db.session.rollback()
                spider.logger.error(f"Database save failed: {e}")
            finally:
                db.session.remove() 
                
        return item
