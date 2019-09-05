#Tómas Ingi Villalobos
#1502003260, 8/20/2019
"""
#Verkefni 1.1
m_str = input('Input m: ')  # do not change this line

m_float = float(m_str) #breytir m_str i float
c = float(300000000)


e = m_float* pow(c,2)
print("e =", e)  # do not change this line

"""
"""
#Verkefni 1.2
in_str = input("Input s: ")
in_int = int(in_str)
print("in_int = ", in_int)
in_float = float(in_int)
print("in_float = ", in_float)
"""
"""
#Verkefni 1.3
import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

d = math.hypot (x1_int - x2_int, y1_int - y2_int)
print("d =",d)  # do not change this line
"""
"""
#Verkefni 1.4

weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_int = float(weight_str)
height_int = float(height_str)/100


bmi = (weight_int) / (height_int**2)

print("BMI is: ", bmi) # do not change this line
"""
"""
#Verkefni 1.5

x_str = input("Input x: ")

first_three = int(x_str)// 1000
last_two = int(x_str) % 100
middle_two = int(x_str) // 100 % 100
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)
"""
"""
#Verkefni 1.6
secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
 
hours = (secs_int // 3600)
minutes = (secs_int%3600)//60
seconds = (secs_int%60)
print(hours,":",minutes,":",seconds) # do not change this line
"""




