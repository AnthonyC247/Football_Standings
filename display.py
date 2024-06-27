import pandas as pd
from database import create_connection

def fetch_data_from_table(table_name):
    '''
    Fetches data from the specified table in the database.

    Args:
    table_name (str): The name of the table to fetch data from.

    Returns:
    pd.DataFrame: The data from the table.
    '''
    with create_connection() as connection:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, connection)
    return df

def display_dataframe(df, max_rows=10):
    '''
    Displays a DataFrame in the terminal with a specified maximum number of rows.

    Args:
    df (pd.DataFrame): The DataFrame to display.
    max_rows (int): The maximum number of rows to display.
    '''
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', None)  # Display all columns
    print(df)

def display_leagues():
    '''
    Fetches and displays the leagues from the database.
    '''
    df = fetch_data_from_table('leagues')
    print("Leagues:")
    display_dataframe(df)

def display_league_standings():
    '''
    Fetches and displays the standings from the database.
    '''
    df = fetch_data_from_table('league_standings')
    print("League Standings:")
    display_dataframe(df)

def display_team_details():
    '''
    Fetches and displays the team details from the database.
    '''
    df = fetch_data_from_table('teams')
    print("Team Details:")
    display_dataframe(df)
