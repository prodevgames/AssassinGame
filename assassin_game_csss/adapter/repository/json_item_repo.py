from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.repository.abstract_item_repo import AbstractItemRepo


class JsonItemRepo(AbstractItemRepo):

    def __init__(self, filepath: str):
        pass

    def save(self, item: Item) -> None:
        pass

    def retrieve_all(self) -> set:
        pass

    def delete(self, item: Item) -> None:
        pass
