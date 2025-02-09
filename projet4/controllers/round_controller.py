from views.round_view import RoundView
from models.round_model import Round
from models.tournament_model import Tournament
from controllers.match_controller import MatchController
import datetime
import random


class RoundController:
    MATCH_NULL_SCORE = 0.5
    MATCH_WIN_SCORE = 1
    MATCH_LOOSE_SCORE = 0
    MATCH_RESULT_CHOICE_LIST = [0, 1, 2]

    def __init__(self, view: RoundView, tournament: Tournament):
        self.view = RoundView()
        self.tournament = tournament

    def manage_rounds(self):
        for i in range(0, self.tournament.roundNumber):
            print(f"Round {i+1} started")
            if i == 0:
                players = self.tournament.playerList.copy()
                random.shuffle(players)
            else:
                players = self.tournament.playerList
            if len(players) >= 2:
                # call here pair_players method
                player1_selected = players[0]['chess_id']
                player2_selected = players[1]['chess_id']
                winner = None
                while winner not in self.MATCH_RESULT_CHOICE_LIST:
                    winner = int(input(f"Player 1 : {player1_selected} VS Player 2 : {player2_selected}\n"
                                       f"who is the winner ? 0 (if null), 1 or 2 : ").strip())
                    if winner in self.MATCH_RESULT_CHOICE_LIST:
                        if winner == 0:
                            player1 = [player1_selected, self.MATCH_NULL_SCORE]
                            player2 = [player1_selected, self.MATCH_NULL_SCORE]
                        elif winner == 1:
                            player1 = [player1_selected, self.MATCH_WIN_SCORE]
                            player2 = [player1_selected, self.MATCH_LOOSE_SCORE]
                        elif winner == 2:
                            player1 = [player1_selected, self.MATCH_LOOSE_SCORE]
                            player2 = [player1_selected, self.MATCH_WIN_SCORE]
                    else:
                        print("invalid input : fill 0 (if null), 1 or 2")

            else:
                print("Pas assez de joueurs pour créer un match.")
                break
            match = self.new_match(player1, player2)
            round = Round(
                number=i,
                name=f"Round {i}",
                matchList=match.append(match)
                )

            round.endDate = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Rounds finished")

    def new_match(self):
        match_controller = MatchController(self.tournament)
        match_controller.manage_matches()

    def pair_players(self):
        # Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
        # Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4
        # Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
        # Lors de la génération des paires, évitez de créer des matchs identiques
        # (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
        # Par exemple, si le joueur 1 a déjà joué contre le joueur 2,associez-le plutôt au joueur 3.
        pass
