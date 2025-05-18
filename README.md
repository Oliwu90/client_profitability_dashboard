# Client Profitability Dashboard
A fully automated Power BI dashboard that tracks client profitability using MySQL, Python, and cloud integrations.

## 📌 Features
- 🐍 Python pipeline to pull, clean, and load work order data
- 🗃️ MySQL backend for centralized storage
- 📊 Power BI dashboard with dynamic metrics:
  - Revenue, Vendor Cost, Gross Margin
  - MoM % and YoY % change
  - Client and State filters
- ☁️ OneDrive-ready CSV export (gateway-free)

## 🔧 Tech Stack
- Python (pandas, SQLAlchemy, dotenv)
- MySQL (AWS RDS)
- Power BI (import mode)
- OneDrive (cloud-based refresh)

## 📂 Folder Structure
client_profitability_dashboard/
├── main.py # Data pipeline logic
├── sql/
│ └── client_profitability.sql
├── .env.dev # Local DB credentials
├── .gitignore
└── README.md

markdown
Copy
Edit

## 🚀 Usage
1. Run `main.py` to fetch and clean data
2. Exported data lands in MySQL or OneDrive (based on setup)
3. Power BI consumes the data and updates the dashboard

## 📈 Future Work
- Power Automate integration
- Enhanced tooltip narratives
- Drill-throughs and export options