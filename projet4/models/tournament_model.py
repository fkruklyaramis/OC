from typing import Optional
from pydantic import BaseModel, Field
from typing import List
from models.player_model import Player


class Tournament(BaseModel):
    name: str
    location: str
    startDate: str
    endDate: str
    roundNumber: int = Field(default=4)
    roundId: Optional[int] = Field(default=None)
    roundList: List[dict] = []
    playerList: List[Player]
    description: str

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "roundNumber": self.roundNumber,
            "roundId": self.roundId,
            "roundList": self.roundList,
            "playerList": self.playerList,
            "description": self.description
        }
