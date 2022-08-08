#This file contains demonstrations of several modules from the python packages functools and itertools to incorporate a functional paradigm
#Import the required packages
import math
from functools import partial
from itertools import count,cycle,repeat

#Function to demonstrate the use of partial functions
def multiply(a, b):
    return a*b

#Function within function 
def Cylinder(r):
    def volume(h):
        return math.pi * r * r * h
    return volume

#Use of itertools modules to generate text in the prescribed format
def itertools_func():
    iter_cycle = cycle(['Yes','No','Maybe'])
    iter_count = count(1,1)
    iter_repeat= repeat('OK')
    a = 0
    for i in zip(iter_cycle,iter_count,iter_repeat):
        print(i)
        a+=1
        if a==5:
            break

#Function calls for all the above functions
q = partial(multiply, b=2)
result = q(10)
print("The product of the given numbers are",result)

q1=Cylinder(5)
q2=q1(10)

print('The volume of the cylinder is:',q2)
q3 = itertools_func()


