from views.player_view import PlayerView
from controllers.player_controller import PlayerController


def main():
    print("Bienvenue dans le gestionnaire de tournois d'échecs !")
    view = PlayerView()
    PlayerController(view).manage_players()
    # only one while here to manage all menus


if __name__ == "__main__":
    main()
