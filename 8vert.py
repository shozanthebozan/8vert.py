__VERSION__ = "V2.0.0"

# You already worked this out yourself in the time section, with to_seconds() and from_seconds(). This is the same trick, written with a dict.
#
# Pick ONE base unit per category. Then every other unit only needs one number: "how many base units is 1 of me?".
# Once you have that table, any pair converts in two steps: into the base unit, then out of it.
def convert(amount, from_unit, to_unit, table):
    base = amount * table[from_unit]
    return base / table[to_unit]


# Lengths in metres. The imperial numbers are the exact definitions
DISTANCE = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.344,
}

# Weights in kilograms
WEIGHT = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1.0,
    "tonnes": 1000.0,
    "oz": 0.028349523125,
    "lb": 0.45359237,
    "stones": 6.35029318,
    "tons": 907.18474,
}

# Speeds in metres per second
SPEED = {
    "km/h": 1 / 3.6,
    "km/s": 1000.0,
    "mph": 0.44704,
    "knots": 1852 / 3600,
    "m/s": 1.0,
    "ft/s": 0.3048,
    "m": 343.0,         # mach
    "c": 299792458.0,   # speed of light
}

# Volumes in litres. These are the US liquid measures
VOLUME = {
    "ml": 0.001,
    "l": 1.0,
    "m3": 1000.0,
    "tsp": 0.00492892159375,
    "tbsp": 0.01478676478125,
    "fl_oz": 0.0295735295625,
    "cup": 0.2365882365,
    "pint": 0.473176473,
    "quart": 0.946352946,
    "gallon": 3.785411784,
}

# Areas in square metres
AREA = {
    "mm2": 0.000001,
    "cm2": 0.0001,
    "m2": 1.0,
    "km2": 1000000.0,
    "in2": 0.00064516,
    "ft2": 0.09290304,
    "yd2": 0.83612736,
    "acre": 4046.8564224,
    "hectare": 10000.0,
}

# Times in seconds. A "year" is 365.25 days, the same as your old code used.
TIME = {
    "s": 1.0,
    "min": 60.0,
    "h": 3600.0,
    "day": 86400.0,
    "week": 604800.0,
    "year": 31557600.0,
}

# Sizes in bytes. 1 bit is an eighth of a byte, so it is 0.125.
DATA = {
    "bit": 0.125,
    "byte": 1.0,
    "KiB": 1024.0,
    "MiB": 1024.0 ** 2,
    "GiB": 1024.0 ** 3,
    "TiB": 1024.0 ** 4,
}

# Temperature is the one category where a table of factors does NOT work.
# Every category above is a pure ratio: 0 of a unit is 0 of every other unit, so a single multiply is enough.
# Temperature has an offset instead - 0 C is not 0 F - so it needs a real formula.
TEMPERATURE = ("C", "F", "K")


def to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    if unit == "K":
        return value - 273.15


def from_celsius(celsius, unit):
    if unit == "C":
        return celsius
    if unit == "F":
        return celsius * 9 / 5 + 32
    if unit == "K":
        return celsius + 273.15


# What each menu number means: 
# the name to show, the units, and a hint for the ones whose names are not obvious.
# For 7 of them the units are the conversion table. Temperature only lists its names, because it uses the formulas above instead.
CATEGORIES = {
    1: ("distance/length/height", DISTANCE, ""),
    2: ("weight", WEIGHT, ""),
    3: ("speed", SPEED, "m is the mach number, c is the speed of light"),
    4: ("temp", TEMPERATURE, "uppercase"),
    5: ("volume", VOLUME, ""),
    6: ("area", AREA, "the 2 means squared, so mm2 is a square millimetre"),
    7: ("time", TIME, ""),
    8: ("data", DATA, ""),
}

# int() raises an error instead of returning something when the text is not a number, so "try" it and fall back to 0, which is not a menu option and lands on "Unknown choice".
# i rewrote to int because it's acually just integers: 1,2,3 ... , it just makes more sense
try:
    convertchoice=int(input("Enter 1 for distance/length/height, 2 for weight, 3 for speed, 4 for temp, 5 for volume, 6 for area, 7 for time or 8 for data: "))
except ValueError:
    convertchoice=0
if convertchoice not in CATEGORIES:
    print("Unknown choice")
else:
    name, units, hint = CATEGORIES[convertchoice]

    # The list of units comes straight from the table, so the prompt can never get out of step with what the code accepts.
    choices = ", ".join(units)
    if hint:
        choices = f"{choices} - {hint}"
    fromUnit=input(f"Enter 1st unit for {name}, it can be {choices}: ")
    toUnit=input("Enter 2nd unit: ")

    # The old code just fell through and printed nothing when you typed a unit it did not know, which made it look broken.
    if fromUnit not in units or toUnit not in units:
        print(f"Sorry, that is not a {name} unit. It can be: {', '.join(units)}")
    else:
        amount=input(f"Enter {fromUnit} amount: ")
        if convertchoice==4:
            answer = from_celsius(to_celsius(float(amount), fromUnit), toUnit)
        else:
            answer = convert(float(amount), fromUnit, toUnit, units)
        print(f"That is {answer} {toUnit}.")
