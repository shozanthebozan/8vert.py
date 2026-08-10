__VERSION__ = "V1.0.1"

# You already worked this out yourself in the time section, with to_seconds() and from_seconds(). This is the same trick, written with a dict.
#
# Pick ONE base unit per category. Then every other unit only needs one number: "how many base units is 1 of me?".
# Once you have that table, any pair converts in two steps: into the base unit, then out of it.
def convert(amount, from_unit, to_unit, table):
    base = amount * table[from_unit]
    return base / table[to_unit]

convertchoice=input("Enter 1 for distance/length/height, 2 for weight, 3 for speed, 4 for temp, 5 for volume, 6 for area, 7 for time or 8 for data: ")
if convertchoice=="1":
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
    distanceUnit=input("Enter 1st unit in lowercase, it can be mm,cm,m,km,inches,feet,yards or miles: ")
    distanceConvert=input("Enter 2nd unit in lowercase, it can be mm,cm,m,km,inches,feet,yards or miles: ")
    amount=input(f"Enter {distanceUnit} amount: ")
    print(f"That is {convert(float(amount), distanceUnit, distanceConvert, DISTANCE)} {distanceConvert}.")
# Completed distance/length/height on 18/05/2026, 1:23 PM. Starting weight from here.
elif convertchoice=="2":
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
    weightUnit=input("Enter 1st unit in lowercase, it can be mg, g, kg, tonnes, oz, lb, stones or tons: ")
    weightConvert=input("Enter 2nd unit in lowercase, it can be mg, g, kg, tonnes, oz, lb, stones or tons: ")
    amount=input(f"Enter {weightUnit} amount: ")
    print(f"That is {convert(float(amount), weightUnit, weightConvert, WEIGHT)} {weightConvert}.")
# Weight has been completed, on 4:00 6/6/2026 on a saturday. Starting speed from here.
elif convertchoice=="3":
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
    speedUnit=input("Enter 1st unit in lowercase, it can be km/h, km/s, mph, knots, m/s, ft/s, m (mach number) or c (speed of light): ")
    speedConvert=input("Enter 2nd unit in lowercase, it can be km/h, km/s, mph, knots, m/s, ft/s, m (mach number) or c (speed of light): ")
    amount=input(f"Enter {speedUnit} amount: ")
    print(f"That is {convert(float(amount), speedUnit, speedConvert, SPEED)} {speedConvert}.")
# Completed speed conversions. Starting temperature.
elif convertchoice=="4":
    tempUnit=input("Enter 1st unit in uppercase (C, F, K): ")
    tempConvert=input("Enter 2nd unit in uppercase (C, F, K): ")
    if tempUnit==tempConvert:
        amount=input("Enter amount: ")
        print(f"That is {float(amount)} {tempConvert}.")
    if tempUnit=="C":
        if tempConvert=="F":
            amount=input("Enter C amount: ")
            print(f"That is {float(amount)*9/5+32} F.")
        if tempConvert=="K":
            amount=input("Enter C amount: ")
            print(f"That is {float(amount)+273.15} K.")
    if tempUnit=="F":
        if tempConvert=="C":
            amount=input("Enter F amount: ")
            print(f"That is {(float(amount)-32)*5/9} C.")
        if tempConvert=="K":
            amount=input("Enter F amount: ")
            print(f"That is {(float(amount)-32)*5/9+273.15} K.")
    if tempUnit=="K":
        if tempConvert=="C":
            amount=input("Enter K amount: ")
            print(f"That is {float(amount)-273.15} C.")
        if tempConvert=="F":
            amount=input("Enter K amount: ")
            print(f"That is {(float(amount)-273.15)*9/5+32} F.")
# Starting volume conversions
elif convertchoice=="5":
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
    volUnit=input("Enter 1st unit in lowercase (ml,l,m3,tsp,tbsp,fl_oz,cup,pint,quart,gallon): ")
    volConvert=input("Enter 2nd unit in lowercase: ")
    amount=input(f"Enter {volUnit} amount: ")
    print(f"That is {convert(float(amount), volUnit, volConvert, VOLUME)} {volConvert}.")
# Area conversions
elif convertchoice=="6":
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
    areaUnit=input("Enter 1st unit (mm2,cm2,m2,km2,in2,ft2,yd2,acre,hectare): ")
    areaConvert=input("Enter 2nd unit: ")
    amount=input(f"Enter {areaUnit} amount: ")
    print(f"That is {convert(float(amount), areaUnit, areaConvert, AREA)} {areaConvert}.")
# Time conversions
elif convertchoice=="7":
    # Times in seconds. A "year" is 365.25 days, the same as your old code used.
    TIME = {
        "s": 1.0,
        "min": 60.0,
        "h": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
        "year": 31557600.0,
    }
    timeUnit=input("Enter 1st unit (s,min,h,day,week,year): ")
    timeConvert=input("Enter 2nd unit: ")
    amount=input(f"Enter {timeUnit} amount: ")
    print(f"That is {convert(float(amount), timeUnit, timeConvert, TIME)} {timeConvert}.")
# Data conversions
elif convertchoice=="8":
    # Sizes in bytes. 1 bit is an eighth of a byte, so it is 0.125.
    DATA = {
        "bit": 0.125,
        "byte": 1.0,
        "KiB": 1024.0,
        "MiB": 1024.0 ** 2,
        "GiB": 1024.0 ** 3,
        "TiB": 1024.0 ** 4,
    }
    dataUnit=input("Enter 1st unit (bit,byte,KiB,MiB,GiB,TiB): ")
    dataConvert=input("Enter 2nd unit: ")
    amount=input(f"Enter {dataUnit} amount: ")
    print(f"That is {convert(float(amount), dataUnit, dataConvert, DATA)} {dataConvert}.")
else:
    print("Unknown choice")

