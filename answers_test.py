import unittest
import answers


class TestAnswers(unittest.TestCase):
    def test_answer1(self):
        tests = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]

        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(answers.answer1_get_fuel(value), expected)

    def test_answer2(self):
        tests = [(14, 2), (1969, 966), (100756, 50346)]

        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(answers.answer2_get_fuel(value), expected)

    def test_answer3(self):
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
                self.assertEqual(answers.answer3_execute(value), expected)

    def test_answer5(self):
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
                self.assertEqual(answers.answer5_closest_intersection(value), expected)

    def test_answer6(self):
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
                self.assertEqual(answers.answer6_closest_path(value), expected)

    def test_answer7(self):
        tests = [
            (123, False),
            (122345, True),
            (111123, True),
            (135679, False),
            (111111, True),
            (223450, False),
            (123789, False),
        ]

        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(answers.answer7_rules(value), expected)

    def test_answer8(self):
        tests = [(112233, True), (123444, False), (111122, True), (223444, True)]

        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(answers.answer8_rules(value), expected)


if __name__ == "__main__":
    unittest.main()
