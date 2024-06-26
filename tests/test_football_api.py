from football_api import fetch_leagues, fetch_league_standings, fetch_team_standings, fetch_team_info, fetch_team_stats

#test to fetch the league 
fetch_leagues('Premier League')

#test to fetch the league standings
fetch_league_standings('Premier League', 2024)

#test to fetch team standings 
fetch_team_standings('Chelsea FC', 2024)

#tes to fetch team info
fetch_team_info(name='Chelsea FC')

#test to fetch team stats
fetch_team_stats('Chelsea FC', 'Premier League', 2024)
