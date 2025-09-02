# 16.	Weather Determination: Based on temperature and humidity, determine weather conditions.
def weather_determination(temp, humidity):
    if temp > 30:
        if humidity > 70:
            return "Hot and Humid"
        else:
            return " Hot and Dry"
    elif 20 <= temp <= 30:
        if humidity > 70:
            return "Warm and Humid"
        else:
            return "Pleasant"
    elif 10 <= temp < 20:
        return "Cool"
    else:
        return "Cold"

# Taking user input
try:
   temp = float(input("Enter the temperature in °C: "))
   humidity = float(input("Enter the humidity in %: "))

# Determining weather
   weather = weather_determination(temp, humidity)

# Display result
   print(f"The weather condition is: {weather}")
except ValueError:
  print("Enter the correct inputs") 