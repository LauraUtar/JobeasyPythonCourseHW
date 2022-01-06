import math
# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula
# type your code here
temperature_fahrenheit = int(input('What is a temperature right now?: '))
result_temperature = round(int((temperature_fahrenheit - 32) * 5 / 9))
print('In Celsius it will be:', math.floor(result_temperature))
print((temperature_fahrenheit - 32) * 5 / 9)
print(int((temperature_fahrenheit - 32) * 5 / 9))
print(round(int(temperature_fahrenheit - 32) * 5 / 9))
