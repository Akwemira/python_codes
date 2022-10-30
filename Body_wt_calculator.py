weight_in_pounds = float(input("What is your weight in pounds?:\n\n"))
weight_in_kilograms = float(weight_in_pounds / 2.205)
conversion = weight_in_kilograms.__round__(3)
print(f"Your body weight is: {weight_in_pounds} lbs, and the equivalent in kgs is: {conversion} kg. Thank you!")
