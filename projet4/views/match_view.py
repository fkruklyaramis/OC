
import models.match_model as match_model


class MatchView():
    def __init__(self, match_data: tuple):
        self.match = match_data

    def play_match(self):
        player1 = self.match[0][0]
        player2 = self.match[1][0]

        result = None
        while result not in match_model.SCORE_MAPPING:
            result = int(input(f"Player 1 : {player1.first_name} {player1.last_name}"
                               f" VS "
                               f"Player 2 : {player2.first_name} {player2.last_name}"
                               f"\nWho is the winner ? 0 (if null), 1 or 2 : ").strip())
            if result in match_model.SCORE_MAPPING:
                scores = match_model.SCORE_MAPPING[result]
                self.match[0][1] = scores[0]
                self.match[1][1] = scores[1]
                return scores
            else:
                print("invalid input : fill 0 (if null), 1 or 2")
