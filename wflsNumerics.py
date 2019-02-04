
from sympy import *
from sympy.plotting import plot
import re 

class WflsNumerics(object):
    def __init__(self, expression = 0):
        if expression != 0:
            self.expression = sympify(expression)
            
    ### calculate cofficients of a number
    def factorsOf (self, number ):
        factors = []
        for n in range(1,abs(number)+1):
            if abs(number)%n ==0: 
                factors.append(n)
                factors.append(-n)
        return factors

    def hornerWfls(self, expression ):
        listRoots = []
        roots = 0
        coeffs = map(int, re.findall(r"([+-]\d+)", expression.replace(' ', '')))
        pows = map(int, re.findall(r"[x^](\d+)", expression.replace(' ', '')))
        fact1Er = self.factorsOf(coeffs[0])
        fact2Do = self.factorsOf(coeffs[-1])
        factFraccion = []

        ### iterate while not find total roots
        while roots < max(pows):
            ### iterate for all factors of the last coefficients
            for fi in fact2Do:
                ### iterate for all coeficients 
                newCoeffs = []
                for i, ci in enumerate(coeffs):
                    if i == 0:
                        newCoeffs.append(coeffs[0])
                    else:
                        ### is the second or more iteration
                        newCoeffs.append( (fi * newCoeffs[i-1])+coeffs[i] )
                ### if the last number is 0, store the factor that produces it
                if newCoeffs[-1] == 0:
                    coeffs = newCoeffs
                    listRoots.append(fi)
                    roots += 1
        return listRoots

    def plotIndependetExpression(self, expression, fromm, to):
        x = symbols('x')
        exp = sympify(expression)
        plot(exp, (x,fromm,to))
  
## +1x^4+0x^3-10x^2+0x+9
## +1x^4+1x^3-19x^2+11x+30
#c = WflsNumerics()

#s =  c.hornerWfls("+1x^4+1x^3-19x^2+11x+30")

#print  
#print  c.plotIndependetExpression("+1*x^4+1*x^3-19*x^2+11*x+30", min(s), -min(s) )