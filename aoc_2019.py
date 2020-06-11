import os


def calculate_basic_fuel(module_mass):
    return module_mass // 3 - 2


def calculate_total_basic_fuel(module_mass_list):
    total_fuel = 0

    for mass in module_mass_list:
        total_fuel += calculate_basic_fuel(mass)

    return total_fuel


def calculate_fuel(module_mass):
    total_fuel = 0

    basic_fuel = calculate_basic_fuel(module_mass)
    while basic_fuel > 0:
        total_fuel += basic_fuel
        basic_fuel = calculate_basic_fuel(basic_fuel)

    return total_fuel


def calculate_total_fuel(module_mass_list):
    total_fuel = 0

    for mass in module_mass_list:
        total_fuel += calculate_fuel(mass)

    return total_fuel


def gravity_assist_program(initial_state):
    idx = 0
    state_length = len(initial_state)
    while idx < state_length:
        int_code = initial_state[idx]
        opcode = __get_opcode(int_code)

        if not opcode or not opcode["func"]:
            return initial_state

        idx += 1
        args_count = opcode["args"]
        opcode["func"](initial_state, *initial_state[idx : idx + args_count])

        idx += args_count

    return initial_state


def __get_opcode(key):
    code = [x for x in OPCODES if x["key"] == key]
    if not code:
        return None

    return code[0]


def __intcode_one(*args):
    arr = args[0]
    pos_x = args[1]
    pos_y = args[2]
    pos_res = args[3]

    arr[pos_res] = arr[pos_x] + arr[pos_y]


def __intcode_two(*args):
    arr = args[0]
    pos_x = args[1]
    pos_y = args[2]
    pos_res = args[3]

    arr[pos_res] = arr[pos_x] * arr[pos_y]


OPCODES = [
    {"key": 1, "args": 3, "func": __intcode_one},
    {"key": 2, "args": 3, "func": __intcode_two},
    {"key": 99, "args": 0, "func": None},
]
