import re


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


def intcode_program(memory, noun, verb):
    if noun:
        memory[1] = noun

    if verb:
        memory[2] = verb

    output = intcode_program_internal(memory)[0]
    return output


def intcode_program_internal(memory):
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

PATH_PATTERN = re.compile(r"^(?P<direction>[URDL])(?P<step>\d+)$")


def convert_path_string(path):
    match = PATH_PATTERN.match(path)
    if not match:
        return None

    direction = match.group("direction")
    step = match.group("step")

    return (direction, int(step))


def convert_path_to_wire(paths):
    wire = []
    cur_x, cur_y = (0, 0)

    path_to_wire = {
        "U": lambda cur_x, cur_y, step: [
            (cur_x, i) for i in range(cur_y + 1, cur_y + 1 + step)
        ],
        "R": lambda cur_x, cur_y, step: [
            (i, cur_y) for i in range(cur_x + 1, cur_x + 1 + step)
        ],
        "D": lambda cur_x, cur_y, step: [
            (cur_x, i) for i in range(cur_y - 1, cur_y - 1 - step, -1)
        ],
        "L": lambda cur_x, cur_y, step: [
            (i, cur_y) for i in range(cur_x - 1, cur_x - 1 - step, -1)
        ],
    }

    wire.append((cur_x, cur_y))
    for path in paths:
        direction = path[0]
        step = path[1]

        wire.extend(path_to_wire[direction](cur_x, cur_y, step))
        cur_x, cur_y = wire[-1]

    return wire


def find_wire_intersections(wire1, wire2):
    intersections = set(wire1).intersection(wire2)
    intersections.remove((0, 0))
    return intersections


def find_wires(path_strings):
    path1_string = path_strings[0]
    path2_string = path_strings[1]

    paths1 = [convert_path_string(x) for x in path1_string.split(",")]
    paths2 = [convert_path_string(x) for x in path2_string.split(",")]

    wire1 = convert_path_to_wire(paths1)
    wire2 = convert_path_to_wire(paths2)

    return wire1, wire2


def find_wires_cross_locations(path_strings):
    wire1, wire2 = find_wires(path_strings)
    return find_wire_intersections(wire1, wire2), wire1, wire2


def calculate_intersection_manhattan_distance(path_strings):
    intersections, _, _ = find_wires_cross_locations(path_strings)
    return min(abs(x[0]) + abs(x[1]) for x in intersections)


def calculate_intersection_fewest_combined_step(path_strings):
    intersections, wire1, wire2 = find_wires_cross_locations(path_strings)
    return min(wire1.index(x) + wire2.index(x) for x in intersections)
