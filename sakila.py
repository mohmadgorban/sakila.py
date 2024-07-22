import pandas as pd 
import seaborn as sns 
import sqlalchemy as db
from sqlalchemy import create_engine

# 2. Connect to Sakila DB
engine = db.create_engine('postgresql+psycopg2://app_student:$vaoNXn3^Rmm@hu-dm.postgres.database.azure.com:5432/sakila')

# 3. import table 
with engine.connect() as connection:
    actor_df = pd.read_sql_table('actor', connection)
    film_df = pd.read_sql_table('film', connection)
    film_actor_df = pd.read_sql_table('film_actor', connection)
    category_df = pd.read_sql_table('category', connection)
    film_category_df = pd.read_sql('film_category',connection)
    payment_df = pd.read_sql_table('payment', connection)
    customer_df = pd.read_sql_table('customer', connection)
    store_df = pd.read_sql_table('store', connection)
    inventory_df = pd.read_sql_table('inventory', connection)
    rental_df = pd.read_sql_table('rental', connection)

print(rental_df.head(3))