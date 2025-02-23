from pydantic import BaseModel


class Player(BaseModel):
    last_name: str
    first_name: str
    birth_date: str
    chess_id: str
    point: float = 0.0

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id
        }

    def __hash__(self):
        return hash(self.chess_id)

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.chess_id == other.chess_id
