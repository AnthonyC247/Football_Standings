from football import fetch_leagues, fetch_league_standings, fetch_team_standings, fetch_team_info, fetch_team_stats

def main():
    while True:
        print("\nWelcome to Football Data Fetcher! \nThe following data can be fetched:")
        print("1. Fetch Team Information")
        print("2. Fetch Leagues")
        print("3. Fetch Team Standings")
        print("4. Fetch Team Statistics")
        print("5. Fetch League Standings")
        print("6. Exit")
        choice = input("What would you like to fetch? Enter your choice (1-6): ")

        if choice == '1':
            team_name = input("Enter the name of the team or country: ")
            fetch_team_info(name=team_name)
        elif choice == '2':
            league_name = input("Enter the name or country of the league (leave blank to fetch all): ")
            fetch_leagues(name=league_name)
        elif choice == '3':
            team_name = input("Enter the name of the team: ")
            season = input("Enter the season year (e.g., 2021): ")
            fetch_team_standings(name=team_name, season=season)
        elif choice == '4':
            team_name = input("Enter the name of the team: ")
            league_name = input("Enter the name of the league: ")
            season = input("Enter the season year (e.g., 2021): ")
            fetch_team_stats(name=team_name, league=league_name, season=season)
        elif choice == '5':
            league_name = input("Enter the name of the league: ")
            season = input("Enter the season year (e.g., 2021): ")
            fetch_league_standings(league=league_name, season=season)
        elif choice == '6':
            print("Thank you for using Football Data Fetcher! Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        continue_choice = input("Do you want to keep fetching data? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using Football Data Fetcher!")
            break

if __name__ == "__main__":
    main()
