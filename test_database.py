from database import create_connection, store_dataframe_in_table
import pandas as pd
from sqlalchemy import text

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
    query = text("SELECT * FROM leagues")
    result = connection.execute(query).fetchall()
    print(result)

