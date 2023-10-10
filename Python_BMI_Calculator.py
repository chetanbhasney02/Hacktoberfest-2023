def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print("Welcome to the BMI Calculator!")

    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
        
        if weight_kg <= 0 or height_m <= 0:
            print("Invalid input. Weight and height must be positive numbers.")
        else:
            bmi = calculate_bmi(weight_kg, height_m)
            bmi_category = interpret_bmi(bmi)
            
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {bmi_category}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for weight and height.")
