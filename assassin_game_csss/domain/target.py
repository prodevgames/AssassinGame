from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player


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

    def __hash__(self):
        return hash((self.__player, self.__item, self.__location))

    def __eq__(self, other):
        if not isinstance(other, Target):
            raise TypeError
        return hash(self) == hash(other)

    def __str__(self):
        return "%s at %s with a %s" % (str(self.__player), str(self.__location), str(self.__item))

    def __repr__(self):
        return "%s(%s, %s, %s)" % (
            self.__class__.__name__, repr(self.__player), repr(self.__location), repr(self.__item))
