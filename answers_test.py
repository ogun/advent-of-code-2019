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
        actual = answers.answer5()
        expected = 446
        self.assertEqual(actual, expected)

    def test_answer6(self):
        actual = answers.answer6()
        expected = 9006
        self.assertEqual(actual, expected)

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
