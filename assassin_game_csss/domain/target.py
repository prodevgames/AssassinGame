from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.item import Item


class Target:
    __player: Player = None
    __item: Item = None
    __location: Location = None

    def __init__(self, player: Player, item: Item, location: Location):
        raise NotImplementedError

    def get_player(self):
        raise NotImplementedError

    def get_item(self):
        raise NotImplementedError

    def get_location(self):
        raise NotImplementedError