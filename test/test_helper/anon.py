from random import choices
from string import ascii_letters, digits, ascii_lowercase

from assassin_game_csss.domain.game import Game
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.target import Target
from assassin_game_csss.domain.upid import UPID


def anon_string(count: int = 10) -> str:
    return ''.join(choices(ascii_letters + digits, k=count))


def anon_player() -> Player:
    return Player(anon_string(), anon_upid())


def anon_upid() -> UPID:
    return UPID("%s%s" % ("".join(choices(ascii_lowercase, k=3)),
                          "".join(choices(digits, k=3))))


def anon_location() -> Location:
    return Location(anon_string())


def anon_item() -> Item:
    return Item(anon_string())


def anon_target() -> Target:
    return Target(anon_player(), anon_item(), anon_location())


def anon_game(players: set = None, items: set = None, locations: set = None) -> Game:
    if players is None:
        players = {anon_player(), anon_player(), anon_player()}
    if items is None:
        items = {anon_item(), anon_item(), anon_item()}
    if locations is None:
        locations = {anon_location(), anon_location(), anon_location()}
    game = Game(players, items, locations)
    return game
