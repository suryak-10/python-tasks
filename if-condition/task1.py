# Temperature Converter

# 1. Ask the user to input a temperature in Celsius.
# 2. If the temperature is below 0, classify it as "Freezing."
# 3. If the temperature is between 0 and 20, classify it as "Cold."
# 4. If the temperature is between 21 and 35, classify it as "Warm."
# 5. If the temperature is above 35, classify it as "Hot."

temp = int(input("Enter Temperature: "))

if temp < 0:
    print("Freezing")
elif  temp >=0 and temp<=20:
    print("Cold")
elif temp >= 21 and temp <=35:
   print("Warm")
else:
   print("Hot")