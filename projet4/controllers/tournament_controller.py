import json
from models.tournament_model import Tournament
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController


class TournamentController:

    def __init__(self, view: TournamentView):
        self.view = view
        self.tournaments_file = "./data/tournaments.json"
        self.menu_choice_list = [{'value': 1, 'label': 'Start a tournament', 'callback': self.add_tournament},
                                 {'value': 2, 'label': 'Manage players', 'callback': self.manage_players},
                                 {'value': 3, 'label': 'Quit', 'callback': exit}]
        self.view.set_choice_list(self.menu_choice_list)
        self.current_tournament = None

    def manage_tournament(self):
        """
        Manages tournament operations based on user menu selection.
        This method displays a menu through the view, matches the user's choice with available options,
        and executes the corresponding callback function if one exists.
        Returns:
        Example:
            tournament_controller.manage_tournament()
        """

        choice = self.view.menu()
        menu_choice = next((item for item in self.menu_choice_list if item['value'] == choice), None)
        if menu_choice and 'callback' in menu_choice:
            menu_choice['callback']()
        else:
            None

    def manage_players(self):
        """
        Delegates player management operations to the PlayerController.
        This method acts as a bridge to the player management functionality,
        instantiating a PlayerController with its associated view and calling
        its manage_players method.
        Returns:
            None
        """

        PlayerController(PlayerView()).manage_players()

    def add_tournament(self):
        """
        Create and initialize a new tournament with players and rounds.
        This method performs the following steps:
        1. Loads existing players
        2. Updates the view with the player list
        3. Gets tournament details from user input
        4. Creates a new Tournament instance
        5. Initializes and starts tournament rounds
        6. Saves the tournament data
        Returns:
            None
        Side Effects:
            - Creates and saves a new Tournament instance
            - Updates self.current_tournament with the new tournament
        """

        players = PlayerController(PlayerView()).load_players()
        self.view.set_players_list(players)
        tournament_data = self.view.get_tournament_details()
        self.current_tournament = Tournament(**tournament_data)
        self.current_tournament.roundList = self.start_rounds()
        self.save_tournament(self.current_tournament)

    def start_rounds(self) -> list:
        """
        Start all rounds of a tournament.
        This method iterates through the number of rounds in the tournament and
        starts each round by calling the RoundController. It then stores the
        round data in a list.
        Returns:
            list: A list of dictionaries containing round details and match results
        Format example:
            [
                {
                    "name": "Round 1",
                    "startDate": "2021-01-01 10:00:00",
                    "endDate": "2021-01-01 10:30:00",
                    "matchList": [
                        {
                            "match": [
                                [{"chess_id": "AB12345", "score": 1.0}, ...],
                                [{"chess_id": "CD67890", "score": 0.0}, ...]
                            ]
                        },
                        ...
                    ]
                },
                ...
            ]
        Notes:
            - The round start and end dates are set automatically
            - Players are paired based on the Swiss tournament system
            - Match results are stored in the round object
        """

        rounds = []
        players = self.current_tournament.playerList
        for i in range(1, self.current_tournament.roundNumber + 1):
            round_controller = RoundController(self.current_tournament, i)
            round_data = round_controller.manage_round()
            rounds.append(round_data)
            self.current_tournament.playerList = players
        return rounds

    def save_tournament(self, tournament: Tournament):
        """
        Save a tournament to the database.
        This method loads the current list of tournaments from the database, adds the new tournament,
        and writes the updated list back to the database.
        Args:
            tournament (Tournament): The tournament instance to save
        Returns:
            None
        Side Effects:
            - Updates the tournaments database file
        """
        # Load existing tournaments
        tournaments = []
        try:
            with open(self.tournaments_file, 'r') as file:
                tournaments = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tournaments = []

        # Convert tournament to dict and handle Player objects
        tournament_dict = tournament.model_dump()

        # Convert Player objects in playerList to dicts
        tournament_dict['playerList'] = [
            player.model_dump() if hasattr(player, 'model_dump')
            else player
            for player in tournament_dict['playerList']
        ]

        # Convert Player objects in matchList
        for round_data in tournament_dict.get('roundList', []):
            for match in round_data.get('matchList', []):
                match_data = match.get('match', [])
                if match_data:
                    # Convert players in match data
                    player1 = match_data[0][0]
                    match_data[0][0] = player1.model_dump() if hasattr(player1, 'model_dump') else player1
                    # possible to reduce the datas stored in the match data by this following code
                    """
                    match_data[0][0] = {
                        'last_name': player1['last_name'],
                        'first_name': player1['first_name']
                    }
                    """
                    player2 = match_data[1][0]
                    match_data[1][0] = player2.model_dump() if hasattr(player2, 'model_dump') else player2

        # Add the tournament to the list
        tournaments.append(tournament_dict)

        # Save back to file
        with open(self.tournaments_file, 'w') as file:
            json.dump(tournaments, file, indent=4)

    def load_tournaments(self):
        """
        Load all tournaments from the database.
        This method reads the list of tournaments from the database file.
        Returns:
            list: A list of dictionaries containing tournament details
        """

        try:
            with open(self.tournaments_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
