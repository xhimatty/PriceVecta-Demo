# PriceVecta

### You give us the targets. We deliver the data.

## Description
PriceVecta is a custom price monitoring platform that automates price collection from client-specified e-commerce, retail, and distributor websites. It continuously tracks product prices, stores historical records, and notifies users whenever pricing changes occur.

<img width="2736" height="1562" alt="Screenshot 2026-06-28 015828" src="https://github.com/user-attachments/assets/70f1bcba-9a9c-4de8-b91d-85e1bf403088" />

PriceVecta eliminates manual data collection by combining automated web scraping with an intuitive dashboard, historical analytics, CSV exports, and real-time alerts to provide businesses with actionable market insights, real-time competitive advantages, and data-driven pricing decisions.

## Key Features
- **Custom Automated Extraction:** Continuous price and stock monitoring across client-specified e-commerce, retail, and distributor websites.
- **Visual Intelligence Dashboard:** A clean, responsive interface viewing tracked products, current prices, and key monitoring metrics. 
- **Historical Data Analytics:** Data persistence layer that logs pricing history over time, enabling long-term trend analysis.
- **Data Export:** Built-in capability to export historical pricing records to CSV for external reporting and business intelligence.
- **Instant Alerting Engine:** Real-time Telegram and Email notifications immediately price changes are detected, including the previous price, current price, and product link.
- **Scalable Data Pipeline:** Built with Scrapy, Flask, SQLAlchemy, and Docker to support reliable, automated monitoring workflows.
- **Cloud-Based Scheduling:** Automated scraping jobs deployed on Google Cloud Compute Engine using Linux cron jobs.

## Full Production Capabilities
*The complete enterprise architecture of PriceVecta supports extended features not active in this standalone demo*

### Target Audience
**PriceVecta is engineered to power data-driven decisions for:**
- E-Commerce Businesses & Retailers: Dynamically optimize repricing strategies.
- Procurement Teams & Distributors: Monitor vendor compliance and identify cost-saving opportunities.
- Market Researchers & Competitive Intelligence Teams: Track long-term market trends and competitor behaviors.

## System Architecture & Tech Stack
PriceVecta is split into four core layers: Extraction, Storage, dashboard, and Infrastructure.

====== put image architecture here =======


============================================

## Dashboard
The dashboard provides a centralized view of monitored products, including:

* Total products tracked
* Highest recorded price
* Lowest recorded price
* Last update timestamp

Each product links directly to its historical pricing page, where users can review previous prices and export the data as a CSV file.

## Price Change Detection
Whenever a scraper runs, newly collected prices are compared against the latest stored values.

If a change is detected, PriceVecta automatically:
* Records the new price
* Stores the previous price history
* Updates the dashboard
* Sends Telegram notifications
* Sends email alerts

## Technology Stack
| Category | Technologies |
| :--- | :--- |
| **Backend** | Python, Flask, Scrapy, SQLAlchemy |
| **Database** | SQLite |
| **Integrations** | Telegram API, SMTP (Email Notifications) |
| **Infrastructure & Deployment** | Docker, Google Cloud Compute Engine, Linux Cron Jobs |

