print("Welcome to a general BMI Calculator")
height = float(input("Enter the height in meters: "))
weight = float(input("Enter the weight in kg: "))

BMI = weight / (height) ** 2

print("Your Body Mass Index is", BMI)

if BMI <= 18.5:
    print("You are underweight.")
elif BMI <= 24.9 and BMI > 18.5:
    print("You are healthy.")
elif BMI <= 29.9 and BMI > 24.9:
    print("You are over weight.")
else:
    print("Seesh! You are obese.")
