#first task
from math import pi

radius = float(input("input the radius of the circle: "))

print("the area of the circle with radius ",radius,"is",pi*radius**2)


#second task
import os
filename = input("Input the Filename: ") 
name, exe = os.path.splitext(filename)    
f = filename.split(".")
print ("The extension of the file is : " + f[-1])
