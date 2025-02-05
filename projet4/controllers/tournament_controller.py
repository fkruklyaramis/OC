import json
from models.tournament_model import Tournament
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import PlayerController
from datetime import datetime


class TournamentController:
    def __init__(self, view: TournamentView):
        self.view = view
        self.tournaments_file = "./data/tournaments.json"
        self.menu_choice_list = [{'value': 1, 'label': 'Démarrer un tournoi', 'callback': self.add_tournament},
                                 {'value': 2, 'label': 'Gestion des joueurs',
                                  'callback': self.manage_players},
                                 {'value': 3, 'label': 'Quitter', 'callback': exit}]

    def manage_tournament(self):
        choice = self.view.menu(self.menu_choice_list)
        menu_choice = next((item for item in self.menu_choice_list if item['value'] == choice), None)
        if menu_choice and 'callback' in menu_choice:
            menu_choice['callback']()
        else:
            None

    def manage_players(self):
        PlayerController(PlayerView()).manage_players()

    def add_tournament(self):
        data = self.view.get_tournament_details()
        tournament = Tournament(**data)
        self.save_tournament(tournament)
        print("Le tournoi est lancé !")

    def cancel_tournament(self):
        # check si un tournoi est en cours
        tournaments = self.load_tournaments()
        for tournament in tournaments:
            if tournament["end_date"] == "":
                self.update_tournament(self, "end_date", str(datetime.now().strftime("%Y-%m-%d")))
                print("Le tournoi est terminé !")
                break

    def save_tournament(self, tournament: Tournament):
        try:
            with open(self.tournaments_file, "r") as file:
                tournaments = json.load(file)
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
