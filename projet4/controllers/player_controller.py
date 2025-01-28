import json
from models.player_model import Player


class PlayerController():
    def __init__(self, view):
        self.view = view
        self.players_file = "./data/players.json"

    def manage_players(self):
        while True:
            print("\nGestion des joueurs :")
            print("1. Ajouter un joueur")
            print("2. Lister tous les joueurs")
            print("3. Quitter")

            choice = input("Choisissez une option : ")
            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    def add_player(self):
        data = self.view.get_player_details()
        player = Player(**data)
        self.save_player(player)
        print("Joueur ajouté avec succès !")

    def list_players(self):
        players = self.load_players()
        self.view.display_players(players)

    def save_player(self, player):
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
