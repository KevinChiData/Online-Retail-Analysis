import pandas as pd
from sqlalchemy import create_engine

# Read and save csv to df
df = pd.read_csv('data/online_retail.csv')

# Clean data by removing null values
df = df.dropna(subset=['InvoiceNo', 'CustomerID'])

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Remove negative quantity and price values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Create Revenue column
df['Revenue'] = df['UnitPrice'] * df['Quantity']

# Convert CustomerID to string
df['CustomerID'] = df['CustomerID'].astype(str)

# Create database to create SQL queries
engine = create_engine('sqlite:///data/online_retail_sql.db')
df.to_sql('online_retail_sql', con=engine, if_exists='replace', index=False)