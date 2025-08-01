import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/online_retail.csv')

df = df.dropna(subset=['InvoiceNo', 'CustomerID'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['Revenue'] = df['UnitPrice'] * df['Quantity']
df['CustomerID'] = df['CustomerID'].astype(str)

engine = create_engine('sqlite:///data/online_retail_sql.db')
df.to_sql('online_retail_sql', con=engine, if_exists='replace', index=False)