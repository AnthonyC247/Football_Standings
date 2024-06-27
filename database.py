import sqlalchemy as db

def create_connection():
    '''
    Establishes a connection to the SQLite database using a context manager.

    Returns:
    sqlalchemy.engine.base.Connection: The database connection.
    '''
    engine = db.create_engine('sqlite:///football_fetcher.db')
    connection = engine.connect()
    return connection

def store_dataframe_in_table(df, table_name):
    '''
    Stores a DataFrame in the SQLite database table.

    Args:
    df (pd.DataFrame): The dataframe to store.
    table_name (str): The name of the table to store the DataFrame in.
    '''
    with create_connection() as connection:
        df.to_sql(table_name, con=connection, if_exists='replace', index=False)
