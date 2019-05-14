import pyowm
import random
from math import pow
from math import pi

city = input("What city you are interested: ")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city " + w.get_detailed_status())

# -----------------------------1--------------------
a = random.randint(0, 100)
b = int(input("Enter your number: "))
while True:
    if b == a:
        print("You are a win")
        break
    elif b < a:
        b = int(input("Enter the most number: "))
    else:
        b = int(input("Enter the less number: "))

#-----------------------2----------------------------
def s_circle():
    radius = int(input("Enter radius of the circle: "))
    S = pi * pow(radius, 2)
    print("S of circle =", S)

def s_triangle():
    a = int(input("Enter side of the triangle: "))
    h = int(input("Enter height of the triangle: "))
    S = 0.5 * a * h
    print("S of the circle =", S)

def s_rectangle():
    a = int(input("Enter first side of the rectangle: "))
    b = int(input("Enter second side of the rectangle: "))
    S = a * b
    print("S of the rectangle =", S)

print("1 = S circle\n"
      "2 = S triangle\n"
      "3 = S rectangle")
user = int(input("Choice figure:"))
if user == 1:
    (s_circle())
elif user == 2:
    (s_triangle())
elif user == 3:
    (s_rectangle())
else:
    print("Input Error")







