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

    def test_gravity_assist_program(self):
        tests = [
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            (
                [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
                [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
            ),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.intcode_program_internal(value)
                self.assertEqual(actual, expected)
