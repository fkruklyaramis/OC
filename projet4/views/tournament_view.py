class TournamentView:

    def get_tournament_details(self):
        print("Création du tournois :")
        tournament_name = input("Nom: ")
        tournament_location = input("Lieu : ")
        startDate = input("Date de début(YYYY-MM-DD) : ")
        endDate = input("Date de fin(YYYY-MM-DD) : ")
        playerList = input("Joueurs : ")
        description = input("Description : ")
        # créer l'objet ici et le retourner
        return {"tournament_name": tournament_name, "tournament_location": tournament_location,
                "startDate": startDate, "endDate": endDate, playerList: playerList, "description": description}

    def menu(self, choice_list: list[dict]):
        for value in choice_list:
            print(f"{value['value']} : {value['label']}")
        choice = int(input("Choisissez une option : "))
        return choice
