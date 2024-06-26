from utils import fetch_data, fetch_league_id, fetch_team_id

def fetch_leagues(name=None):
    '''
    Fetches the football league based on the name from API.

    Args:
    name (str): The name of the league to search for.
    '''
    url = 'https://v3.football.api-sports.io/leagues'
    params = {'search': name}
    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response'][0]
        print(response)
    else:
        print('Failed to fetch league or no leagues data available.')

def fetch_league_standings(league=None, season=None):
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
        print('Season not specified correctly or out of bounds.')
        return

    url = 'https://v3.football.api-sports.io/standings'
    params = {'league': league_id, 'season': season}
    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response'][0]['league']['standings']
        print(response)
    else:
        print('Failed to fetch standings or no standings data available.')


def fetch_team_standings(name=None, season=None):
    '''
    Fetches the standings for a specific team and season from API.

    Args:
    team (str): The name of the team.
    season (int): The season year.
    '''
    team_id = None
    if name:
        team_id = fetch_team_id(name)

    if not team_id:
        print('Team ID not found.')
        return

    if not season:
        print('Season not specified correctly or out of bounds.')
        return
    url = 'https://v3.football.api-sports.io/standings'
    params = {'team': team_id, 'season': season}
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

def fetch_team_stats(name=None, league=None, season=None):
    '''
    Fetches statistics for a team based on name or country from the API.

    Args:
    name (str): The name of the team to search for.
    league (str): The name of the league.
    season (int): The season year.
    '''
    if not (name and league and season):
        print("Please provide team name, league name, and season year.")
        return

    team_id = fetch_team_id(name)
    league_id = fetch_league_id(league)
    if not team_id:
        print(f"Team '{name}' not found.")
        return
    if not league_id:
        print(f"League '{league}' not found.")
        return

    url = 'https://v3.football.api-sports.io/teams/statistics'
    params = {'season': season, 'team': team_id, 'league': league_id}
    data = fetch_data(url, params)
    if data and 'response' in data:
        response = data['response']
        print(f"Statistics for {name} in season {season}:")
        print(response)  # Modify to display specific statistics as needed
    else:
        print('Failed to fetch team statistics or no data available.')
