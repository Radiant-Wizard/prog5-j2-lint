from dataclasses import dataclass
from enum import Enum


class Size(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    BIG = "BIG"


@dataclass
class Wallet:
    def __init__(
        self,
        color: str,
        size: Size,
        owner: str,
    ) -> None:
        self.color = color
        self.size = size
        self.owner = owner
        self.isLost = False
        self.isOpen = False
        self.balance = 0.0

    def getVola(self, amountTaken) -> None:
        self.balance -= amountTaken

    def addVola(self, amountAdded) -> None:
        self.balance += amountAdded

    def checkVola(self) -> float:
        return self.balance
