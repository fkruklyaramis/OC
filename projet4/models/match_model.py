from typing import List, Tuple
from pydantic import BaseModel


class Match(BaseModel):
    match: Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]
