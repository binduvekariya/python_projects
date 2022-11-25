#first task
from math import pi

radius = float(input("input the radius of the circle: "))

print("the area of the circle with radius ",radius,"is",pi*radius**2)


#second task
import os
filename = input("Input the Filename: ") 
name, ext = os.path.splitext(filename)    
ext_with_dot = ext[1:]
print ("The extension of the file is : " + ext)
