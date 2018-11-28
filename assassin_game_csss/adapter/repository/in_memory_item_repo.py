from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.repository.abstract_item_repo import AbstractItemRepo


class InMemoryItemRepo(AbstractItemRepo):

    __items: set = None

    def __init__(self):
        self.__items = set()

    def save(self, item: Item) -> None:
        if type(item) is not Item:
            raise TypeError("Invalid type given as item argument")

        self.__items.add(item)

    def retrieve_all(self) -> set:
        return self.__items.copy()

    def delete(self, item: Item) -> None:
        if type(item) is not Item:
            raise TypeError("Invalid type given as item argument")

        self.__items.remove(item)
