from unittest import TestCase

from assassin_game_csss.domain.item import Item
from test.test_helper.anon import anon_item


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
        expected_name = "Test Name"
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
        def action(): item.name = "New Name"

        # Assert
        self.assertRaises(AttributeError, action)

    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        item_a = Item("Identical Name")
        item_b = Item("Identical Name")

        # Act
        actual = (item_a == item_b)

        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        item_a = Item("Not Item B")
        item_b = Item("Not Item A")

        # Act
        actual = (item_a == item_b)

        # Assert
        self.assertFalse(actual)

    def test__equals__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        item_a = Item("Identical Name")
        item_b = Item("Identical Name")
        items = {item_a}

        # Act
        items.add(item_b)

        # Assert
        self.assertEqual(1, len(items))

    def test__equals__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        item_a = Item("Not Item B")
        item_b = Item("Not Item A")
        items = {item_a}

        # Act
        items.add(item_b)

        # Assert
        self.assertEqual(2, len(items))
