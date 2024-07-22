import pandas as pd 
import seaborn as sns 
import sqlalchemy as db
from sqlalchemy import create_engine

# 2. Connect to Sakila DB
engine = db.create_engine('postgresql+psycopg2://app_student:$vaoNXn3^Rmm@hu-dm.postgres.database.azure.com:5432/sakila')