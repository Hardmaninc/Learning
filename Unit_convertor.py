
# Define a function to convert between units
def convert(value, from_unit, to_unit):
    # Convert value to SI units if necessary
    if from_unit!= "SI":
        value = value * units[from_unit]
    # Convert to desired unit
    value = value / units[to_unit]
    # Return the converted value
    return value

# Define a dictionary of units for conversion
units = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "km": 1000,
    "mi": 1609.344,
    "ft": 0.3048,
    "yd": 0.9144,
    "NA": 1,
    "kN": 1000,
    "MN": 1000000,
    "GN": 1000000000,
    "T": 1,
    "degC": 1,
    "degF": 5/9,
    "K": 1,
    "mol": 1,
    "l": 1,
    "ml": 1/1000,
    "t": 1/1000,
    "gal": 3.78541,
    "oz": 28.3495,
    "lb": 453.6,
    "kg": 1,
    "g": 1/1000,
    "oz_t": 2834.95,
    "lb_t": 453592.37,
    "slug": 14.5939,
    "S": 1,
    "W": 1,
    "A": 1,
    "V": 1,
    "Ohm": 1,
    "S": 1,
    "Hz": 1,
    "rad": 1,
    "sr": 1
}
# Prompt the user to enter the value and units
value = float(input("Enter the value: "))
from_unit = input("Enter the original units: ")
to_unit = input("Enter the desired units: ")

# Convert the value and print the result
result = convert(value, from_unit, to_unit)
print(f"{value} {from_unit} is {result} {to_unit}.")
