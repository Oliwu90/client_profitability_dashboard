import os
from dotenv import load_dotenv
import sqlalchemy
import pandas as pd
from urllib.parse import quote_plus
import numpy as np

# Load environment variables from .env file
load_dotenv()  # Load .env file
# load_dotenv(dotenv_path=".env.dev")  # Load .env.dev file
print("Loaded user:", os.getenv('DB_USER'))

user = os.getenv('DB_USER')
password = quote_plus(os.getenv('DB_PASS')) # Use quote_plus to handle special characters
host = os.getenv('DB_HOST')
db = os.getenv('DB_NAME')

engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:3306/{db}')

# Read SQL from external file
with open("sql/client_profitability.sql", "r") as file:
    query = file.read() # Execute the SQL query and load the result into a DataFrame

# Load to pandas
df = pd.read_sql(query, engine)

print(df.head())
# Clean up raw work orders
df['approveddate'] = pd.to_datetime(df['approveddate'], errors='coerce')
df['ordereddate'] = pd.to_datetime(df['ordereddate'], errors='coerce')
df['revenue'] = df['clientprice'] - df['vendorprice']

# Clean
df = df.replace([np.inf, -np.inf], np.nan)
df = df.where(pd.notnull(df), None)

# Export raw data to MySQL
df.to_sql("client_profitability_raw", engine, if_exists="replace", index=False)

print("Raw data exported.")