import json
from models.player_model import Player
from views.player_view import PlayerView


class PlayerController():

    def __init__(self, view: PlayerView):
        self.view = view
        self.players_file = "./data/players.json"
        self.menu_choice_list = [{'value': 1, 'label': 'Ajouter un joueur', 'callback': self.add_player},
                                 {'value': 2, 'label': 'Lister tous les joueur', 'callback': self.list_players},
                                 {'value': 3, 'label': 'Retour au menu principal'}]
        self.view.set_choice_list(self.menu_choice_list)

    def manage_players(self):
        choice = self.view.menu()
        menu_choice = next((item for item in self.menu_choice_list if item['value'] == choice), None)
        if menu_choice and 'callback' in menu_choice:
            menu_choice['callback']()
        else:
            None

    def add_player(self):
        data = self.view.get_player_details()
        player = Player(**data)
        self.save_player(player)
        print("Joueur ajouté avec succès !")

    def list_players(self):
        players = self.load_players()
        self.view.display_players(players)

    def save_player(self, player: Player):
        try:
            with open(self.players_file, "r") as file:
                players = json.load(file)
        except FileNotFoundError:
            players = []

        players.append(player.to_dict())

        with open(self.players_file, "w") as file:
            json.dump(players, file, indent=4)

    def load_players(self):
        try:
            with open(self.players_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
