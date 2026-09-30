print("\nHEALTH MONITORING SYSTEM\n" 
  "Where your weight , height, BMI, Temperature are valued.")

while True:
    name = input("Please fill your name: ")
    old_weight = float(input("Enter your weight: "))
    unit = input("Is weight in lbs or kgs): ")
    if unit == "lbs":
        bmi_weight = round(old_weight / 2.205 , 2)
        unit = "kgs"
        print(f"You are {bmi_weight} {unit}.")


    elif unit == "kgs":
        new_weight = round(old_weight * 2.205 , 2)
        unit = "lbs"
        print(f"You are {new_weight} {unit}.")
        bmi_weight = old_weight
    else:
        print(f"{unit} invalid!")

      #Height Conversion

    height = float(input("My height: "))
    height_unit = input("Height in cm or feet(Cm / F): ")

    if height_unit == "F":
        new_height = round(height * 30.48 , 2)
        new_unit = "Cm"
        print(f"You are {new_height} {new_unit}.")
        bmi_height = new_height / 100
    

    elif height_unit == "Cm":
        new_height = round(height / 30.48 , 2)
        new_unit = "F"
        print(f"You are {new_height} {new_unit}.")
        bmi_height = height / 100
    else:
        print(f"{height_unit} invalid!")

         #BMI CALCULATION

    bmi = round((bmi_weight) / pow(bmi_height , 2) , 2)
    

    temperature = input("My temperature is: " )
    print(f"Hello {name} , your BMI is {bmi} and temperature is {temperature}\u00b0 Celsius.")       
  
    break
    


  
