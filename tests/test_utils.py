from utils import fetch_league_id , fetch_team_id

#testing thr fetch league ID
league_id = fetch_league_id('Premier League')
print(f'Premier League ID: {league_id}')

#testing the fetch team id 
team_id = fetch_team_id('Chelsea FC')
print (f'Chelsea FC team ID: {team_id}')

