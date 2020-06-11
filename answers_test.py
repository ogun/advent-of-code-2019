import unittest
import answers


class TestAnswers(unittest.TestCase):
    def test_answer1(self):
        actual = answers.answer1()
        expected = 3415076
        self.assertEqual(actual, expected)

    def test_answer2(self):
        actual = answers.answer2()
        expected = 5119745
        self.assertEqual(actual, expected)

    def test_answer3(self):
        actual = answers.answer3()
        expected = 5305097
        self.assertEqual(actual, expected)

    def test_answer4(self):
        actual = answers.answer4()
        expected = 4925
        self.assertEqual(actual, expected)

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
