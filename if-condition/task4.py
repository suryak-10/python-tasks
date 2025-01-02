# BMI Calculator


# 1. Ask the user to input their weight (kg) and height (m).
# 2. Calculate the BMI using the formula: BMI = weight / (height * height).
# 3. Classify the BMI:
#    - Below 18.5: Underweight
#    - 18.5 to 24.9: Normal weight
#    - 25.0 to 29.9: Overweight
#    - 30.0 and above: Obese

weight = int(input("weight:"))
height = float(input("height:"))
try:
    bmi = weight / (height * height)
except ZeroDivisionError:
    print("cannot be divided by zero.")
if bmi < 18.5:
    print("Underweight")
elif  bmi >=18.5 and bmi<24.9:
    print("Normal")
elif bmi >= 25.0 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")