from pydantic import BaseModel
from datetime import datetime


class Round(BaseModel):
    number: int
    name: str = None
    matchList: list = []
    startDate: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    endDate: str = None

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "matchList": self.matchList,
            "startDate": self.startDate,
            "endDate": self.endDate
        }
