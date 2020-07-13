from math import *
x = float(input("Введіть  х ="))

e = 2.71828
y = atan(x) + ((pow(e,0.6*x-1)-pow(x+6.1,3/2))/(log(x)+pow(log10(x),2)))
print (y)
