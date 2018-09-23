from unittest import skip

from assassin_game_csss.domain.repository.abstract_item_repo import AbstractItemRepo
from test.test_helper.abstract_test_case import AbstractTestCase
from test.test_helper.anon import anon_item


class TestAbstractItemRepo(AbstractTestCase):

    _item_repo: AbstractItemRepo = None

    def setUp(self):
        self._item_repo = self._get_instance()

    @skip("Not Yet Implemented")
    def test__save__shouldThrowException__whenProvidedNonItemArg(self):

        # Act
        # noinspection PyTypeChecker
        def action(): self._item_repo.save(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__save__shouldNotThrowException__whenProvidedValidItemArg(self):

        # Arrange
        item = anon_item()

        # Act
        self._item_repo.save(item)

    @skip("Not Yet Implemented")
    def test__save__shouldNotThrowException__whenItemAlreadyExistsInRepo(self):
        # Arrange
        item = anon_item()
        self._item_repo.save(item)

        # Act
        self._item_repo.save(item)

    @skip("Not Yet Implemented")
    def test__save__shouldNotSaveDuplicateItem__whenItemAlreadyExistsInRepo(self):
        # Arrange
        item = anon_item()
        self._item_repo.save(item)

        # Act
        self._item_repo.save(item)

        # Assert
        items = self._item_repo.retrieve_all()
        self.assertEqual(1, len(items))

    @skip("Not Yet Implemented")
    def test__retrieve_all__shouldReturnEmptySet__whenRepoIsEmpty(self):

        # Act
        items = self._item_repo.retrieve_all()

        # Assert
        self.assertIsInstance(set, items)
        self.assertEqual(0, len(items))

    @skip("Not Yet Implemented")
    def test__retrieve_all__shouldReturnSavedItem__whenOnlyOneItemStored(self):

        # Arrange
        expected_item = anon_item()
        self._item_repo.save(expected_item)

        # Act
        items = self._item_repo.retrieve_all()

        # Assert
        actual = items.pop()
        self.assertEqual(expected_item, actual)

    @skip("Not Yet Implemented")
    def test__retrieve_all__shouldReturnAllSavedItems__whenMultipleItemsStored(self):

        # Arrange
        item1 = anon_item()
        item2 = anon_item()
        item3 = anon_item()
        self._item_repo.save(item1)
        self._item_repo.save(item2)
        self._item_repo.save(item3)

        # Act
        items = self._item_repo.retrieve_all()

        # Assert
        self.assertEqual({item1, item2, item3}, items)

    @skip("Not Yet Implemented")
    def test__delete__shouldThrowException__whenArgumentIsNotOfTypeItem(self):

        # Act
        # noinspection PyTypeChecker
        def action(): self._item_repo.delete(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__delete__shouldThrowException__whenRepositoryIsEmpty(self):

        # Act
        def action(): self._item_repo.delete(anon_item())

        # Assert
        self.assertRaises(KeyError, action)

    @skip("Not Yet Implemented")
    def test__delete__shouldThrowException__whenRepositoryContainsItemsButNotTheDeletedOne(self):

        # Arrange
        self._item_repo.save(anon_item())
        self._item_repo.save(anon_item())

        # Act
        def action(): self._item_repo.delete(anon_item())

        # Assert
        self.assertRaises(KeyError, action)

    @skip("Not Yet Implemented")
    def test__delete__shouldNotModifyEntries__whenDeleteCalledWithItemNotInRepo(self):

        # Arrange
        item1 = anon_item()
        item2 = anon_item()
        self._item_repo.save(item1)
        self._item_repo.save(item2)

        # Act
        try:
            self._item_repo.delete(anon_item())
        except KeyError:
            pass

        # Assert
        items = self._item_repo.retrieve_all()
        self.assertEqual({item1, item2}, items)

    @skip("Not Yet Implemented")
    def test__delete__shouldRemoveItem__whenItemExistsInRepository(self):

        # Arrange
        item = anon_item()
        expected_item1 = anon_item()
        expected_item2 = anon_item()
        self._item_repo.save(expected_item1)
        self._item_repo.save(expected_item2)
        self._item_repo.save(item)

        # Act
        self._item_repo.delete(item)

        # Assert
        items = self._item_repo.retrieve_all()
        self.assertEqual({expected_item1, expected_item2}, items)
