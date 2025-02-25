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
