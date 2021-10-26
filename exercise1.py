# -*- coding: utf-8 -*-
"""
The program should print two roots of the quadratic equation of the form

a x² + b x + c = 0

The roots must be stored in a tuple named xx and printed at the very end of the program.
"""

# This is sample input data

a = 1
b = 3
c = 2

# This is a tuple for a results. You should override it with actual results

solutions = ()

# DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!


# Put your here...
if a==0:
    x=-c/b
    solutions=(x,)
else:
    if b**2-4*a*c<0:
        pass
    elif b**2-4*a*c==0:
        x=-b/(2*a)
        solutions=(x,)
    elif b**2-4*a*c>0:
        x1=(-b-(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b+(b**2-4*a*c)**0.5)/(2*a)
        solutions=(x1,x2)



# At the end the results are printed to the screen
print(*solutions)
