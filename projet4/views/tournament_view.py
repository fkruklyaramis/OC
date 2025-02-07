from views.view import View


class TournamentView(View):

    def __init__(self):
        super().__init__()
        self.players = []

    def set_players_list(self, players):
        self.players = players

    def get_tournament_details(self):
        print("Création du tournois :")
        tournament_name = input("Nom: ")
        tournament_location = input("Lieu : ")
        startDate = input("Date de début(YYYY-MM-DD) : ")
        endDate = input("Date de fin(YYYY-MM-DD) : ")
        playerList = self.select_players()
        description = input("Description : ")
        # créer l'objet ici et le retourner
        return {"name": tournament_name, "location": tournament_location,
                "startDate": startDate, "endDate": endDate, "playerList": playerList, "description": description}

    def select_players(self) -> list:
        if not self.players:
            print("Aucun joueur enregistré.")
            return []

        print("\nListe des joueurs disponibles :")
        for player in self.players:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        selected_ids = input("\nEntrez les chess_id des joueurs (séparés par des virgules) : ").strip().split(',')

        player_list = []
        for chess_id in selected_ids:
            chess_id = chess_id.strip()
            player = next((p for p in self.players if p['chess_id'] == chess_id), None)
            if player:
                player_list.append(player)
            else:
                print(f"Joueur avec l'ID {chess_id} introuvable.")

        print("\nJoueurs sélectionnés :")
        for player in player_list:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        return player_list
