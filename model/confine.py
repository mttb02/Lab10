from dataclasses import dataclass


@dataclass
class Confine:
    _country1: str
    _country2: str
    _conntype: int

    @property
    def country1(self):
        return self._country1

    @property
    def country2(self):
        return self._country2

    @property
    def conntype(self):
        return self._conntype

    def __hash__(self):
        return self._country1 + self._country2

    def __str__(self):
        return f"{self._country1 + self._country2}"
