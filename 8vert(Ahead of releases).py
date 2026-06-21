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