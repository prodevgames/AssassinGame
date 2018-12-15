from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.item import Item


class Target:
    __player: Player = None
    __item: Item = None
    __location: Location = None

    def __init__(self, player: Player, item: Item, location: Location):
        if not isinstance(player, Player) or not isinstance(item, Item) or not isinstance(location, Location):
            raise TypeError
        self.__player = player
        self.__item = item
        self.__location = location

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def item(self) -> Item:
        return self.__item

    @property
    def location(self) -> Location:
        return self.__location
