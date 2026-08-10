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
    speedUnit=input("Enter 1st unit in lowercase, it can be km/h, km/s, mph, knots, m/s, ft/s, m (mach number) or c (speed of light): ")
    speedConvert=input("Enter 2ndt unit in lowercase, it can be km/h, km/s, mph, knots, m/s, ft/s, m (mach number) or c (speed of light): ")
    if speedUnit=="km/h":
        if speedConvert=="km/s":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)/3600} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)*0.621371} mph.")
        elif speedConvert=="knots":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)* 0.539957} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)/3.6} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)/1.09728} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter km/h amount: ")
            print(f"That is M{float(amount)/1234.8}.")
        elif speedConvert=="c":
            amount=input("Enter km/h amount: ")
            print(f"That is {float(amount)/1079252848.8} c.")
# km/h converting done on 21/6/2026 at 11:26 AM, starting km/s from here. Need to convert to km/h, mph, knots, m/s, ft/s, m (mach number) and c (speed of light)
    if speedUnit=="km/s":
        if speedConvert=="km/h":
            amount=input("Enter km/s amount: ")
            print(f"That is {float(amount)*3600} km/h.")
        elif speedConvert=="mph":
            amount=input('Enter km/s amount: ')
            print(f"That is {float(amount)*2236.936} mph.")
        elif speedConvert=="knots":
            amount=input("Enter km/s amount: ")
            print(f"That is {float(amount)*1943.844} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter km/s amount: ")
            print(f"That is {float(amount)*1000} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter km/s amount: ")
            print(f"That is {float(amount)*3280.84} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter km/s amount: ")
            print(f"That is M{float(amount)/0.34029}.")
        elif speedConvert=="c":
            amount=input("Enter km/s amount: ")
            print(f"That is {float(amount)/299792.458} c.")
    if speedUnit=="mph":
        if speedConvert=="km/h":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)/0.621371} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)/2236.936} km/s.")
        elif speedConvert=="knots":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)*0.868976} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)/2.23694} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)*1.46667} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter mph amount: ")
            print(f"That is M{float(amount)/761.207}.")
        elif speedConvert=="c":
            amount=input("Enter mph amount: ")
            print(f"That is {float(amount)/670616629.384} c.")
    if speedUnit=="knots":
        if speedConvert=="km/h":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)/0.539957} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)/1943.844} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)/0.868976} mph.")
        elif speedConvert=="m/s":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)/1.943844} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)*1.68781} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter knots amount: ")
            print(f"That is M{float(amount)/661.47}.")
        elif speedConvert=="c":
            amount=input("Enter knots amount: ")
            print(f"That is {float(amount)/589613.0} c.")
    if speedUnit=="m/s":
        if speedConvert=="km/h":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)*3.6} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)/1000} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)*2.23694} mph.")
        elif speedConvert=="knots":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)*1.943844} knots.")
        elif speedConvert=="ft/s":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)*3.28084} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter m/s amount: ")
            print(f"That is M{float(amount)/340.29}.")
        elif speedConvert=="c":
            amount=input("Enter m/s amount: ")
            print(f"That is {float(amount)/299792458} c.")
    if speedUnit=="ft/s":
        if speedConvert=="km/h":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)*1.09728} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)/3280.84} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)/1.46667} mph.")
        elif speedConvert=="knots":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)/1.68781} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)/3.28084} m/s.")
        elif speedConvert=="m":
            amount=input("Enter ft/s amount: ")
            print(f"That is M{float(amount)/1116.47}.")
        elif speedConvert=="c":
            amount=input("Enter ft/s amount: ")
            print(f"That is {float(amount)/983571000} c.")
    if speedUnit=="m":
        if speedConvert=="km/h":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*1234.8} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*0.342} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*767.269} mph.")
        elif speedConvert=="knots":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*667.0} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*343.0} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*1125.98} ft/s.")
        elif speedConvert=="c":
            amount=input("Enter mach number amount: ")
            print(f"That is {float(amount)*0.000001144} c.")
    if speedUnit=="c":
        if speedConvert=="km/h":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*1079252848.8} km/h.")
        elif speedConvert=="km/s":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*299792.458} km/s.")
        elif speedConvert=="mph":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*670616629.384} mph.")
        elif speedConvert=="knots":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*582749977.0} knots.")
        elif speedConvert=="m/s":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*299792458} m/s.")
        elif speedConvert=="ft/s":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is {float(amount)*983571056} ft/s.")
        elif speedConvert=="m":
            amount=input("Enter light-speed fraction amount: ")
            print(f"That is M{float(amount)*8766.0}.")
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
    volUnit=input("Enter 1st unit in lowercase (ml,l,m³,tsp,tbsp,fl_oz,cup,pint,quart,gallon): ")
    volConvert=input("Enter 2nd unit in lowercase: ")
    if volUnit=="ml":
        if volConvert=="l":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/1000} l.")
        if volConvert=="m3":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/1000000} m³.")
        if volConvert=="tsp":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/4.92892} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/14.7868} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/29.5735} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/236.588} cup.")
        if volConvert=="pint":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/473.176} pint.")
        if volConvert=="quart":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/946.353} quart.")
        if volConvert=="gallon":
            amount=input("Enter ml amount: ")
            print(f"That is {float(amount)/3785.41} gallon.")
    if volUnit=="l":
        if volConvert=="ml":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)*1000} ml.")
        if volConvert=="m3":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/1000} m³.")
        if volConvert=="tsp":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.00492892} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.0147868} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.0295735} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.236588} cup.")
        if volConvert=="pint":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.473176} pint.")
        if volConvert=="quart":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/0.946353} quart.")
        if volConvert=="gallon":
            amount=input("Enter l amount: ")
            print(f"That is {float(amount)/3.78541} gallon.")
    if volUnit=="m3":
        if volConvert=="ml":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)*1000000} ml.")
        if volConvert=="l":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)*1000} l.")
        if volConvert=="tsp":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.00000492892} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.0000147868} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.0000295735} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.000236588} cup.")
        if volConvert=="pint":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.000473176} pint.")
        if volConvert=="quart":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.000946353} quart.")
        if volConvert=="gallon":
            amount=input("Enter m3 amount: ")
            print(f"That is {float(amount)/0.00378541} gallon.")
    if volUnit=="tsp":
        if volConvert=="ml":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)*4.92892} ml.")
        if volConvert=="l":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)*0.00492892} l.")
        if volConvert=="m3":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)*0.00000492892} m³.")
        if volConvert=="tbsp":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/3} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/6} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/48} cup.")
        if volConvert=="pint":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/96} pint.")
        if volConvert=="quart":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/192} quart.")
        if volConvert=="gallon":
            amount=input("Enter tsp amount: ")
            print(f"That is {float(amount)/768} gallon.")
    if volUnit=="tbsp":
        if volConvert=="ml":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)*14.7868} ml.")
        if volConvert=="l":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)*0.0147868} l.")
        if volConvert=="m3":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)*0.0000147868} m³.")
        if volConvert=="tsp":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)*3} tsp.")
        if volConvert=="fl_oz":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)/2} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)/16} cup.")
        if volConvert=="pint":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)/32} pint.")
        if volConvert=="quart":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)/64} quart.")
        if volConvert=="gallon":
            amount=input("Enter tbsp amount: ")
            print(f"That is {float(amount)/256} gallon.")
    if volUnit=="fl_oz":
        if volConvert=="ml":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)*29.5735} ml.")
        if volConvert=="l":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)*0.0295735} l.")
        if volConvert=="m3":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)*0.0000295735} m³.")
        if volConvert=="tsp":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)*6} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)*2} tbsp.")
        if volConvert=="cup":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)/8} cup.")
        if volConvert=="pint":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)/16} pint.")
        if volConvert=="quart":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)/32} quart.")
        if volConvert=="gallon":
            amount=input("Enter fl_oz amount: ")
            print(f"That is {float(amount)/128} gallon.")
    if volUnit=="cup":
        if volConvert=="ml":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*236.588} ml.")
        if volConvert=="l":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*0.236588} l.")
        if volConvert=="m3":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*0.000236588} m³.")
        if volConvert=="tsp":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*48} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*16} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)*8} fl_oz.")
        if volConvert=="pint":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)/2} pint.")
        if volConvert=="quart":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)/4} quart.")
        if volConvert=="gallon":
            amount=input("Enter cup amount: ")
            print(f"That is {float(amount)/16} gallon.")
    if volUnit=="pint":
        if volConvert=="ml":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*473.176} ml.")
        if volConvert=="l":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*0.473176} l.")
        if volConvert=="m3":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*0.000473176} m³.")
        if volConvert=="tsp":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*96} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*32} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*16} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)*2} cup.")
        if volConvert=="quart":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)/2} quart.")
        if volConvert=="gallon":
            amount=input("Enter pint amount: ")
            print(f"That is {float(amount)/8} gallon.")
    if volUnit=="quart":
        if volConvert=="ml":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*946.353} ml.")
        if volConvert=="l":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*0.946353} l.")
        if volConvert=="m3":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*0.000946353} m³.")
        if volConvert=="tsp":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*192} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*64} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*32} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*4} cup.")
        if volConvert=="pint":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)*2} pint.")
        if volConvert=="gallon":
            amount=input("Enter quart amount: ")
            print(f"That is {float(amount)/4} gallon.")
    if volUnit=="gallon":
        if volConvert=="ml":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*3785.41} ml.")
        if volConvert=="l":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*3.78541} l.")
        if volConvert=="m3":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*0.00378541} m³.")
        if volConvert=="tsp":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*768} tsp.")
        if volConvert=="tbsp":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*256} tbsp.")
        if volConvert=="fl_oz":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*128} fl_oz.")
        if volConvert=="cup":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*16} cup.")
        if volConvert=="pint":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*8} pint.")
        if volConvert=="quart":
            amount=input("Enter gallon amount: ")
            print(f"That is {float(amount)*4} quart.")
# Area conversions
elif convertchoice=="6":
    areaUnit=input("Enter 1st unit (mm²,cm²,m²,km²,in²,ft²,yd²,acre,hectare): ")
    areaConvert=input("Enter 2nd unit: ")
    if areaUnit=="mm2":
        if areaConvert=="cm2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/100} cm².")
        if areaConvert=="m2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/1000000} m².")
        if areaConvert=="km2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/1e+12} km².")
        if areaConvert=="in2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/645.16} in².")
        if areaConvert=="ft2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/92903.04} ft².")
        if areaConvert=="yd2":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/836127.36} yd².")
        if areaConvert=="acre":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/4046856422.4} acre.")
        if areaConvert=="hectare":
            amount=input("Enter mm2 amount: ")
            print(f"That is {float(amount)/10000000000} hectare.")
    if areaUnit=="cm2":
        if areaConvert=="mm2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)*100} mm².")
        if areaConvert=="m2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/10000} m².")
        if areaConvert=="km2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/1e+10} km².")
        if areaConvert=="in2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/6.4516} in².")
        if areaConvert=="ft2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/929.0304} ft².")
        if areaConvert=="yd2":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/8361.2736} yd².")
        if areaConvert=="acre":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/40468564.224} acre.")
        if areaConvert=="hectare":
            amount=input("Enter cm2 amount: ")
            print(f"That is {float(amount)/100000000} hectare.")
    if areaUnit=="m2":
        if areaConvert=="mm2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)*1000000} mm².")
        if areaConvert=="cm2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)*10000} cm².")
        if areaConvert=="km2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/1000000} km².")
        if areaConvert=="in2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/0.00064516} in².")
        if areaConvert=="ft2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/0.09290304} ft².")
        if areaConvert=="yd2":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/0.83612736} yd².")
        if areaConvert=="acre":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/4046.8564224} acre.")
        if areaConvert=="hectare":
            amount=input("Enter m2 amount: ")
            print(f"That is {float(amount)/10000} hectare.")
    if areaUnit=="km2":
        if areaConvert=="mm2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*1e+12} mm².")
        if areaConvert=="cm2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*1e+10} cm².")
        if areaConvert=="m2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*1000000} m².")
        if areaConvert=="in2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*154998400000} in².")
        if areaConvert=="ft2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*10763910.4} ft².")
        if areaConvert=="yd2":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*1195990.08} yd².")
        if areaConvert=="acre":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*247.105381} acre.")
        if areaConvert=="hectare":
            amount=input("Enter km2 amount: ")
            print(f"That is {float(amount)*100} hectare.")
    if areaUnit=="in2":
        if areaConvert=="mm2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)*645.16} mm².")
        if areaConvert=="cm2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)*6.4516} cm².")
        if areaConvert=="m2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)*0.00064516} m².")
        if areaConvert=="km2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)*6.4516e-10} km².")
        if areaConvert=="ft2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)/144} ft².")
        if areaConvert=="yd2":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)/1296} yd².")
        if areaConvert=="acre":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)/6272640} acre.")
        if areaConvert=="hectare":
            amount=input("Enter in2 amount: ")
            print(f"That is {float(amount)/15500031} hectare.")
    if areaUnit=="ft2":
        if areaConvert=="mm2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)*92903.04} mm².")
        if areaConvert=="cm2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)*929.0304} cm².")
        if areaConvert=="m2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)*0.09290304} m².")
        if areaConvert=="km2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)*9.290304e-8} km².")
        if areaConvert=="in2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)*144} in².")
        if areaConvert=="yd2":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)/9} yd².")
        if areaConvert=="acre":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)/43560} acre.")
        if areaConvert=="hectare":
            amount=input("Enter ft2 amount: ")
            print(f"That is {float(amount)/107639.104} hectare.")
    if areaUnit=="yd2":
        if areaConvert=="mm2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*836127.36} mm².")
        if areaConvert=="cm2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*8361.2736} cm².")
        if areaConvert=="m2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*0.83612736} m².")
        if areaConvert=="km2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*8.3612736e-7} km².")
        if areaConvert=="in2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*1296} in².")
        if areaConvert=="ft2":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)*9} ft².")
        if areaConvert=="acre":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)/4840} acre.")
        if areaConvert=="hectare":
            amount=input("Enter yd2 amount: ")
            print(f"That is {float(amount)/11959.9} hectare.")
    if areaUnit=="acre":
        if areaConvert=="mm2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*4046856422.4} mm².")
        if areaConvert=="cm2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*40468564.224} cm².")
        if areaConvert=="m2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*4046.8564224} m².")
        if areaConvert=="km2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)/247.105381} km².")
        if areaConvert=="in2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*6272640} in².")
        if areaConvert=="ft2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*43560} ft².")
        if areaConvert=="yd2":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*4840} yd².")
        if areaConvert=="hectare":
            amount=input("Enter acre amount: ")
            print(f"That is {float(amount)*0.4046856424} hectare.")
    if areaUnit=="hectare":
        if areaConvert=="mm2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*10000000000} mm².")
        if areaConvert=="cm2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*100000000} cm².")
        if areaConvert=="m2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*10000} m².")
        if areaConvert=="km2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)/100} km².")
        if areaConvert=="in2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*15500031} in².")
        if areaConvert=="ft2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*107639.104} ft².")
        if areaConvert=="yd2":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*11959.9} yd².")
        if areaConvert=="acre":
            amount=input("Enter hectare amount: ")
            print(f"That is {float(amount)*2.47105381} acre.")
# Time conversions
elif convertchoice=="7":
    timeUnit=input("Enter 1st unit (s,min,h,day,week,year): ")
    timeConvert=input("Enter 2nd unit: ")
    def to_seconds(v,u):
        if u=="s":
            return v
        if u=="min":
            return v*60
        if u=="h":
            return v*3600
        if u=="day":
            return v*86400
        if u=="week":
            return v*604800
        if u=="year":
            return v*31557600
    def from_seconds(s,u):
        if u=="s":
            return s
        if u=="min":
            return s/60
        if u=="h":
            return s/3600
        if u=="day":
            return s/86400
        if u=="week":
            return s/604800
        if u=="year":
            return s/31557600
    amount=input("Enter amount: ")
    secs=to_seconds(float(amount), timeUnit)
    print(f"That is {from_seconds(secs, timeConvert)} {timeConvert}.")
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

