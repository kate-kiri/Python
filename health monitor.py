print("\nHEALTH MONITORING SYSTEM\n" 
  "Where your weight , height, BMI, Temperature is valued.\n")

while True:
    name = input("Please fill your name: ")
    # print("\nWEIGHT CONVERTER\n")

    # old_weight = float(input("Enter your weight: "))
    # unit = input("Is weight in lbs or kgs): ")
    # if unit == "lbs":
    #     bmi_weight = round(old_weight / 2.205 , 2)
    #     unit = "kgs"
    #     print(f"You are {bmi_weight} {unit}.")


    # elif unit == "kgs":
    #     new_weight = round(old_weight * 2.205 , 2)
    #     unit = "lbs"
    #     print(f"You are {new_weight} {unit}.")
    #     bmi_weight = old_weight
    # else:
    #     print(f"{unit} invalid!")

    #   #Height Conversion

    # print("\nHEIGHT CONVERSION\n")

    # height = float(input("My height: "))
    # height_unit = input("Height in cm or feet(Cm / F): ")

    # if height_unit == "F":
    #     new_height = round(height * 30.48 , 2)
    #     new_unit = "Cm"
    #     print(f"You are {new_height} {new_unit}.")
    #     bmi_height = new_height / 100
    

    # elif height_unit == "Cm":
    #     new_height = round(height / 30.48 , 2)
    #     new_unit = "F"
    #     print(f"You are {new_height} {new_unit}.")
    #     bmi_height = height / 100
    # else:
    #     print(f"{height_unit} invalid!")

    #      #BMI CALCULATION

    # print("\nBMI CALCULATOR\n")

    # bmi = round((bmi_weight) / pow(bmi_height , 2) , 2)
    

    # temperature = input("My temperature is: \n" )
    # print(f"Hello {name} , your BMI is {bmi} and temperature is {temperature}\u00b0 Celsius.\n")

        ##Checking If the user is a patient
    print ("#######\nVerify Patient")
    patients = ["Mary" , "Mark" , "Kamau" , "Micah"] 
    if name == patients:
            print(f"{name} is a patient.")
    else:
            print(f"{name} is not a patient.")
    
    patients.append(name)
    patients.sort()
    print(patients)
    # if bmi < 18.5: 
    #     print("underweight")
    # elif bmi >= 18.5 and bmi < 24.9:
    #     print("Normal weight")
    # else: 
    #  print("Obese")
  
    break
    


  
