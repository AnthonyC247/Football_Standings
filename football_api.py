import requests
import pandas as pd
from config import FOOTBALL_API_KEY
from database import store_dataframe_in_table
from display import display_leagues, display_standings, display_team_details

def fetch_data(url, params=None):
    '''
    Fetches data from the given API URL with optional parameters.

    Args:
    url (str): The API endpoint URL.
    params (dict, optional): Parameters to include in the request.

    Returns:
    dict: The JSON response from the API if successful, else None.
    '''
    headers = {'X-Auth-Token': FOOTBALL_API_KEY}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

def fetch_leagues():
    '''
    Fetches a list of available football leagues from API and stores them in the database.
    '''
    url = 'https://api.football-data.org/v4/matches/'
    data = fetch_data(url)
    if data and 'leagues' in data:
        leagues = data['leagues']
        df = pd.DataFrame(leagues)
        store_dataframe_in_table(df, 'leagues')
        display_leagues()  # Display leagues after storing them
    else:
        print('Failed to fetch leagues or no leagues data available.')

def fetch_standings(league_id):
    '''
    Fetches the standings for a specific league from API and stores them in the database.

    Args:
    league_id (int): The ID of the league.
    '''
    url = f'https://api.football-data.org/v2/competitions/{league_id}/matches'
    data = fetch_data(url)
    if data and 'matches' in data:
        standings = data['matches']
        df = pd.DataFrame(standings)
        store_dataframe_in_table(df, 'matches')
        display_standings()  # Display standings after storing them
    else:
        print('Failed to fetch standings or no standings data available.')

def fetch_team_details(team_id):
    '''
    Fetches details for a specific team from the API and stores them in the database.

    Args:
    team_id (int): The ID of the team.
    '''
    url = f"https://api.football-data.org/v2/teams/{team_id}"
    data = fetch_data(url)
    if data and 'team' in data:
        team = data['team']
        df = pd.DataFrame([team])
        store_dataframe_in_table(df, 'team')
        display_team_details()  # Display team details after storing them
    else:
        print('Failed to fetch team details or no team data available.')
