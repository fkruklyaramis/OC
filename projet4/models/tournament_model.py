from typing import Optional
from pydantic import BaseModel


class Tournament(BaseModel):
    name: str
    location: str
    startDate: str
    endDate: str
    roundNumber: 4
    roundId: Optional[int]
    roundList: Optional[list]
    playerList: list
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
