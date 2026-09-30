weight = float(input("Enter your weight: "))
unit = input("Is weight in lbs or kgs): ")
if unit == "lbs":
    new_weight = round(weight / 2.205 , 2)
    unit = "kgs"
    print(f"You are {new_weight} {unit}.")

elif unit == "kgs":
    new_weight = round(weight * 2.205 , 2)
    unit = "lbs"
    print(f"You are {new_weight} {unit}.")
else:
    print(f"{unit} invalid!")

  
