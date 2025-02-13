import json
from models.tournament_model import Tournament
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from views.round_view import RoundView


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
        data = self.view.get_tournament_details()
        self.current_tournament = Tournament(**data)
        self.current_tournament.roundList = self.start_rounds()
        self.save_tournament(self.current_tournament)

    def start_rounds(self) -> list:
        return RoundController(RoundView(), self.current_tournament).manage_rounds()

    def save_tournament(self, tournament):
        try:
            with open(self.tournaments_file, "r") as file:
                try:
                    tournaments = json.load(file)
                except json.JSONDecodeError:
                    tournaments = []
        except FileNotFoundError:
            tournaments = []

        tournaments.append(tournament.to_dict())

        with open(self.tournaments_file, "w") as file:
            json.dump(tournaments, file, indent=4)

    def load_tournaments(self):
        try:
            with open(self.tournaments_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
