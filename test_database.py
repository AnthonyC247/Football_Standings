import sys
import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, \
                        Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql import text
from database import create_connection, store_dataframe_in_table


# Add the root directory of the project to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join
                (os.path.dirname(__file__), '..')))

# Create a test DataFrame
df = pd.DataFrame({
    'name': ['Premier League'],
    'country': ['England'],
    'season': [2024]
})

# Store the DataFrame in the 'leagues' table
store_dataframe_in_table(df, 'leagues')

# Fetch and print the data to verify
with create_connection() as connection:
    result = connection.execute(text("SELECT * FROM leagues")).fetchall()
    print(result)
