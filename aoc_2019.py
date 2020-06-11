
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