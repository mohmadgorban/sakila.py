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

# films = film_df.merge(film_category_df, how='left', on='film_id')
# films = films.merge(category_df, how='left', on='category_id')

# films_group_by_category = films.groupby(['category_id','name']).agg(count_rows = ('film_id' , 'count')).reset_index()


# films_group_by_category.set_index('name', inplace=True)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='name', y='count_rows', data=films_group_by_category, palette='viridis')

# plt.xlabel('Category')
# plt.ylabel('Count')
# plt.title('Count of Rows by Category')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 3. Who are the top 5 actors with most movies?
# actor = film_df.merge(film_actor_df, how='left', on='film_id')
# actor = actor.merge(actor_df, how='left', on='actor_id')

# films_group_by_actor = actor.groupby('actor_id').agg(count_rows = ('film_id' , 'count')).reset_index()

# films_group_by_actor_5 =films_group_by_actor.sort_values(by='count_rows', ascending=False).head(5)
# print(films_group_by_actor_5)

# films_group_by_actor_5.set_index('actor_id', inplace=True)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='actor_id', y='count_rows', data=films_group_by_actor_5, palette='viridis')

# plt.xlabel('actor_id')
# plt.ylabel('Count')
# plt.title('Count of Rows by film for actor')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 4. Get a sorted list of movies based on number of actors.

# actor_in_film = actor.groupby('film_id').agg(count_rows = ('actor_id' , 'count')).reset_index()
# print(actor_in_film.head)

# 5. What is the monthly trend of total sales? (by payment date)

# payment_df['month'] = payment_df['payment_date'].dt.month_name()
# total_sales = payment_df.groupby('month').agg(count_rows = ('payment_id' , 'count')).reset_index()

# total_sales.set_index('month', inplace=True)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='month', y='count_rows', data=total_sales, palette='viridis')
# sns.lineplot(x='month', y='count_rows', data=total_sales, color='red', marker='o')

# plt.xlabel('month')
# plt.ylabel('Count')
# plt.title('month trend of total sales')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 6. Is store 1 doing better than store 2?

rental = rental_df.merge(inventory_df, how='left', on='inventory_id')

rental_store = rental.groupby('store_id').agg(count_rows = ('rental_id' , 'count')).reset_index()

rental_store.set_index('store_id', inplace=True)

plt.figure(figsize=(10, 6))
sns.barplot(x='store_id', y='count_rows', data=rental_store, palette='viridis')

plt.xlabel('store')
plt.ylabel('Count')
plt.title('Count of rental in store')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()