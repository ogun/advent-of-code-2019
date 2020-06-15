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

    def test_convert_path_string(self):
        tests = [
            ("R8", ("R", 8)),
            ("L1143", ("L", 1143)),
            ("D1", ("D", 1)),
            ("U82", ("U", 82)),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.convert_path_string(value)
                self.assertEqual(actual, expected)

    def test_convert_path_to_wire(self):
        tests = [
            ([("R", 1)], [(0, 0), (1, 0)]),
            ([("L", 1)], [(0, 0), (-1, 0)]),
            ([("U", 1)], [(0, 0), (0, 1)]),
            ([("D", 1)], [(0, 0), (0, -1)]),
            ([("R", 2)], [(0, 0), (1, 0), (2, 0)]),
            ([("L", 2)], [(0, 0), (-1, 0), (-2, 0)]),
            ([("U", 2)], [(0, 0), (0, 1), (0, 2)]),
            ([("D", 2)], [(0, 0), (0, -1), (0, -2)]),
            ([("D", 2), ("D", 2)], [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4)]),
            ([("D", 2), ("D", 2)], [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4)]),
            (
                [("U", 2), ("R", 2), ("D", 2), ("L", 2)],
                [
                    (0, 0),
                    (0, 1),
                    (0, 2),
                    (1, 2),
                    (2, 2),
                    (2, 1),
                    (2, 0),
                    (1, 0),
                    (0, 0),
                ],
            ),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.convert_path_to_wire(value)
                self.assertEqual(actual, expected)

    def test_find_intersection(self):
        tests = [
            (
                (
                    [(0, 0), (1, 0), (2, 0), (3, 0)],
                    [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 0)],
                ),
                {(3, 0)},
            )
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.find_wire_intersections(value[0], value[1])
                self.assertEqual(actual, expected)

    def test_find_wires_cross_locations(self):
        tests = [(["R8,U5,L5,D3", "U7,R6,D4,L4"], {(3, 3), (6, 5)})]

        for value, expected in tests:
            with self.subTest(value=value):
                actual, _, _ = aoc_2019.find_wires_cross_locations(value)
                self.assertEqual(actual, expected)

    def test_calculate_intersection_manhattan_distance(self):
        tests = [
            (["R8,U5,L5,D3", "U7,R6,D4,L4"], 6),
            (
                [
                    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                    "U62,R66,U55,R34,D71,R55,D58,R83",
                ],
                159,
            ),
            (
                [
                    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                ],
                135,
            ),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.calculate_intersection_manhattan_distance(value)
                self.assertEqual(actual, expected)

    def test_calculate_intersection_fewest_combined_step(self):
        tests = [
            (["R8,U5,L5,D3", "U7,R6,D4,L4"], 30),
            (
                [
                    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                    "U62,R66,U55,R34,D71,R55,D58,R83",
                ],
                610,
            ),
            (
                [
                    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                ],
                410,
            ),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                actual = aoc_2019.calculate_intersection_fewest_combined_step(value)
                self.assertEqual(actual, expected)
