
from views.tournament_view import TournamentView
from controllers.tournament_controller import TournamentController


def main():
    while True:
        print("Bienvenue dans le gestionnaire de tournois d'échecs !")
        main_view = TournamentView()
        TournamentController(main_view).manage_tournament()


if __name__ == "__main__":
    main()
