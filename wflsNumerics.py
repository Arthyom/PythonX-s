
from sympy import *
from sympy.plotting import plot
import re 

class WflsNumerics(object):
    def __init__(self, expression = 0):
        if expression != 0:
            self.expression = sympify(expression)
            
    ### calculate fraction factors
    def fractions(self, lastTerm, firstTerm):
        a = []
        for fl in lastTerm:
            for ft in firstTerm:
                s = (1.0*fl)/ft
                if s not in lastTerm and s not in firstTerm: a.append(s)
        return a 

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
        factFraccion = self.fractions(fact2Do, fact1Er) ###[ fu/fp for fu in fact2Do for fp in fact1Er ]
        factorOptions = [fact2Do,fact1Er,factFraccion]

        ### iterate while not find total roots
        while roots < max(pows):
            ### iterate for each factor from one of three factors options
            for factN in factorOptions:
                ### iterate for all factors of the last coefficients
                for fi in factN:
                ### iterate for all coeficients
                    newCoeffs = []
                    for i, ci in enumerate(coeffs):
                        if i == 0:
                            newCoeffs.append(coeffs[0])
                        else:
                            ### is the second or more iteration
                            newCoeffs.append((fi * newCoeffs[i-1])+coeffs[i])
                    ### if the last number is 0, store the factor that produces it
                    if newCoeffs[-1] == 0:
                        coeffs = newCoeffs
                        listRoots.append(fi)
                        roots += 1
                factorOptions.remove(factN)
            if len(factorOptions) == 0: 
                listRoots.append('raices complejas')
                break
        return listRoots

    def plotIndependetExpression(self, expression, fromm, to):
        x = symbols('x')
        exp = sympify(expression)
        plot(exp, (x,fromm,to))
  
## +1x^4+0x^3-10x^2+0x+9
## +1x^4+1x^3-19x^2+11x+30
## +2x^4+1x^3-8x^2-1x+6
## +4x^4+9x^3-5x^2+9x-9
c = WflsNumerics()

##s =  c.hornerWfls("+4*x^4+9*x^3-5*x^2+9*x-9")
##print s
#c.plotIndependetExpression("+4*x^4+9*x^3-5*x^2+9*x-9", min(s), -min(s) )