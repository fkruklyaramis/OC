from views.interface_view import InterfaceView


class ReportView(InterfaceView):

    def show_players_list(self, players: list):
        """Display a list of players in alphabetical order.

        This function prints a formatted list of players, showing their last name,
        first name, and chess ID. The list is displayed with a header and each player
        entry is preceded by a bullet point.

            players (list): A list of dictionaries containing player information.
                           Each dictionary must have 'last_name', 'first_name',
                           and 'chess_id' keys.

        Example:
            >>> players = [
                {'last_name': 'Smith', 'first_name': 'John', 'chess_id': '12345'},
                {'last_name': 'Doe', 'first_name': 'Jane', 'chess_id': '67890'}
            ]
            >>> show_players_list(players)
            === Players List (Alphabetical) ===
            • Smith, John (ID: 12345)
            • Doe, Jane (ID: 67890)
        """
        print("\n=== Players List (Alphabetical) ===")
        for player in players:
            print(f"• {player['last_name']}, {player['first_name']} "
                  f"(ID: {player['chess_id']})")

    def show_all_tournaments(self, tournaments: list):
        """Display a list of all tournaments sorted by start date.
        Args:
            tournaments (list): List of tournament dictionaries containing tournament information
                               Each dictionary should have 'name', 'location', 'startDate', and 'endDate' keys
        Returns:
            None: Prints the tournament information to console
        Example output:
            === Tournament List (ranked by startDate)===
            • Tournament1, Paris (ID: 2023-01-01, 2023-01-02)
            • Tournament2, London (ID: 2023-02-01, 2023-02-02)
        """

        print("\n=== Tournament List (ranked by startDate)===")
        for tournament in tournaments:
            print(f"• {tournament['name']}, {tournament['location']} "
                  f"({tournament['startDate']}, {tournament['endDate']})")

    def show_tournament_details(self, tournament):
        """Display detailed information about a tournament.
        This method prints out all the essential details of a tournament including
        its name, location, start date, end date, and description.
        Args:
            tournament (dict): A dictionary containing tournament information with the following keys:
                - name (str): Name of the tournament
                - location (str): Location where tournament is held
                - startDate (str): Start date of the tournament
                - endDate (str): End date of the tournament
                - description (str): Description of the tournament
        Returns:
            None
        """

        if tournament:
            print(f"\n=== Tournament Details: {tournament['name']} ==="
                  f"\nLocation: {tournament['location']}"
                  f"\nStart Date: {tournament['startDate']}"
                  f"\nEnd Date: {tournament['endDate']}"
                  f"\nDescription: {tournament['description']}")
        else:
            print("\nNo tournament found with that name.")

    def show_tournament_players(self, players: list, tournament_name: str):
        """
        Display the list of players participating in a specific tournament.

        Args:
            players (list): List of dictionaries containing player information.
                           Each dictionary should have 'last_name' and 'first_name' keys.
            tournament_name (str): Name of the tournament.

        Returns:
            None

        Example:
            players = [
                {'last_name': 'Smith', 'first_name': 'John'},
                {'last_name': 'Doe', 'first_name': 'Jane'}
            ]
            show_tournament_players(players, "Chess Championship 2023")
        """
        if tournament_name:
            print(f"\n=== Players in {tournament_name} ===")
            for player in players:
                print(f"• {player['last_name']}, {player['first_name']}")
        else:
            print("\nNo tournament found with that name.")

    def show_tournament_rounds(self, rounds: list, tournament_name: str):
        """
        Display the rounds and matches information for a specific tournament.
        This method prints a formatted view of all rounds in a tournament, including:
        - Round number
        - Start and end dates for each round
        - Match results with player names and scores
        Args:
            rounds (list): List of dictionaries containing round information including:
                - roundNumber: Number identifying the round
                - startDate: Start date of the round
                - endDate: End date of the round
                - matchList: List of matches with player information and scores
            tournament_name (str): Name of the tournament being displayed
        Returns:
            None: This method only prints to console
        """
        if tournament_name:
            print(f"\n=== Rounds and Matches in {tournament_name} ===")
            for round_data in rounds:
                print(f"\nRound: {round_data['roundNumber']}")
                print(f"Started: {round_data['startDate']}")
                print(f"Ended: {round_data['endDate']}")
                print("Matches:")
                for match in round_data['matchList']:
                    player1 = match['match'][0][0]
                    score1 = match['match'][0][1]
                    player2 = match['match'][1][0]
                    score2 = match['match'][1][1]
                    print(f"  • {player1['first_name']} {player1['last_name']} ({score1}) vs "
                          f"{player2['first_name']} {player2['last_name']} ({score2})")
        else:
            print("\nNo tournament found with that name.")

    def get_tournament_name(self):
        """
        Gets the tournament name from user input.
        Returns:
            str: The name of the tournament entered by the user, with leading and trailing whitespace removed.
        """

        return input("\nEnter tournament name: ").strip()
