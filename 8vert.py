__VERSION__ = "V1.0.1"
convertchoice=input("Enter 1 for distance/length/height, 2 for weight, 3 for speed, 4 for temp, 5 for volume, 6 for area, 7 for time or 8 for data: ")
if convertchoice=="1":
    distanceUnit=input("Enter 1st unit in lowercase, it can be mm,cm,m,km,inches,feet,yards or miles: ")
    distanceConvert=input("Enter 2nd unit in lowercase, it can be mm,cm,m,km,inches,feet,yards or miles: ")
    if distanceUnit=="mm":
       if distanceConvert=="cm":
          amount=input("Enter mm amount: ")
          print(f"That is {float(amount)/10} cm.")
    if distanceUnit=="cm":
       if distanceConvert=="mm":
          amount=input("Enter cm amount: ")
          print(f"That is {float(amount)*10} mm.")
  
    if distanceUnit=="mm":
       if distanceConvert=="m":
             amount=input("Enter mm amount: ")
             print(f"That is {float(amount)/1000} m.")
    if distanceUnit=="mm":
       if distanceConvert=="km":
           amount=input("Enter mm amount: ")
           print(f"That is {float(amount)/1000000} km.")
    
    if distanceUnit=="mm":
       if distanceConvert=="inches":
           amount=input("Enter mm amount: ")
           print(f"That is {float(amount)/25.4} inches.")
    if distanceUnit=="mm":
        if distanceConvert=="feet":
            amount=input("Enter mm amount: ")
            print(f"That is {float(amount)/304.8} feet.")
    if distanceUnit=="mm":
        if distanceConvert=="yards":
            amount=input("Enter mm amount: ")
            print(f"That is {float(amount)/914.4} yards.")
    if distanceUnit=="mm":
        if distanceConvert=="miles":
            amount=input("Enter mm amount: ")
            print(f"That is {float(amount)/1609344} miles.")
    if distanceUnit=="cm":
        if distanceConvert=="m":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/100} m.")
    if distanceUnit=="cm":
        if distanceConvert=="km":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/100000} km.")
    if distanceUnit=="cm":
        if distanceConvert=="inches":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/2.54} inches.")
    if distanceUnit=="cm":
        if distanceConvert=="feet":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/30.48} feet.")
    if distanceUnit=="cm":
        if distanceConvert=="yards":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/91.44} yards.")
    if distanceUnit=="cm":
        if distanceConvert=="miles":
            amount=input("Enter cm amount: ")
            print(f"That is {float(amount)/160934.4} miles.")
    if distanceUnit=="m":
        if distanceConvert=="mm":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)*1000} mm.")   
    if distanceUnit=="m":
        if distanceConvert=="cm":
            amount=input("Enter m amount: ")   
            print(f"That is {float(amount)*100} cm.")     
    if distanceUnit=="m":
        if distanceConvert=="km":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)/1000} km.") 
    if distanceUnit=="m":
        if distanceConvert=="inches":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)*39.3701} inches.")
    if distanceUnit=="m":
        if distanceConvert=="feet":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)*3.28084} feet.")
    if distanceUnit=="m":
        if distanceConvert=="yards":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)*1.09361} yards.")
    if distanceUnit=="m":
        if distanceConvert=="miles":
            amount=input("Enter m amount: ")
            print(f"That is {float(amount)/1609.34} miles.")
    if distanceUnit=="km":
        if distanceConvert=="mm":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)*1000000} mm.")
    if distanceUnit=="km":
        if distanceConvert=="cm":
              amount=input("Enter km amount: ")
              print(f"That is {float(amount)*100000} cm.")
    if distanceUnit=="km":
        if distanceConvert=="m":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)*1000} m.")
    if distanceUnit=="km":
        if distanceConvert=="inches":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)*39370.1} inches.")
    if distanceUnit=="km":
        if distanceConvert=="feet":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)*3280.84} feet.")
    if distanceUnit=="km":
        if distanceConvert=="yards":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)*1093.61} yards.")
    if distanceUnit=="km":
        if distanceConvert=="miles":
            amount=input("Enter km amount: ")
            print(f"That is {float(amount)/1.60934} miles.")
    if distanceUnit=="inches":
        if distanceConvert=="mm":
            amount=input("Enter inches amount: ")
            print(f"That is {float(amount)*25.4} mm.")
    if distanceUnit=="inches":
        if distanceConvert=="cm":
            amount=input("Enter inches amount: ")
            print(f"That is {float(amount)*2.54} cm.")
    if distanceUnit=="inches":
         if distanceConvert=="m":
              amount=input("Enter inches amount:")
              print(f"That is {float(amount)/39.3701} m.")
    if distanceUnit=="inches":
        if distanceConvert=="km":
            amount=input("Enter inches amount: ")
            print(f"That is {float(amount)/39370.1} km.")
    if distanceUnit=="inches":
        if distanceConvert=="feet":
            amount=input("Enter inches amount: ")
            print(f"That is {float(amount)/12} feet.")
    if distanceUnit=="inches":
        if distanceConvert=="yards":
            amount=input("Enter inches amount: ")
            print(f"That is {float(amount)/36} yards.")
    if distanceUnit=="inches":
        if distanceConvert=="miles":
            amount=input("Enter inches amount: ")
            print(f"THat is {float(amount)/63360} miles.") 
# use  mm,cm,m,km,inches,feet,yards or miles
    if distanceUnit=="feet":
        if distanceConvert=="mm":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)*304.8} mm.")
    if distanceUnit=="feet":
        if distanceConvert=="cm":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)*30.48} cm.")
    if distanceUnit=="feet":
        if distanceConvert=="m":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)*0.3048} m.") 
    if distanceUnit=="feet":
        if distanceConvert=="km":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)*0.0003048} km.") 
    if distanceUnit=="feet":
        if distanceConvert=="inches":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)*12} inches.") 
    if distanceUnit=="feet":
        if distanceConvert=="yards":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)/3} yards.")
# use  mm,cm,m,km,inches,feet,yards or miles
    if distanceUnit=="feet":
        if distanceConvert=="miles":
            amount=input("Enter feet amount: ")
            print(f"That is {float(amount)/5280} miles.") 
# Up to converting yards, do mm,cm,m,km,inches,feet,yards or miles
    if distanceUnit=="yards":
        if distanceConvert=="mm":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)*914.4} mm.")
    if distanceUnit=="yards":
        if distanceConvert=="cm":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)*91.44} cm.") 
    if distanceUnit=="yards":
        if distanceConvert=="m":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)*0.9144} m.") 
    if distanceUnit=="yards":
        if distanceConvert=="km":
            amount=input("Enter yards amount: ")
            print(f"THat is {float(amount)*0.0009144} km.") 
# Up to converting yards, do mm,cm,m,km,inches,feet,yards or miles
    if distanceUnit=="yards":
        if distanceConvert=="inches":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)*36} inches.")
    if distanceUnit=="yards":
        if distanceConvert=="feet":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)*3} feet.")
    if distanceUnit=="yards":
        if distanceConvert=="miles":
            amount=input("Enter yards amount: ")
            print(f"That is {float(amount)/1760} miles.") 
# Started miles here, on 18/05/2026, last of distance/length/height    
#  Up to converting miles, do mm,cm,m,km,inches,feet,yards or miles 
    if distanceUnit=="miles":
        if distanceConvert=="mm":
            amount=input("Enter miles amount: ") 
            print(f"That is {float(amount)*1609344} mm.")
    if distanceUnit=="miles":
        if distanceConvert=="cm": 
            amount=input("Enter miles amount: ")
            print(f"That is {float(amount)*160934.4} cm.")
    if distanceUnit=="miles":
        if distanceConvert=="m":
            amount=input("Enter miles amount: ")
            print(f"That is {float(amount)*1609.344} m.")  
    if distanceUnit=="miles":
        if distanceConvert=="km":
            amount=input("Enter miles amount: ")
            print(f"That is {float(amount)*1.609344} km.") 
    if distanceUnit=="miles":
        if distanceConvert=="inches":
            amount=input("Enter miles amount: ")
            print(f"That is {float(amount)*63360} inches.") 
    if distanceUnit=="miles":
        if distanceConvert=="feet":
            amount=input("Enter miles amount: ")
            print(f"That is {float(amount)*5280} feet.") 
    if distanceUnit=="miles":
        if distanceConvert=="yards":
            amount=input("Enter miles amount: ") 
            print(f"That is {float(amount)*1760} yards.")
# Completed distance/length/height on 18/05/2026, 1:23 PM. Starting weight from here.
elif convertchoice=="2":
    weightUnit=input("Enter 1st unit in lowercase, it can be mg, g, kg, tonnes, oz, lb, stones or tons: ") 
    weightConvert=input("Enter 2nd unit in lowercase, it can be mg, g, kg, tonnes, oz, lb, stones or tons: ") 
    if weightUnit=="mg":
        if weightConvert=="g":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/1000} g.")
        elif weightConvert=="kg":
            amount=input("Enter mg amount: ") 
            print(f"That is {float(amount)/1000000} kg.")
        elif weightConvert=="tonnes":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/1000000000} tonnes.")
        elif weightConvert=="oz":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/28349.5} oz.")
        elif weightConvert=="lb":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/453592} lb.") 
        elif weightConvert=="stones":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/6350293} stones.")
        elif weightConvert=="tons":
            amount=input("Enter mg amount: ")
            print(f"That is {float(amount)/907185000} tons.")
    if weightUnit=="g":
        if weightConvert=="mg":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)*1000} mg.")  
        elif weightConvert=="kg":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)/1000} kg.")
        elif weightConvert=="tonnes":  
            amount=input("Enter g amount: ")   
            print(f"That is {float(amount)/1000000} tonnes.")   
        elif weightConvert=="oz":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)/28.3495} oz.")
        elif weightConvert=="lb":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)/453.592} lb.")
        elif weightConvert=="stones":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)/6350.293} stones.")
        elif weightConvert=="tons":
            amount=input("Enter g amount: ")
            print(f"That is {float(amount)/907185} tons.")  
# starting kg here, on 18/05/2026, 4:38 PM. Up to converting kg, do mg, g, tonnes, oz, lb, stones and tons
    if weightUnit=="kg":
        if weightConvert=="mg":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)*1000000} mg.")
        elif weightConvert=="g":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)*1000} g.")
        elif weightConvert=="tonnes":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)/1000} tonnes.")
        elif weightConvert=="oz":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)*35.274} oz.")
        elif weightConvert=="lb":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)*2.20462} lb.")
        elif weightConvert=="stones":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)*0.157473} stones.")
        elif weightConvert=="tons":
            amount=input("Enter kg amount: ")
            print(f"That is {float(amount)/907.185} tons.")
    if weightUnit=="tonnes":
        if weightConvert=="mg":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*1000000000} mg.")
        elif weightConvert=="g":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*1000000} g.")
        elif weightConvert=="kg":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*1000} kg.")
        elif weightConvert=="oz":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*35274} oz.")
        elif weightConvert=="lb":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*2204.62} lb.")
        elif weightConvert=="stones":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)*157.473} stones.")
        elif weightConvert=="tons":
            amount=input("Enter tonnes amount: ")
            print(f"That is {float(amount)/0.907185} tons.")
    if weightUnit=="oz":
        if weightConvert=="mg":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)*28349.5} mg.")
        elif weightConvert=="g":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)*28.3495} g.")
        elif weightConvert=="kg":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)/35.274} kg.")
        elif weightConvert=="tonnes":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)/35274} tonnes.")
        elif weightConvert=="lb":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)/16} lb.")
        elif weightConvert=="stones":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)/224} stones.")
        elif weightConvert=="tons":
            amount=input("Enter oz amount: ")
            print(f"That is {float(amount)/32000} tons.")
    if weightUnit=="lb":
        if weightConvert=="mg":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)*453592} mg.")
        elif weightConvert=="g":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)*453.592} g.")
        elif weightConvert=="kg":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)/2.20462} kg.")
        elif weightConvert=="tonnes":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)/2204.62} tonnes.")
        elif weightConvert=="oz":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)*16} oz.")
        elif weightConvert=="stones":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)/14} stones.")
        elif weightConvert=="tons":
            amount=input("Enter lb amount: ")
            print(f"That is {float(amount)/2000} tons.")
# up to converting stones, have to convert to mg, g, kg, tonnes, oz, lb,tons
    if weightUnit=="stones":
       if weightConvert=="mg":
          amount=input("Enter stones amount :")
          print(f"That is {float(amount)*6350293.18} mg.")
       elif weightConvert=="g":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*6350.29318} g.")
       elif weightConvert=="kg":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*6.35029318} kg.")
       elif weightConvert=="tonnes":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*0.00635029} tonnes.")
       elif weightConvert=="oz":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*224} oz.")
       elif weightConvert=="lb":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*14} lb.")
       elif weightConvert=="tons":
          amount=input("Enter stones amount: ")
          print(f"That is {float(amount)*0.007} tons.")
# up to converting tons, last of weight, have to convert to mg, g, kg, tonnes, oz, lb, stones
    if weightUnit=="tons":
        if weightConvert=="mg":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*907184740} mg.")
        elif weightConvert=="g":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*907184.74} g.")
        elif weightConvert=="kg":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*907.18474} kg.")
        elif weightConvert=="tonnes":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*0.90718474} tonnes.")
        elif weightConvert=="oz":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*32000} oz.")
        elif weightConvert=="lb":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*2000} lb.")
        elif weightConvert=="stones":
           amount=input("Enter tons amount: ")
           print(f"That is {float(amount)*142.857143} stones.")
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
            print(f"That is {float(amount)*3280.84} ft/s.")
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
    dataUnit=input("Enter 1st unit (bit,byte,KiB,MiB,GiB,TiB): ")
    dataConvert=input("Enter 2nd unit: ")
    if dataUnit=="bit":
        if dataConvert=="byte":
            amount=input("Enter bit amount: ")
            print(f"That is {float(amount)/8} byte.")
        if dataConvert=="KiB":
            amount=input("Enter bit amount: ")
            print(f"That is {float(amount)/(8*1024)} KiB.")
        if dataConvert=="MiB":
            amount=input("Enter bit amount: ")
            print(f"That is {float(amount)/(8*1024**2)} MiB.")
        if dataConvert=="GiB":
            amount=input("Enter bit amount: ")
            print(f"That is {float(amount)/(8*1024**3)} GiB.")
        if dataConvert=="TiB":
            amount=input("Enter bit amount: ")
            print(f"That is {float(amount)/(8*1024**4)} TiB.")
    if dataUnit=="byte":
        if dataConvert=="bit":
            amount=input("Enter byte amount: ")
            print(f"That is {float(amount)*8} bit.")
        if dataConvert=="KiB":
            amount=input("Enter byte amount: ")
            print(f"That is {float(amount)/1024} KiB.")
        if dataConvert=="MiB":
            amount=input("Enter byte amount: ")
            print(f"That is {float(amount)/1024**2} MiB.")
        if dataConvert=="GiB":
            amount=input("Enter byte amount: ")
            print(f"That is {float(amount)/1024**3} GiB.")
        if dataConvert=="TiB":
            amount=input("Enter byte amount: ")
            print(f"That is {float(amount)/1024**4} TiB.")
    if dataUnit=="KiB":
        if dataConvert=="bit":
            amount=input("Enter KiB amount: ")
            print(f"That is {float(amount)*1024*8} bit.")
        if dataConvert=="byte":
            amount=input("Enter KiB amount: ")
            print(f"That is {float(amount)*1024} byte.")
        if dataConvert=="MiB":
            amount=input("Enter KiB amount: ")
            print(f"That is {float(amount)/1024} MiB.")
        if dataConvert=="GiB":
            amount=input("Enter KiB amount: ")
            print(f"That is {float(amount)/1024**2} GiB.")
        if dataConvert=="TiB":
            amount=input("Enter KiB amount: ")
            print(f"That is {float(amount)/1024**3} TiB.")
    if dataUnit=="MiB":
        if dataConvert=="bit":
            amount=input("Enter MiB amount: ")
            print(f"That is {float(amount)*1024**2*8} bit.")
        if dataConvert=="byte":
            amount=input("Enter MiB amount: ")
            print(f"That is {float(amount)*1024**2} byte.")
        if dataConvert=="KiB":
            amount=input("Enter MiB amount: ")
            print(f"That is {float(amount)*1024} KiB.")
        if dataConvert=="GiB":
            amount=input("Enter MiB amount: ")
            print(f"That is {float(amount)/1024} GiB.")
        if dataConvert=="TiB":
            amount=input("Enter MiB amount: ")
            print(f"That is {float(amount)/1024**2} TiB.")
    if dataUnit=="GiB":
        if dataConvert=="bit":
            amount=input("Enter GiB amount: ")
            print(f"That is {float(amount)*1024**3*8} bit.")
        if dataConvert=="byte":
            amount=input("Enter GiB amount: ")
            print(f"That is {float(amount)*1024**3} byte.")
        if dataConvert=="KiB":
            amount=input("Enter GiB amount: ")
            print(f"That is {float(amount)*1024**2} KiB.")
        if dataConvert=="MiB":
            amount=input("Enter GiB amount: ")
            print(f"That is {float(amount)*1024} MiB.")
        if dataConvert=="TiB":
            amount=input("Enter GiB amount: ")
            print(f"That is {float(amount)/1024} TiB.")
    if dataUnit=="TiB":
        if dataConvert=="bit":
            amount=input("Enter TiB amount: ")
            print(f"That is {float(amount)*1024**4*8} bit.")
        if dataConvert=="byte":
            amount=input("Enter TiB amount: ")
            print(f"That is {float(amount)*1024**4} byte.")
        if dataConvert=="KiB":
            amount=input("Enter TiB amount: ")
            print(f"That is {float(amount)*1024**3} KiB.")
        if dataConvert=="MiB":
            amount=input("Enter TiB amount: ")
            print(f"That is {float(amount)*1024**2} MiB.")
        if dataConvert=="GiB":
            amount=input("Enter TiB amount: ")
            print(f"That is {float(amount)*1024} GiB.")
else:
    print("Unknown choice")

