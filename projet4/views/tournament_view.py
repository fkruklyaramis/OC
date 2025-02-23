from views.interface_view import InterfaceView


class TournamentView(InterfaceView):

    def __init__(self):
        super().__init__()
        self.players = []

    def set_players_list(self, players):
        """
        Sets a list of players for the tournament.
        Args:
            players (list): A list of Player objects to be associated with the tournament
        Returns:
            None
        """

        self.players = players

    def get_tournament_details(self):
        """Gets tournament details from user input.
        This method prompts the user to enter various tournament details including name,
        location, start date, end date, list of players, and description.
        Returns:
            dict: A dictionary containing the tournament details with the following keys:
                - name (str): Name of the tournament
                - location (str): Location where tournament takes place
                - startDate (str): Start date in YYYY-MM-DD format
                - endDate (str): End date in YYYY-MM-DD format
                - playerList (list): List of selected players
                - description (str): Tournament description
        """

        print("Create tournament")
        tournament_name = input("Name: ")
        tournament_location = input("Location : ")
        startDate = input("Start date (YYYY-MM-DD) : ")
        endDate = input("End date (YYYY-MM-DD) : ")
        playerList = self.select_players()
        description = input("Description : ")
        # créer l'objet ici et le retourner
        return {"name": tournament_name, "location": tournament_location,
                "startDate": startDate, "endDate": endDate, "playerList": playerList, "description": description}

    def select_players(self) -> list:
        """
        Allows user to select players from a list of available players.
        This method displays all available players and prompts the user to select players
        by entering their chess IDs. It validates the selections and returns a list of
        selected players.
        Returns:
            list: A list of dictionaries containing the selected players' information.
                  Returns empty list if no players are registered.
                  Each player dictionary contains:
                  - 'first_name': Player's first name
                  - 'last_name': Player's last name
                  - 'chess_id': Player's chess ID
        Example:
            >>> view = TournamentView()
            >>> selected_players = view.select_players()
            List of available players:
            - John Doe (ID: AB12345)
            - Jane Smith (ID: CD67890)
            Enter chess IDs of players (separated by commas): AB12345, CD67890
            Selected players:
            - John Doe (ID: AB12345)
            - Jane Smith (ID: CD67890)
        """

        if not self.players:
            print("No registered players.")
            return []

        print("\nAvailable players :")
        for player in self.players:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        selected_ids = input("\nEnter players' chess IDs (separated by comma): ").strip().split(',')

        player_list = []
        for chess_id in selected_ids:
            chess_id = chess_id.strip()
            player = next((p for p in self.players if p['chess_id'] == chess_id), None)
            if player:
                player_list.append(player)
            else:
                print(f"Chess id {chess_id} unknown.")

        print("\nSelected players :")
        for player in player_list:
            print(f"- {player['first_name']} {player['last_name']} (ID: {player['chess_id']})")

        return player_list
