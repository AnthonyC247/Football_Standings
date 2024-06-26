import requests
import pandas as pd
from config import FOOTBALL_API_KEY

def fetch_data(url, params=None):
    '''
    Fetches data from the given API URL with optional parameters.

    Args:
    url (str): The API endpoint URL.
    params (dict, optional): Parameters to include in the request.

    Returns:
    dict: The JSON response from the API if successful, else None.
    '''
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': FOOTBALL_API_KEY
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

def fetch_league_id(league_name):
    '''
    Fetches the league ID based on the league name.

    Args:
    league_name (str): The name of the league.

    Returns:
    int: The ID of the league if found, else None.
    '''
    url = 'https://v3.football.api-sports.io/leagues'
    params = {'search': league_name}
    data = fetch_data(url, params)
    if data and 'response' in data:
        leagues = data['response']
        if leagues:
            return leagues[0]['league']['id']
    print(f'League "{league_name}" not found.')
    return None

def fetch_team_id(team_name):
    '''
    Fetches the team ID based on the team name.

    Args:
    team_name (str): The name of the team.

    Returns:
    int: The ID of the team if found, else None.
    '''
    url = 'https://v3.football.api-sports.io/teams'
    params = {'search': team_name}
    data = fetch_data(url, params)
    if data and 'response' in data:
        teams = data['response']
        if teams:
            return teams[0]['team']['id']
    print(f'Team "{team_name}" not found.')
    return None