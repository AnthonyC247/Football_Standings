# display.py
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
    # Create a database connection
    with create_connection() as connection:
        # Construct SQL query to fetch data from table
        query = f"SELECT * FROM {table_name} LIMIT 10;"
        # Read data into a DataFrame using Pandas
        df = pd.read_sql(query, connection)
    return df


def display_dataframe(df, max_rows=10):
    '''
    Displays a DataFrame in the terminal with a specified
    maximum number of rows.

    Args:
    df (pd.DataFrame): The DataFrame to display.
    max_rows (int): The maximum number of rows to display.
    '''
    # Set Pandas options to display max_rows and all columns
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', None)  # Display all columns
    # Print the DataFrame
    print(df)


def display_team_info():
    '''
    Fetches and displays the team information from the database.
    '''
    # Fetch data for 'leagues' table
    df = fetch_data_from_table('teams')
    print("Team Details:")
    # Display the fetched DataFrame
    display_dataframe(df)


def display_team_standings():
    '''
    Fetches and displays the team statistics from database
    '''
    # Fetch data for 'leagues' table
    df = fetch_data_from_table('team_standings')
    print("Team Standings:")
    # Display the fetched DataFrame
    display_dataframe(df)


def display_team_stats():
    '''
    Fetches and displays the team statistics from database
    '''
    # Fetch data for 'leagues' table
    df = fetch_data_from_table('team_stats')
    print("Team Statistics:")
    # Display the fetched DataFrame
    display_dataframe(df)


def display_leagues():
    '''
    Fetches and displays the leagues from the database.
    '''
    # Fetch data for 'leagues' table
    df = fetch_data_from_table('leagues')
    print("Leagues:")
    # Display the fetched DataFrame
    display_dataframe(df)


def display_league_standings():
    '''
    Fetches and displays the standings from the database.
    '''
    # Fetch data for 'leagues' table
    df = fetch_data_from_table('league_standings')
    print("League Standings:")
    # Display the fetched DataFrame
    display_dataframe(df)
