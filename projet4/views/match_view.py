
import models.match_model as match_model


class MatchView():
    def __init__(self, match_data: tuple, colors: dict):
        self.match = match_data
        self.colors = colors

    def play_match(self, match_number: int, total_matches: int):
        """
        Executes the match play process and updates the match results.
        This method coordinates with the view to get match results and updates
        the match model with the scores. The scores are stored at specific indexes
        in the match data structure.
        Returns:
            dict: A dictionary containing the match data after updating the results
        """

        player1 = self.match[0][0]
        player2 = self.match[1][0]

        result = None
        print(f"\nMatch {match_number} of {total_matches}")

        while result not in match_model.SCORE_MAPPING:
            result = int(input(f"Player 1 : {player1.first_name} {player1.last_name} ({self.colors['player1_color']})"
                               f" VS "
                               f"Player 2 : {player2.first_name} {player2.last_name} ({self.colors['player2_color']})"
                               f"\nWho is the winner ? 0 (if null), 1 or 2 : ").strip())
            if result in match_model.SCORE_MAPPING:
                scores = match_model.SCORE_MAPPING[result]
                self.match[0][1] = scores[0]
                self.match[1][1] = scores[1]
                player1.point += scores[0]
                player2.point += scores[1]
                print("Match result:")
                print(f"{player1.first_name} {player1.last_name} : +{scores[0]} point(s) (Total: {player1.point})")
                print(f"{player2.first_name} {player2.last_name}: +{scores[1]} point(s) (Total: {player2.point})")
                return scores
            else:
                print("Invalid input : fill 0 (if null), 1 or 2")
