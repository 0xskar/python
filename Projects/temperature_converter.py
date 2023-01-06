# Temperature Converter
########################
#
# Simple script for converting fahrenheit to celcius and vice versa.
# 
# °F = (°C × 9/5) + 32 
#
# or
#
# °C = (°F − 32) x 5/9 
#
# 0xskar
#
########################

conversion_options = ["Celcius", "C", "Fahrenheit", "F"]

print("Temperature Converter by 0xskar")
print("Please, which temperature would you like converted?")
convert = input("Enter C or Celcius, or F or Fahrenheit: ")
convert = str(convert.capitalize())

while convert not in conversion_options:
    print("You didnt enter a valid choice.")
    print("Please, which temperature would you like converted?")
    convert = input("Enter C or Celcius, or F or Fahrenheit: ")
    convert = str(convert.capitalize())

# Fahrenheit Conversion

if convert == conversion_options[2] or convert == conversion_options[3]:
    while True:
        try:
            print("Preparing to convert fahrenheit...")
            temperature = int(input("Enter the temperature in fahrenheit: "))
            break
        except ValueError:
            print("Not a valid number, try again...")
        
    temperature_output = (temperature - 32) * 5 / 9    
    print(temperature, " fahrenheit equals: ", temperature_output)

# Celcius Conversion

if convert == conversion_options[0] or convert == conversion_options[1]:
    while True:
        try:
            print("Preparing to convert celcius...")
            temperature = int(input("Enter the temperature in celcuis: "))
            break
        except ValueError:
            print("Not a valid number, try again...")

    temperature_output = (temperature * 9/5) + 32
    print(temperature, " celcuis equals: ", temperature_output)
