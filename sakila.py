import pandas as pd 
import seaborn as sns 
import sqlalchemy as db
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


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

#analysa
#  1. Are there any duplicates in actor data? If so, drop them from the data.

actor_df = actor_df.drop_duplicates()

# 2. Which categories have most films?

films = film_df.merge(film_category_df, how='left', on='film_id')
films = films.merge(category_df, how='left', on='category_id')

films_group_by_category = films.groupby(['category_id','name']).agg(count_rows = ('film_id' , 'count')).reset_index()


films_group_by_category.set_index('name', inplace=True)

plt.figure(figsize=(10, 6))
sns.barplot(x='name', y='count_rows', data=films_group_by_category, palette='viridis')

plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Count of Rows by Category')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()