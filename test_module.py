import unittest
from RPS_game import play, one, two, three, four
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_one(self):
        print("Testing game against one...")
        actual = play(player, one, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat one at least 60% of the time.')

    def test_player_vs_two(self):
        print("Testing game against two...")
        actual = play(player, two, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat two at least 60% of the time.')

    def test_player_vs_three(self):
        print("Testing game against three...")
        actual = play(player, three, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat three at least 60% of the time.')

    def test_player_vs_four(self):
        print("Testing game against four...")
        actual = play(player, four, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat four at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
