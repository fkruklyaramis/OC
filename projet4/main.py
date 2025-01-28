from views.player_view import PlayerView
from controllers.player_controller import PlayerController


def main():
    print("Bienvenue dans le gestionnaire de tournois d'échecs !")
    PlayerController(PlayerView()).manage_players()


if __name__ == "__main__":
    main()
