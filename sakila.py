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

# rental = rental_df.merge(inventory_df, how='left', on='inventory_id')

# rental_store = rental.groupby('store_id').agg(count_rows = ('rental_id' , 'count')).reset_index()

# rental_store.set_index('store_id', inplace=True)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='store_id', y='count_rows', data=rental_store, palette='viridis')

# plt.xlabel('store')
# plt.ylabel('Count')
# plt.title('Count of rental in store')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 7. Are there any movies that are not in the inventory? If so, how many?

# inventory_film = film_df.merge(inventory_df, how='left', on='film_id')
# is_null_a =inventory_film['inventory_id'].isna()
# count_is_null_a = (is_null_a == True).sum()
# print(count_is_null_a)

# 8. How many customers have not returned more than 1 DVD?

# rental_df['new_column'] = rental_df['return_date'].apply(lambda x: 0 if pd.notna(x) else 1)
# rental_not_return = rental_df.groupby('customer_id').agg(count_rows = ('new_column' , 'sum')).reset_index()
# count_greater_than_one = (rental_not_return['count_rows'] > 1).sum()
# print(count_greater_than_one)

# 9. Get the number of times each movie which is available for rent (i.e., can be found in the inventory) has been rented and get its total revenue.

# film_df = film_df.merge(inventory_df, how='left', on='film_id')
# film_df = film_df.merge(rental_df, how='left', on='inventory_id')
# film_df = film_df.merge(payment_df, how='left', on='rental_id')

# summary = film_df.groupby(['title','rental_rate']).agg({'rental_id': 'count', 'amount': 'sum'})
# summary = summary.reset_index()
# summary.rename(columns={'rental_id': 'total_rentals', 'amount': 'total_amount'}, inplace=True)
# print(summary.head())

# 10. Get rental count and total revenue of movies by genre and rental month.

# category_df = category_df.merge(film_category_df, how='inner', on='category_id')
# category_df = category_df.merge(inventory_df, how='inner',on='film_id')
# category_df = category_df.merge(rental_df, how='inner',on='inventory_id', suffixes=('_category', '_rental'))
# category_df = category_df.merge(payment_df, on='rental_id')
# category_df['rental_month'] = category_df['rental_date'].dt.to_period('M')
# rental_count_total_revenue = category_df.groupby(['name','rental_month']).agg(rental_count = ('rental_id' , 'count'),total_revenue = ('amount' , 'sum')).reset_index()
# print(rental_count_total_revenue.head())

# 11. For how long each movie have waited in the shelf? (total and average number of days between rentals)

# rental_df = rental_df.merge(inventory_df, on='inventory_id')
# rental_df = rental_df.merge(film_df, on='film_id')
# sub_data = rental_df[['title','inventory_id', 'rental_date', 'return_date','rental_id']].sort_values(by='rental_date')
# sub_data['previous_rental'] = sub_data.groupby(['title','inventory_id'])['return_date'].shift(1)
# sub_data['shelf_days'] = (sub_data['rental_date'] - sub_data['previous_rental']).dt.days
# total_data = sub_data.groupby(['title'])['shelf_days'].sum()
# print(total_data.head())


# 12. Are movies usually returned late, early, or on time?

# film_df = film_df.merge(inventory_df, on= 'film_id')
# film_df = film_df.merge(rental_df, on='inventory_id')
# film_df['rented_days'] = (film_df['return_date'] - film_df['rental_date']).dt.days
# film_df['status'] = 'Not Returned'
# film_df.loc[(film_df['rented_days'] == film_df['rental_duration']),'status'] = 'On Time'
# film_df.loc[(film_df['rented_days'] < film_df['rental_duration']),'status'] = 'Early'
# film_df.loc[(film_df['rented_days'] > film_df['rental_duration']),'status'] = 'Late'
# print(film_df['status'].head())
# summary = film_df.groupby('status')['title'].count().reset_index()
# summary.set_index('status', inplace=True)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='status', y='title', data=summary, palette='viridis')

# plt.xlabel('status')
# plt.ylabel('title')
# plt.title('status movies usually returned')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 13. In each category, which actor is the most popular among customers?

# actor_df = actor_df.merge(film_actor_df,on='actor_id')
# actor_df = actor_df.merge(film_category_df,on = 'film_id')
# actor_df = actor_df.merge(category_df,on='category_id' ,suffixes=('_actor', '_category'))
# actor_df = actor_df.merge(inventory_df, on='film_id')
# actor_df = actor_df.merge(rental_df, on='inventory_id',suffixes=('_inventory', '_rental'))
# actor_df = actor_df.merge(payment_df, on='rental_id')

# most_popular = actor_df.groupby(['name' ,'first_name' ,'last_name']).agg(count_rows = ('actor_id' , 'count')).reset_index()
# print(most_popular.iloc[most_popular.groupby(['name'])['count_rows'].idxmax()])
