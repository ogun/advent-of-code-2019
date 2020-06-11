import unittest
import aoc_2019


class TestAOC2019(unittest.TestCase):
    def test_calculate_basic_fuel(self):
        tests = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.calculate_basic_fuel(value)
                self.assertEqual(actual, expected)

    def test_calculate_total_basic_fuel(self):
        tests = [([12, 14], 4), ([12, 14, 1969], 658), ([12, 14, 100756], 33587)]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.calculate_total_basic_fuel(value)
                self.assertEqual(actual, expected)

    def test_calculate_fuel(self):
        tests = [(14, 2), (1969, 966), (100756, 50346)]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.calculate_fuel(value)
                self.assertEqual(actual, expected)
