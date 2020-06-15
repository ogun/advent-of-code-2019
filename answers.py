import math
from data import problem1, problem3, problem6
import aoc_2019


def answer1():
    return aoc_2019.calculate_total_basic_fuel(problem1.MODULES)


def answer2():
    return aoc_2019.calculate_total_fuel(problem1.MODULES)


def answer3():
    memory = problem3.MEMORY.copy()
    return aoc_2019.intcode_program(memory, noun=12, verb=2)


def answer4():
    expected = 19690720

    for noun in range(100):
        for verb in range(100):
            memory = problem3.MEMORY.copy()
            actual = aoc_2019.intcode_program(memory, noun, verb)
            if actual == expected:
                return 100 * noun + verb

    return 100 * noun + verb


def answer5():
    return aoc_2019.calculate_intersection_manhattan_distance(problem6.WIRES)


def answer6():
    return aoc_2019.calculate_intersection_fewest_combined_step(problem6.WIRES)


def answer7():
    total_correct_result = 0

    for number in range(197487, 673251):
        if answer7_rules(number):
            total_correct_result += 1

    return total_correct_result


def answer7_rules(value):
    digits = [int(x) for x in list(str(value))]

    if len(digits) != 6:
        return False

    double = False
    decreasing = False

    previous = 0
    for digit in digits:
        if digit == previous:
            double = True

        if previous > digit:
            decreasing = True

        previous = digit

    if not double:
        return False

    if decreasing:
        return False

    return True


def answer8():
    total_correct_result = 0

    for number in range(197487, 673251):
        if answer8_rules(number):
            total_correct_result += 1

    return total_correct_result


def answer8_rules(value):
    digits = [int(x) for x in list(str(value))]
    digit_set = set(digits)
    if not 2 in [
        len(list(filter(lambda digit: digit == y, digits)))
        for y in [x for x in digit_set]
    ]:
        return False

    if len(digits) != 6:
        return False

    decreasing = False

    previous = 0
    for digit in digits:
        if previous > digit:
            decreasing = True

        previous = digit

    if decreasing:
        return False

    return True
