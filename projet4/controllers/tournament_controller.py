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
        self.menu_choice_list = [{'value': 1, 'label': 'Démarrer un tournoi', 'callback': self.add_tournament},
                                 {'value': 2, 'label': 'Gestion des joueurs', 'callback': self.manage_players},
                                 {'value': 3, 'label': 'Quitter', 'callback': exit}]
        self.view.set_choice_list(self.menu_choice_list)
        self.current_tournament = None

    def manage_tournament(self):
        choice = self.view.menu()
        menu_choice = next((item for item in self.menu_choice_list if item['value'] == choice), None)
        if menu_choice and 'callback' in menu_choice:
            menu_choice['callback']()
        else:
            None

    def manage_players(self):
        PlayerController(PlayerView()).manage_players()

    def add_tournament(self):
        players = PlayerController(PlayerView()).load_players()
        self.view.set_players_list(players)
        tournament_data = self.view.get_tournament_details()
        self.current_tournament = Tournament(**tournament_data)
        self.current_tournament.roundList = self.start_rounds()
        self.save_tournament(self.current_tournament)

    def start_rounds(self) -> list:
        rounds = []
        players = self.current_tournament.playerList
        for i in range(1, self.current_tournament.roundNumber + 1):
            round_controller = RoundController(self.current_tournament, i)
            round_data = round_controller.manage_round()
            rounds.append(round_data)
            self.current_tournament.playerList = players
        return rounds

    def save_tournament(self, tournament: Tournament):
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
        try:
            with open(self.tournaments_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
