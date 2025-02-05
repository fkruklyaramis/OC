from pydantic import BaseModel


class Round(BaseModel):
    name: str
    matchList: list
    startDate: str
    endDate: str
    