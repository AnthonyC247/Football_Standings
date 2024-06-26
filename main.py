from football import fetch_leagues, fetch_standings, fetch_team_details

def main():
    while True:
        print("\nFootball Data Fetcher")
        print("1. Fetch Leagues")
        print("2. Fetch Standings")
        print("3. Fetch Team Details")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            fetch_leagues()
        elif choice == '2':
            league_id = input("Enter League ID: ")
            fetch_standings(league_id)
        elif choice == '3':
            team_id = input("Enter Team ID: ")
            fetch_team_details(team_id)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
