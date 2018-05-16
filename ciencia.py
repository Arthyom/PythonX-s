from numpy import *
from sympy import *

# get string expression
x = symbols('x')
st_exp = raw_input()
exp = sympify(st_exp)
a = arange(0,10+1,)

#f = lambdify(x,exp,'numpy')
#print( f(a) )



#print(exp)
#k = exp.subs(x,1)
#print(k)
#print(k.evalf())
