from utils import fetch_data, fetch_league_id

def fetch_leagues(name=None):
    '''
    Fetches the football league based on the name from API.

    Args:
    name (str): The name of the league to search for.
    '''
    url = 'https://v3.football.api-sports.io/leagues'
    params = { 'search' : name}
    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response'][0]
        print(response)
    else:
        print('Failed to fetch league or no leagues data available.')

def fetch_standings(league=None, season=None):
    '''
    Fetches the standings for a specific league and season from API.

    Args:
    league (str): The name of the league.
    season (int): The season year.
    '''
    league_id = None
    if league:
        league_id = fetch_league_id(league)

    if not league_id:
        print('League ID not found.')
        return

    if not season:
        print('Season not specified.')
        return

    url = 'https://v3.football.api-sports.io/standings'
    params = {'league': league_id, 'season': season}
    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response'][0]['league']['standings']
        print(response)
    else:
        print('Failed to fetch standings or no standings data available.')


def fetch_team_info(name=None, country=None):
    '''
    Fetches details for teams based on name or country from the API.

    Args:
    name (str): The name of the team to search for.
    country (str): The country name of the team to search for.
    '''
    url = 'https://v3.football.api-sports.io/teams'
    params = {}
    if name:
        params['search'] = name
    if country:
        params['country'] = country

    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response'][0]
        print(response)
    else:
        print('Failed to fetch team details or no team data available.')