from abc import abstractmethod, ABC

from assassin_game_csss.domain.item import Item


class AbstractItemRepo(ABC):

    @abstractmethod
    def save(self, item: Item) -> None:
        pass

    @abstractmethod
    def retrieve_all(self) -> frozenset:
        pass

    @abstractmethod
    def delete(self, item: Item) -> None:
        pass
