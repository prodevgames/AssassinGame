from assassin_game_csss.adapter.repository.in_memory_item_repo import InMemoryItemRepo
from test.domain.repository.test_abstract_item_repo import TestAbstractItemRepo


class TestInMemoryItemRepo(TestAbstractItemRepo):

    def _get_instance(self):
        return InMemoryItemRepo()
