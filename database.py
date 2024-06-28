import sqlalchemy as db


def create_connection():
    '''
    Establishes a connection to the SQLite database using a context manager.

    Returns:
    sqlalchemy.engine.base.Connection: The database connection.
    '''
    try:
        # Create an SQLAlchemy engine for SQLite database
        engine = db.create_engine('sqlite:///football_fetcher.db')
        # Connect to the database
        connection = engine.connect()
        return connection
    except db.exc.SQLAlchemyError as e:
        print(f"Database connection failed: {e}")
        return None


def store_dataframe_in_table(df, table_name):
    '''
    Stores a DataFrame in the SQLite database table.

    Args:
    df (pd.DataFrame): The dataframe to store.
    table_name (str): The name of the table to store the DataFrame in.
    '''
    # Establish database connection
    connection = create_connection()

    # Check if connection is successful and DataFrame is not empty
    if connection and not df.empty:
        try:
            # Store DataFrame into the specified table in the database
            df.to_sql(table_name, con=connection,
                      if_exists='replace', index=False)
            print(f"Data stored successfully in table {table_name}.")
        except ValueError as e:
            print(f"Storing data in table {table_name} failed: {e}")
        finally:
            # Close the database connection
            connection.close()
    else:
        # If no data or connection failed, print message and close connection
        print(f"No data to store in {table_name} table.")
        connection.close()
        return
