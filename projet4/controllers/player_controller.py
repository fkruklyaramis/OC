import json
from models.player_model import Player
from views.player_view import PlayerView


class PlayerController():

    def __init__(self, view: PlayerView):
        self.view = view
        self.players_file = "./data/players.json"
        self.menu_choice_list = [{'value': 1, 'label': 'Add a player', 'callback': self.add_player},
                                 {'value': 2, 'label': 'List player', 'callback': self.list_players},
                                 {'value': 3, 'label': 'Back to main menu', 'callback': None}]
        self.view.set_choice_list(self.menu_choice_list)

    def manage_players(self):
        """
        Manages player-related operations through a menu system.
        This method displays a menu to the user through the view component and processes
        the user's choice. It matches the user's selection with predefined menu options
        and executes the corresponding callback function if one exists.
        Returns:
        Notes:
            - The method relies on self.view.menu() to display and get user input
            - Menu choices are stored in self.menu_choice_list
            - Each valid menu choice should have a 'callback' function defined
        """

        choice = self.view.menu()
        menu_choice = next((item for item in self.menu_choice_list if item['value'] == choice), None)
        if menu_choice and 'callback' in menu_choice:
            menu_choice['callback']()
        else:
            None

    def add_player(self):
        """
        Add a new player to the database.
        This method collects player details through the view, creates a new Player instance,
        and saves it to the database.
        Returns:
            None
        Side Effects:
            - Creates a new player entry in the database
            - Prints success message to console
        """

        data = self.view.get_player_details()
        player = Player(**data)
        self.save_player(player)
        print("Player added successfully!")

    def list_players(self):
        """
        List all players in the database.
        This method loads all players from the database and displays them through the view.
        Returns:
            None
        Side Effects:
            - Displays a list of all players to the console
        """
        players = self.load_players()
        self.view.display_players(players)

    def save_player(self, player: Player):
        """
        Save a player to the database.
        This method loads the current list of players from the database, adds the new player,
        and writes the updated list back to the database.
        Args:
            player (Player): The player instance to save
        Returns:
            None
        Side Effects:
            - Updates the players database file
        """
        try:
            with open(self.players_file, "r") as file:
                players = json.load(file)
        except FileNotFoundError:
            players = []

        players.append(player.to_dict())

        with open(self.players_file, "w") as file:
            json.dump(players, file, indent=4)

    def load_players(self):
        """
        Load all players from the database.
        This method reads the list of players from the database file.
        Returns:
            list: A list of player dictionaries
        """

        try:
            with open(self.players_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
