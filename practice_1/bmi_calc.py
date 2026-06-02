weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meter): "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

match bmi:
    case _ if bmi < 18.5:
        print("Category: Underweight")
    case _ if bmi < 25:
        print("Category: Normal")
    case _ if bmi < 30:
        print("Category: Overweight")
    case _:
        print("Category: Obese")