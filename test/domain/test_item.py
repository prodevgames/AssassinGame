from unittest import TestCase, skip

from assassin_game_csss.domain.item import Item
from test.test_helper.anon import anon_item, anon_string


class TestItem(TestCase):

    def test__constructor__shouldThrowException__whenGivenNonString(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): Item(None)

        # noinspection PyTypeChecker
        def action_int(): Item(42)

        # noinspection PyTypeChecker
        def action_set(): Item(set())

        # noinspection PyTypeChecker
        def action_list(): Item([])

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Item("")

        # Assert
        self.assertRaises(ValueError, action)

    def test__name__shouldReturnName__whenAccessed(self):
        # Arrange
        expected_name = anon_string()
        item = Item(expected_name)

        # Act
        actual = item.name

        # Assert
        self.assertEqual(expected_name, actual)

    def test__name__shouldRaiseException__whenAttemptingToSet(self):
        # Arrange
        item = anon_item()

        # Act
        # noinspection PyPropertyAccess
        def action(): item.name = anon_string()

        # Assert
        self.assertRaises(AttributeError, action)

    def test__equals__shouldReturnTrue__whenNameIsSame(self):
        # Arrange
        name = anon_string()
        item_a = Item(name)
        item_b = Item(name)

        # Act
        actual = (item_a == item_b)

        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenNameIsDifferent(self):
        # Arrange
        item_a = Item(anon_string())
        item_b = Item(anon_string())

        # Act
        actual = (item_a == item_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldReturnSameHash__whenNameIsSame(self):
        # Arrange
        name = anon_string()
        item_a = Item(name)
        item_b = Item(name)

        # Act
        hash_a = hash(item_a)
        hash_b = hash(item_b)

        # Assert
        self.assertEqual(hash_a, hash_b)

    def test__hash__shouldReturnDifferentHash__whenNameIsDifferent(self):
        # Arrange
        item_a = Item(anon_string())
        item_b = Item(anon_string())

        # Act
        hash_a = hash(item_a)
        hash_b = hash(item_b)

        # Assert
        self.assertNotEqual(hash_a, hash_b)

    @skip("Not Yet Implemented")
    def test__str__shouldReturnStringForm(self):
        # Arrange
        expected_name = anon_string()
        item = Item(expected_name)

        # Act
        actual = str(item)

        # Assert
        self.assertEqual(expected_name, actual)

    @skip("Not Yet Implemented")
    def test__repr__shouldReturnRepresentation(self):
        # Arrange
        name = anon_string()
        expected_string = "%s(\"%s\")" % (Item.__name__, name)
        item = Item(name)

        # Act
        actual = repr(item)

        # Assert
        self.assertEqual(expected_string, actual)
