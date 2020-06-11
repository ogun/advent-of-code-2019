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


def gravity_assist_program(memory):
    instruction_pointer = 0
    memory_size = len(memory)
    while instruction_pointer < memory_size:
        opcode = memory[instruction_pointer]
        instruction = __get_instruction(opcode)

        if not instruction or not instruction["func"]:
            return memory

        instruction_pointer += 1
        param_count = instruction["param_count"]
        instruction["func"](
            memory, memory[instruction_pointer : instruction_pointer + param_count]
        )

        instruction_pointer += param_count

    return memory


def __get_instruction(opcode):
    instructions = [x for x in INSTRUCTIONS if x["opcode"] == opcode]
    if not instructions:
        return None

    return instructions[0]


def __intcode_one(memory, params):
    addr_x = params[0]
    addr_y = params[1]
    addr_res = params[2]

    memory[addr_res] = memory[addr_x] + memory[addr_y]


def __intcode_two(memory, params):
    addr_x = params[0]
    addr_y = params[1]
    addr_res = params[2]

    memory[addr_res] = memory[addr_x] * memory[addr_y]


INSTRUCTIONS = [
    {"opcode": 1, "param_count": 3, "func": __intcode_one},
    {"opcode": 2, "param_count": 3, "func": __intcode_two},
    {"opcode": 99, "param_count": 0, "func": None},
]
