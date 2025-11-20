from dataclasses import dataclass


@dataclass
class Wallet:
    def __init__(
        self,
        color: str,
        size: int,
        owner: str,
    ) -> None:
        self._color = color
        self._size = size
        self._owner = owner
        self._isLost = False
        self._balance = 0.0
