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
    return answer5_closest_intersection(problem6.WIRES)


def answer5_closest_intersection(wires):
    sets = []

    for wire in wires:
        paths = wire.split(",")

        new_set = set()
        current_x = 0
        current_y = 0
        for path in paths:
            direction = path[0:1]
            step = int(path[1:])
            if direction == "U":
                for i in range(current_y + 1, current_y + step + 1):
                    current_y = i
                    new_set.add((current_x, current_y))
            elif direction == "D":
                for i in range(current_y - 1, current_y - (step + 1), -1):
                    current_y = i
                    new_set.add((current_x, i))
            elif direction == "R":
                for i in range(current_x + 1, current_x + step + 1):
                    current_x = i
                    new_set.add((current_x, current_y))
            elif direction == "L":
                for i in range(current_x - 1, current_x - (step + 1), -1):
                    current_x = i
                    new_set.add((current_x, current_y))
        sets.append(new_set)

    intersections = sets[0].intersection(sets[1])

    return min(abs(x[0]) + abs(x[1]) for x in intersections)


def answer6():
    return answer6_closest_path(problem6.WIRES)


def answer6_closest_path(wires):
    sets = []
    lists = []

    for wire in wires:
        paths = wire.split(",")

        new_set = set()
        new_list = list()
        current_x = 0
        current_y = 0
        for path in paths:
            direction = path[0:1]
            step = int(path[1:])
            if direction == "U":
                for i in range(current_y + 1, current_y + step + 1):
                    current_y = i
                    new_set.add((current_x, current_y))
                    new_list.append((current_x, current_y))
            elif direction == "D":
                for i in range(current_y - 1, current_y - (step + 1), -1):
                    current_y = i
                    new_set.add((current_x, i))
                    new_list.append((current_x, i))
            elif direction == "R":
                for i in range(current_x + 1, current_x + step + 1):
                    current_x = i
                    new_set.add((current_x, current_y))
                    new_list.append((current_x, current_y))
            elif direction == "L":
                for i in range(current_x - 1, current_x - (step + 1), -1):
                    current_x = i
                    new_set.add((current_x, current_y))
                    new_list.append((current_x, current_y))
        sets.append(new_set)
        lists.append(new_list)

    intersections = sets[0].intersection(sets[1])

    return min(lists[0].index(x) + lists[1].index(x) + 2 for x in intersections)


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
