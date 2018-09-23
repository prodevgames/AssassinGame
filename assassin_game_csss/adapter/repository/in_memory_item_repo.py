from assassin_game_csss.domain.repository.abstract_item_repo import AbstractItemRepo
from assassin_game_csss.domain.item import Item


class InMemoryItemRepo(AbstractItemRepo):
    def save(self, item: Item) -> None:
        raise NotImplementedError

    def retrieve_all(self) -> set:
        raise NotImplementedError

    def delete(self, item: Item) -> bool:
        raise NotImplementedError
