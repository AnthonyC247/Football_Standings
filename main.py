from football_api import fetch_leagues, fetch_league_standings, fetch_team_standings, fetch_team_info, fetch_team_stats
from display import display_league_standings, display_team_info, display_team_stats, display_team_standings, display_leagues


def main():
    while True:
        print("\nWelcome to Football Data Fetcher! \nThe following data can be fetched:")
        print("1. Fetch Team Information")
        print("2. Fetch Team Standings")
        print("3. Fetch Team Statistics")
        print("4. Fetch League")
        print("5. Fetch League Standings")
        print("6. Exit")
        choice = input("What would you like to fetch? Enter your choice (1-6): ")

        if choice == '1':
            # Fetch and display team information
            team_name = input("Enter the name of the team or country: ")
            success = fetch_team_info(name=team_name)
            if not success:
                continue
            display_team_info()  # Display team information after fetching

        elif choice == '2':
            # Fetch and display team standings
            team_name = input("Enter the name of the team: ")
            season = input("Enter the season year (e.g., 2021): ")
            success = fetch_team_standings(name=team_name, season=season)
            if not success:
                continue
            display_team_standings()  # Display team standings after fetching

        elif choice == '3':
            # Fetch and display team statistics
            team_name = input("Enter the name of the team: ")
            league_name = input("Enter the name of the league: ")
            season = input("Enter the season year (e.g., 2021): ")
            success = fetch_team_stats(name=team_name, league=league_name, season=season)
            if not success:
                continue
            display_team_stats()  # Display team statistics after fetching

        elif choice == '4':
            # Fetch and display league information
            league_name = input("Enter the name of the league (leave blank to fetch all): ")
            season = input("Enter the season year (e.g., 2021): ")
            success = fetch_leagues(name=league_name, season=season)
            if not success:
                continue
            display_leagues()  # Display leagues information after fetching

        elif choice == '5':
            # Fetch and display league standings
            league_name = input("Enter the name of the league: ")
            season = input("Enter the season year (e.g., 2021): ")
            success = fetch_league_standings(league=league_name, season=season)
            if not success:
                continue
            display_league_standings()  # Display league standings after fetching

        elif choice == '6':
            # Exit the program
            print("Thank you for using Football Data Fetcher! Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

        # Prompt user if they want to continue fetching data
        continue_choice = input("Do you want to keep fetching data? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using Football Data Fetcher!")
            break


if __name__ == "__main__":
    main()
