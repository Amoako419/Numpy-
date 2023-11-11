import numpy as np

a = np.arange(6)
print("1d array")
print(a.dtype)
print(a,end="\n")


b = np.arange(12).reshape(4,3)
print(b.dtype)
print("2d array")
print(b)

c = np.arange(24).reshape(2,3,4)
print(c.dtype)
print("3d array")
print(c)

d =np.linspace(1,16,10)
print("4d array")
print(d.dtype)
print(d,end="\n")