from views.interface_view import InterfaceView
from jinja2 import Environment, FileSystemLoader
import os


class ReportView(InterfaceView):
    def __init__(self):
        super().__init__()
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.display_mode = self.choose_display_mode()

    def choose_display_mode(self) -> str:
        """Prompts user to select display format for reports.
        This method allows user to choose between HTML and console output format
        through command line interface.
        Returns:
            str: 'html' if user selects HTML format (1),
                'console' if user selects console format (2)
        """

        while True:
            print("\nChoose display mode:")
            print("1. HTML format")
            print("2. Console format")
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                return 'html' if choice == '1' else 'console'
            print("Invalid choice. Please enter 1 or 2.")

    def show_players_list(self, players: list):
        """
        Display a list of players either in HTML format or as plain text based on the display mode.

        Args:
            players (list): A list of dictionaries containing player information.
                           Each dictionary should have 'last_name' and 'first_name' keys.

        Notes:
            - If display_mode is 'html', renders the players_list.html template
            - If display_mode is not 'html', prints a plain text list of players sorted alphabetically
            - Players are displayed in "Last Name, First Name" format in plain text mode
        """

        if self.display_mode == 'html':
            template = self.env.get_template('players_list.html')
            print(template.render(players=players))
        else:
            print("\n=== Players List (Alphabetical) ===")
            for player in players:
                print(f"• {player['last_name']}, {player['first_name']}")

    def show_all_tournaments(self, tournaments: list):
        """Display a list of all tournaments.

        This method shows all tournaments either in HTML format using a template,
        or in console text format depending on the display_mode setting.

        Args:
            tournaments (list): A list of tournament dictionaries containing tournament details
                               like name, location, startDate and endDate.

        Returns:
            None

        Example:
            For console display mode, outputs:
            === Tournament List (ranked by startDate)===
            • Tournament1, Paris (2023-01-01, 2023-01-02)
            • Tournament2, London (2023-02-01, 2023-02-02)
        """

        if self.display_mode == 'html':
            template = self.env.get_template('tournaments_list.html')
            print(template.render(tournaments=tournaments))
        else:
            print("\n=== Tournament List (ranked by startDate)===")
            for tournament in tournaments:
                print(f"• {tournament['name']}, {tournament['location']} "
                      f"({tournament['startDate']}, {tournament['endDate']})")

    def show_tournament_details(self, tournament):
        """
        Display tournament details in either HTML or console format.

        Args:
            tournament (dict): A dictionary containing tournament information with the following keys:
                - name (str): Name of the tournament
                - location (str): Location where tournament is held
                - startDate (str): Start date of tournament
                - endDate (str): End date of tournament
                - description (str): Tournament description

        Returns:
            None: Prints tournament details to console or renders HTML template

        Notes:
            - If display_mode is 'html', renders tournament_details.html template
            - If display_mode is not 'html', prints formatted tournament details to console
            - If tournament is None, prints "No tournament found" message
        """

        if self.display_mode == 'html':
            template = self.env.get_template('tournament_details.html')
            print(template.render(tournament=tournament))
        else:
            if tournament:
                print(f"\n=== Tournament Details: {tournament['name']} ===")
                print(f"Location: {tournament['location']}")
                print(f"Start Date: {tournament['startDate']}")
                print(f"End Date: {tournament['endDate']}")
                print(f"Description: {tournament['description']}")
            else:
                print("\nNo tournament found with that name.")

    def show_tournament_players(self, players: list, tournament_name: str):
        """Display a list of players in a tournament.

        This method shows the list of players participating in a specific tournament.
        The display format depends on the display_mode setting (HTML or console).

        Args:
            players (list): List of dictionaries containing player information
                           with 'last_name' and 'first_name' keys
            tournament_name (str): Name of the tournament to display players for

        Returns:
            None
                Prints output either in HTML format using a template
                or as plain text to console
        """

        if self.display_mode == 'html':
            template = self.env.get_template('tournament_players.html')
            print(template.render(players=players, tournament_name=tournament_name))
        else:
            if tournament_name:
                print(f"\n=== Players in {tournament_name} ===")
                for player in players:
                    print(f"• {player['last_name']}, {player['first_name']}")
            else:
                print("\nNo tournament found with that name.")

    def show_tournament_rounds(self, rounds: list, tournament_name: str):
        """
        Display tournament rounds and matches information either in HTML or console format.

        Args:
            rounds (list): List of dictionaries containing round information including:
                - roundNumber: Round number
                - startDate: Round start date
                - endDate: Round end date
                - matchList: List of matches with player information and scores
            tournament_name (str): Name of the tournament to display

        Returns:
            None

        Notes:
            If display_mode is 'html', renders data using tournament_rounds.html template.
            Otherwise prints formatted text output to console showing:
            - Tournament name
            - For each round:
                - Round number
                - Start/end dates
                - List of matches with player names and scores
            Displays "No tournament found" message if tournament_name is empty.
        """

        if self.display_mode == 'html':
            template = self.env.get_template('tournament_rounds.html')
            print(template.render(rounds=rounds, tournament_name=tournament_name))
        else:
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

    def get_tournament_name(self) -> str:
        """
        Gets the tournament name from user input.

        Returns:
            str: The tournament name entered by the user, with leading and trailing whitespace removed.
        """

        return input("Enter tournament name: ").strip()
