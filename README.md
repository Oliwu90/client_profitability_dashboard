# Client Profitability Dashboard
This project analyzes monthly gross margins by client and regions using a Power BI dashboard powered by MySQL and Python.

## 🔧 Components
- **Python**: ETL script (`main.py`) reads and cleans raw data, then pushes to MySQL.
- **MySQL**: Stores the cleaned table `client_profitability_raw`.
- **Power BI**: Consumes MySQL data to visualize margin trends and YoY changes.

## 📁 Structure
- `main.py`: Loads environment variables and exports raw data to MySQL.
- `sql/client_profitability.sql`: Base query to extract work order data.
- `pbix/`: (Optional) Power BI dashboard files.
- `.env.dev`: Example of required DB environment variables.

## ⚙️ Usage
1. Fill in `.env.dev` with your MySQL credentials:
DB_USER=username
DB_PASS=password
DB_HOST=host_url
DB_NAME=readonlydata

2. Run the pipeline:
python main.py

## 📊 Key Metrics
Gross Margin %

MoM and YoY Margin Changes

Work Orders by Client and State