import json
from models.tournament_model import Tournament
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import PlayerController


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

    def select_players(self) -> list:
        players = PlayerController(PlayerView()).load_players()
        if not players:
            print("Aucun joueur enregistré.")
            return []

        print("\nListe des joueurs disponibles :")
        for player in players:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        selected_ids = input("\nEntrez les chess_id des joueurs (séparés par des virgules) : ").strip().split(',')

        player_list = []
        for chess_id in selected_ids:
            chess_id = chess_id.strip()
            player = next((p for p in players if p['chess_id'] == chess_id), None)
            if player:
                player_list.append(player)
            else:
                print(f"Joueur avec l'ID {chess_id} introuvable.")

        print("\nJoueurs sélectionnés :")
        for player in player_list:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        return player_list
