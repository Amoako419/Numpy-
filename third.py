
import numpy as np 
print("This code prints a odd number with your range")
try:
    a = int(input("The start of the range"))
    b = int(input("The end of the range"))
except ValueError:
    print("Input a number")
c = np.array(range(a,b,2))
print (c)