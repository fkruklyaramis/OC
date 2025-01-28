class PlayerView:
    def get_player_details(self):
        print("Ajout d'un joueur :")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (YYYY-MM-DD) : ")
        chess_id = input("Identifiant d'échecs : ")
        return {"last_name": last_name, "first_name": first_name, "birth_date": birth_date, "chess_id": chess_id}

    def display_players(self, players):
        print("\nListe des joueurs :")
        for player in players:
            print(f"{player['chess_id']} - {player['last_name']} {player['first_name']} "
                  f"{player['birth_date']}")
