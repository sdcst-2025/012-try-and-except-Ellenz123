#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")


try:
  a=float(input("Enter the first number:"))
  b=float(input("Enter the second number:"))
  c=float(input("Enter the third number:"))
  x=b**2 - 4*a*c
  if x<0:
    print("There are no real roots to the equation")
  elif x==0:
    root=-b/(2*a)
    print(f"The roots are {root} and {root}")
  else:
    root1=(-b+math.sqrt(x))/(2*a)
    root1=round(root1,2)
    root2=(-b-math.sqrt(x))/(2*a)
    root2=round(root2,2)
    print(f"The roots are {root1} and {root2}")


except Exception as e:
  print("Those are not valid values for a, b or c")