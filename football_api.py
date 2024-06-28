import pandas as pd
from utils import fetch_data, fetch_league_id, fetch_team_id
from database import store_dataframe_in_table


def fetch_team_info(name=None):
    '''
    Fetches details for teams based on name or country from the API.

    Args:
    name (str): The name of the team to search for.
    country (str): The country name of the team to search for.
    '''
    # API endpoint
    url = 'https://v3.football.api-sports.io/teams'

    # Ensure name is provided
    if not name:
        print('No team inputted')
        return False
    params = {'search': name}

    # Fetch data from API
    data = fetch_data(url, params)

    # Process API response
    if data and 'response' in data:
        teams_data = data['response']

        # Handle case where no teams are found
        if not teams_data:
            print(f'Team "{name}" not found.')
            return False

        # Extract relevant information from API response
        teams_info = []
        for team in teams_data:
            team_details = {
                'TeamName': team['team']['name'],
                'Country': team['team']['country'],
                'YearFounded': team['team']['founded'],
                'National': 'Yes' if team['team']['national'] else 'No'
            }
            teams_info.append(team_details)

        # Store data in DataFrame and database
        if teams_info:
            df = pd.DataFrame(teams_info)
            store_dataframe_in_table(df, 'teams')
            print('Team information stored successfully.')
            return True
        else:
            print('No valid team data found.')
            return False
    else:
        print('Failed to fetch team details or no team data available.')
        return False


def fetch_team_standings(name=None, season=None):
    '''
    Fetches the standings for a specific team and season from API.

    Args:
    team (str): The name of the team.
    season (int): The season year.
    '''
    # Check if season is not an integer and attempt to convert it
    if not isinstance(season, int):
        try:
            season = int(season)
        except ValueError:
            print('Invalid season format. Please enter a valid year.')
            return False

    # Fetch team ID based on provided team name
    team_id = fetch_team_id(name)

    # Return false if team ID is not found
    if not team_id:
        return False

    # API endpoint and parameters
    url = 'https://v3.football.api-sports.io/standings'
    params = {'team': team_id, 'season': season}

    # Fetch data from API
    data = fetch_data(url, params)

    # Process API response
    if data and 'response' in data:
        response = data['response']

        # Handle case where no standings are found for the team
        if not response:
            print(f'Team "{name}" not found.')
            return False

        # Extract standings information for each league the team is in
        standings_info = []
        for league_data in response:
            league = league_data['league']
            standings = league['standings'][0][0]
            league_standings = {
                'LeagueName': league['name'],
                'Country': league['country'],
                'Rank': standings['rank'],
                'Points': standings['points'],
                'GoalsDifference': standings['goalsDiff'],
                'Played': standings['all']['played'],
                'Wins': standings['all']['win'],
                'Draws': standings['all']['draw'],
                'Losses': standings['all']['lose'],
                'GoalsFor': standings['all']['goals']['for']
            }
            standings_info.append(league_standings)

        # Store data in DataFrame and database
        if standings_info:
            df = pd.DataFrame(standings_info)
            store_dataframe_in_table(df, 'team_standings')
            print(f"Team standings for '{name}' in season {season} \
                  stored successfully.")
            return True
        else:
            print('No valid team standings data found.')
            return False
    else:
        print('Failed to fetch standings or no standings data available.')
        return False


def fetch_team_stats(name=None, league=None, season=None):
    '''
    Fetches statistics for a team based on name or country from the API.

    Args:
    name (str): The name of the team to search for.
    league (str): The name of the league.
    season (int): The season year.
    '''
    # Check if all required parameters are provided
    if not (name and league and season):
        print("Please provide team name, league name, and season year.")
        return False

    # Check if season is not an integer and attempt to convert it
    if not isinstance(season, int):
        try:
            season = int(season)
        except ValueError:
            print('Invalid season format. Please enter a valid year.')
            return False

    # Fetch team ID based on provided team name
    team_id = fetch_team_id(name)
    if not team_id:
        return False

    # Fetch league ID based on provided league name
    league_id = fetch_league_id(league)
    if not league_id:
        return False

    # API endpoint and parameters
    url = 'https://v3.football.api-sports.io/teams/statistics'
    params = {'season': season, 'team': team_id, 'league': league_id}

    # Fetch data from API
    data = fetch_data(url, params)

    # Process API response
    if data and 'response' in data:
        if not data['response']:
            print(f"No statistics found for team '{name}' \
                  in league '{league}' for season '{season}'.")
            return False

        # Extract required statistics from API response
        response = data['response']
        league_name = response['league']['name']
        league_country = response['league']['country']
        team_name = response['team']['name']
        fixtures_played_total = response['fixtures']['played']['total']
        fixtures_wins_total = response['fixtures']['wins']['total']
        fixtures_draws_total = response['fixtures']['draws']['total']
        fixtures_losses_total = response['fixtures']['loses']['total']
        biggest_streak = response['biggest']['streak']
        penalty_score_total = response['penalty']['scored']['total']
        penalty_total = response['penalty']['total']

        # Construct DataFrame from extracted data
        data_dict = {
            'LeagueName': [league_name],
            'LeagueCountry': [league_country],
            'TeamName': [team_name],
            'PlayedGames': [fixtures_played_total],
            'WinsTotal': [fixtures_wins_total],
            'DrawsTotal': [fixtures_draws_total],
            'LossesTotal': [fixtures_losses_total],
            'BiggestWinStreak': [biggest_streak['wins']],
            'PenaltyTotal': [penalty_total],
            'PenaltyScored': [penalty_score_total]
        }

        df = pd.DataFrame(data_dict)
        df = df.transpose().reset_index()
        df.columns = ['Attribute', 'Value']

        # Store DataFrame in database table
        store_dataframe_in_table(df, 'team_stats')
        print(f"Team statistics for '{team_name}' stored successfully.")
        return True
    else:
        print('Failed to fetch team statistics or no data available.')
        return False


def fetch_leagues(name=None, season=None):
    '''
    Fetches football leagues based on name and season from API.

    Args:
    name (str): The name of the league to search for.
    season (int): The season year.
    '''
    # Check if season is not an integer and attempt to convert it
    if not isinstance(season, int):
        try:
            season = int(season)
        except ValueError:
            print('Please enter a valid year.')
            return False
    # Ensure name is provided
    if not name:
        print('Name not specified')
        return False

    # API endpoint and parameters
    url = 'https://v3.football.api-sports.io/leagues'
    params = {'name': name, 'season': season}

    # Fetch data from API
    data = fetch_data(url, params)

    # Process API response
    if data and 'response' in data:
        leagues_data = data['response']

        # Handle case where no leagues are found
        if not leagues_data:
            print(f'League "{name}" not found.')
            return False

        # Extract relevant information from API response
        leagues_info = []
        for league in leagues_data:
            league_details = {
                'Country': league['country']['name'],
                'SeasonStart': league['seasons'][0]['start'],
                'SeasonEnd': league['seasons'][0]['end'],
            }
            leagues_info.append(league_details)

        # Store data in DataFrame and database
        if leagues_info:
            df = pd.DataFrame(leagues_info)
            store_dataframe_in_table(df, 'leagues')
            print('Leagues information stored successfully.')
            return True
        else:
            print('No valid leagues data found.')
            return False
    else:
        print('Failed to fetch leagues or no leagues data available.')
        return False


def fetch_league_standings(league=None, season=None):
    '''
    Fetches the standings for a specific league and season from API.

    Args:
    league (str): The name of the league.
    season (int): The season year.
    '''
    # Check if season is not an integer and attempt to convert it
    if not isinstance(season, int):
        try:
            season = int(season)
        except ValueError:
            print('Invalid season format. Please enter a valid year.')
            return False

    # Fetch league ID based on provided league name
    league_id = fetch_league_id(league)

    # Return false if league ID is not found
    if not league_id:
        return False

    # API endpoint and parameters
    url = 'https://v3.football.api-sports.io/standings'
    params = {'league': league_id, 'season': season}

    # Fetch data from API
    data = fetch_data(url, params)

    # Process API response
    if data and 'response' in data:
        response = data['response'][0]['league']['standings'][0]
        if not response:
            print(f'No standings found for league {league}')
            return False

        # Normalize JSON data into DataFrame
        df = pd.json_normalize(response)
        df = df[['rank', 'team.name', 'points', 'goalsDiff', 'group',
                 'all.played', 'all.win', 'all.draw', 'all.lose']]
        df.columns = ['Rank', 'Team', 'Points', 'Goals Difference',
                      'Group', 'Played', 'Wins', 'Draws', 'Losses']

        # Store DataFrame in database table
        store_dataframe_in_table(df, 'league_standings')
        print('League standings stored successfully.')
        return True
    else:
        print('Failed to fetch standings or no standings data available.')
        return False
