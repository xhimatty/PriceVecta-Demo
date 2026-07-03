from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class PriceMonitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    product = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    new_price = db.Column(db.Float)
    status = db.Column(db.String(50))
    url = db.Column(db.String(2000), nullable=False)
    scraped_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))