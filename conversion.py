start_up = input('What do you want to do: options available \n 1. distance \n 2. liquid \n 3. weight ')

enterNumbers = 'Please enter numbers only'

#this is the function for distance
def def_for_distance():
    distance = input('Convert anything to Meters:  ')

    #converting everything
    if distance == 'km' or distance == 'kilometer' or distance == 'kilometers':
        #convert kilometer
        print(enterNumbers)
        
        km = input('Convert CM to Meters: ')
        
        if km.isnumeric():
            save_km = int(km)
            print(save_km / 1000)
        else:
            def_for_distance()
    elif distance == 'cm' or distance == 'centimeters' or distance == 'centimeter':
        #convert cm
        print(enterNumbers)

        cm = input('Convert CM to Meters: ')

        if cm.isnumeric():
            save_cm = int(cm)
            print()
        else:
            def_for_distance()
    elif distance == 'inch' or distance == 'inches' or distance == 'in':
        #convert inch
        print(enterNumbers)

        inch = input('Convert inches to Meters: ')

        if inch.isnumeric():
            save_inch = int(inch)
            print(save_inch/ 39.37)
        else:
            def_for_distance()
    elif distance == 'foot' or distance == 'feet' or distance == 'ft':
        #convert feet
        print(enterNumbers)

        feet = input('Convert feet to Meters: ')

        if feet.isnumeric():
            save_feet = int(feet)
            print(save_feet / 3.281)
        else:
            def_for_distance()
    elif distance == 'yard' or distance == 'yards':
        #convert yards
        print(enterNumbers)

        yards = input('Convert yards to Meters: ')

        if yards.isnumeric():
            if yards.isnumeric():
                save_yards = int(yards)
                print(yards / 1.094)
            else:
                def_for_distance()
    elif distance == 'mm' or distance == 'milimeter' or distance == 'milimeters':
        #convert milimeters
        print(enterNumbers)

        mm = input('Convert MM to Meters: ')

        if mm.isnumeric():
            save_mm = int(mm)
            print(mm / 1000)  
        else:
            def_for_distance() 
    elif distance == 'mile' or distance == 'miles' or distance == 'mi':
        #convert miles
        print(enterNumbers)

        mi = input('Convert miles to Meters: ')

        if mi.isnumeric():
            save_mi = int(mi)
            print(save_mi * 1609)
        else:
            def_for_distance()
    elif distance == 'nanometer' or distance == 'nanometers' or distance == 'nm':
        #convert nanometers
        print (enterNumbers)

        nm = input('Convert nanometers to meters')

        if nm.isnumeric():
            save_nm = int(nm)
            print(save_nm / 1,000,000,000)
        else:
            def_for_distance()
    else: 
        #this will print if the user did not type a word correctly
        print('Please restart the program')

#define def for weights 
def def_for_weight():
    weight = input('Convert anything to grams: ')

    if weight == 'kilograms' or weight == 'kg' or weight == 'kilogram':
        #convert kilograms
        print(enterNumbers)

        kg = input('Convert KG to grams: ')

        if kg.isnumeric():
            save_kg = int(kg)
            print(save_kg * 1000)
        else:
            def_for_weight()
    elif weight == 'miligram' or weight == 'mg' or weight == 'miligrams':
        #convert miligram
        print(enterNumbers)

        mg = input('Conver MG to Grams: ')

        if mg.isnumeric():
            save_mg = int(mg)
            print(mg / 1000)
        else:
            def_for_weight()
    elif weight == 'microgram' or weight == 'micrograms' or weight == 'mcg':
        #convert microgram
        print(enterNumbers)

        mcg = input('Convert MCG to Grams: ')

        if mcg.isnumeric():
            save_mcg = int(mcg)
            print(save_mcg / 1,000,000)
        else:
            def_for_weight()
    elif weight == 'ton' or weight == 'tons' or weight == 'tonne' or weight == 'tonnes':
        #converting tonnes
        print(enterNumbers)

        tonne = input('Convert Tonnes to Grams: ')
        if tonne.isnumeric():
            tonne_save = int(tonne)
            print(tonne_save / 1000000)
        else:
            def_for_weight()
    elif weight == 'pounds' or weight == 'pound' or weight == 'lbs':
        #converting pounds
        print(enterNumbers)

        pounds = input('Convert Pounds to Grams')

        if pounds.isnumeric():
            save_pounds = int(pounds)
            print(save_pounds * 454)
        else:
            def_for_weight()
    elif weight == 'ounces' or weight == 'ounce':
        #coverting ounces
        print(enterNumbers)

        ounce = input('Convert Onces to Grams: ')
        if ounce.isnumeric():
            save_ounce = int(ounce)
            print(save_ounce * 28.35)
        else:
            def_for_weight()
    elif weight == 'stone' or weight == 'st':
        #converting stone 
        print(enterNumbers)

        stone = input('Convert Stone to Grams: ')

        if stone.isnumeric():
            save_stone = int(stone)
            print(save_stone * 6350)
        else:
            def_for_weight()
    else:
        #this will print if the user did not type a word correctly
        print('Please restart the program')

#define def for _liquid
def def_for_liquid():
    liquid = input('Convert anything to Liters: ')

    if liquid == 'fluid ounce':
        #convert fluid ounce
        print(enterNumbers)

        fluid_ounce = input('Convert Fluid Ounce to Liters: ')

        if fluid_ounce.isnumeric():
            save_fluid_ounce = int(fluid_ounce)
            print(save_fluid_ounce * 3.785)
        else:
            def_for_liquid()
    elif liquid == 'ml' or liquid == 'mililiter' or liquid == 'mililiters':
        #convert mililiters
        print(enterNumbers)

        ml = input('Convert ML to Liters: ')

        if ml.isnumeric():
            save_ml = int(ml)
            print(ml / 1000)
        else:
            def_for_liquid()
    elif liquid == 'cubic meter' or liquid == 'cubic meters':
        #convert cubic meter
        print(enterNumbers)

        cubic_meter = input('Convert Cubic Meters to Liters: ')

        if cubic_meter.isnumeric():
            save_cubic_meter = int(cubic_meter)
            print(save_cubic_meter * 1000)
        else:
            def_for_liquid()
    elif liquid == 'gallon' or liquid == 'gallons':
        #convert gallons
        print(enterNumbers)

        gallon = input('Convert Gallons to Liters: ')

        if gallon.isnumeric():
            save_gallon = int(gallon)
            print(gallon * 3.785)
        else:
            def_for_liquid()
    elif liquid == 'cubic inch' or liquid == 'cubic inches':
        #convert cubic inch 
        print(enterNumbers)

        cubic_inch = input('Convert Cubic Inch to Liters: ')

        if cubic_inch.isnumeric():
            save_cubic_inch = int(cubic_inch)
            print(save_cubic_inch / 61.024)
        else:
            def_for_liquid()
    elif liquid == 'cubic feet' or liquid == 'cubic foot':
        #convert cubic feet 
        print(enterNumbers)

        cubic_feet = input('Convert Cubic Feet to Liters: ')

        if cubic_feet.isnumeric():
            save_cubic_feet = int(cubic_feet)
            print(cubic_feet / 28.317)
        else:
            def_for_liquid()

if start_up == 'distance' or start_up == '1':
    #posting to the function below
    def_for_distance()
elif start_up == 'weight' or start_up == '2':
    def_for_weight()
elif start_up == 'liquid' or start_up == '3':
    def_for_liquid()
