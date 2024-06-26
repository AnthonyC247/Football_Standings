from football import fetch_leagues, fetch_standings, fetch_team_info

def main():
    while True:
        print("\nFootball Data Fetcher")
        print("1. Fetch Leagues")
        print("2. Fetch Standings")
        print("3. Fetch Team Information")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            league_name = input("Enter the name or country of the league (leave blank to fetch all): ")
            fetch_leagues(name=league_name)
        elif choice == '2':
            league_name = input("Enter the name of the league: ")
            season = input("Enter the season year (e.g., 2021): ")
            fetch_standings(league=league_name, season=season)
        elif choice == '3':
            team_name = input("Enter the name of the team: ")
            fetch_team_info(name=team_name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
