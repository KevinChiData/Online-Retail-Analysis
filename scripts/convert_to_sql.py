import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/online_retail.csv')

engine = create_engine('sqlite:///data/online_retail_sql.db')
df.to_sql('online_retail_sql', con=engine, if_exists='replace', index=False)