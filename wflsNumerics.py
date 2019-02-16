
from sympy import *
from sympy.plotting import plot
import re 
import math
import numpy 

class WflsNumerics(object):
    def __init__(self, expression = 0):
        if expression != 0:
            self.strExpression = expression
            self.expression = sympify(expression)
            self.x = symbols('x')
            self.EA = 1e-10

    def getError(self,xNew, xOld):
        error = 0
        if xNew != 0:
            error = abs((xNew - xOld)/(xNew*1.0))*100
        return error

    def findSignusChange(self,a,b,x):       
        interval = list(numpy.arange(a,b,x))
        subint   = []

        for i,vi in enumerate(interval):
            if i+1 < len(interval):
                fa = self.expression.subs(self.x, vi)
                fb = self.expression.subs(self.x, interval[i+1])
                if (fa * fb) <= 0:
                    subint.append([vi, interval[i+1]]) 
        return subint

    def getPows(self):
        pows = map(int, re.findall(r"[x^](\d+)", self.strExpression.replace(' ', '')))
        return pows

    def getCoefficents(self):
        coeffs = map(int, re.findall(r"([+-]\d+)", self.strExpression.replace(' ', '')))
        return coeffs

    ### this method asumess that exist an matematic expression    
    def wflsRegulaFalsi(self,a,b,x, maxIt):
        subranges = self.findSignusChange(a,b,x)
        ### check if there is a signus change in the expression
        roots = []; c = 0; i = 0; z = 0
        
        for a,b in subranges:
            i = 0
            ### calculate f(a) , f(b)
            fa = self.expression.subs(self.x, a)
            fb = self.expression.subs(self.x, b)
            ### check if exists a signus change in the interval
            if (fa * fb <= 0):
                while maxIt > i:
                    z = c
                    c = (a*fb -  (1.0*b)*fa)/(fb - fa)
                    ### calculate fa . fc, fb . fc
                    fc = self.expression.subs(self.x, c)
                    ### check root cases
                    if fc == 0 or self.getError(c,z) <= self.EA:
                        ### fc is a solution
                        if c not in roots:
                            roots.append(c)
                            print '.....................'
                            break
                    else:
                        if fa * fb > 0: a = c
                        else: b = c
                    i += 1 
                    
        return roots

    def wflsSimpleRegulaFalsi(self,a,b):
        ### check if there is a signus change in the expression
        c = 0; i = 0; z = 0
        ### get the maximum number of iterations
        maxIt = self.maxIterations(a,b)
        ### calculate f(a) , f(b)
        while maxIt >= i:
            fa = self.expression.subs(self.x, a)
            fb = self.expression.subs(self.x, b)
            ### check if exists a signus change in the interval
            if (fa * fb <= 0):
                z = c
                c = (a*fb -  (1.0*b)*fa)/(fb - fa)
                ### calculate fa . fc, fb . fc
                fc = self.expression.subs(self.x, c)
                ### check root cases
                if fc == 0 or self.getError(c,z) <= self.EA: return c
                else:
                    if fa * fb > 0: a = c
                    else: b = c
                i += 1
        return 'nf'

    ### this method asumess that exist an matematic expression    
    def wflsBissection(self,a,b,x, maxIt):
        subranges = self.findSignusChange(a,b,x)
        ### check if there is a signus change in the expression
        roots = []; c = 0; i = 0; z = 0
        
        for a,b in subranges:
            i = 0
            ### calculate f(a) , f(b)
            fa = self.expression.subs(self.x, a)
            fb = self.expression.subs(self.x, b)
            ### check if exists a signus change in the interval
            if (fa * fb <= 0):
                while maxIt > i:
                    z = c
                    c = (a+b)/2*(1.0)
                    ### calculate fa . fc, fb . fc
                    fca = fa * self.expression.subs(self.x, c)
                    ### check root cases
                    if   fca > 0: a = c
                    elif fca < 0: b = c
                    elif fca == 0 or self.getError(c,z) <= self.EA:
                        roots.append(c)
                        break
                    i += 1
        return roots
    

    def maxIterations(self, a,b ):
        maxIt = 0
        if a != 0 or b != 0: 
            maxIt = round( (abs( (math.log(abs(b-a)) - math.log(self.EA))/ math.log(2) )) ,0 )
        return int(maxIt)

    def wflsSimpleBissection(self,a,b):
        ### check if there is a signus change in the expression
        c = 0; i = 0; z = 0
        ### get the maximum number of iterations
        maxIt = 100#self.maxIterations(a,b) 
        while maxIt >= i:
            ### calculate f(a) , f(b)
            fa = self.expression.subs(self.x, a)
            fb = self.expression.subs(self.x, b)
            ### check if exists a signus change in the interval
            if (fa * fb <= 0):
                ##maxIt = self.maxIterations(a,b)
                z = c
                c = (a+b)/(2*(1.0))
                ### calculate fa . fc, fb . fc
                fca = fa * self.expression.subs(self.x, c)
                if fca == 0 or self.getError(c,z) <= self.EA :  return c
                ### check root cases
                elif   fca > 0: a = c
                elif   fca < 0: b = c
            i += 1
        return 'nf'


    ### calculate fraction factors
    def fractions(self, lastTerm, firstTerm):
        a = []
        for fl in lastTerm:
            for ft in firstTerm:
                s = (1.0*fl)/ft
                if s not in lastTerm and s not in firstTerm: a.append(s)
        return a 

    def evaluateX(self, val):
        s =self.expression.subs(self.x, val)
        return s

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
        plot(exp, (x,fromm,to), title=expression)
  
## +1*x^4+0*x^3-10*x^2+0*x+9
## +1*x^5-25*x^3+1*x^2+0*x-25
## +1*x^5-25*x^3+1*x^2+0*x-25
## +1*x^4+1*x^3-19*x^2+11*x+30
## +2*x^4+1*x^3-8*x^2-1*x+6
## +4*x^4+9*x^3-5*x^2+9*x-9
c = WflsNumerics("1*x^3 - 2*x^2 +1")
#print c.evaluateX(0.0750794556940274)
#Sprint c.wflsBissection(-1 ,2 ,.5,100)

#print c.findSignusChange(-6,4)

print  'regula ->: ' + str( c.wflsSimpleRegulaFalsi(-.7, -.4))
#print c.evaluateX(-1), c.evaluateX(-.5)

print 'Bissec ->: '+ str( c.wflsSimpleBissection(-.7,-.4) )

#print c.wflsBissection(-4, -.5)
#print c.hornerWfls("1*x^3 - 2*x^2 +1")
#print s
#c.plotIndependetExpression("+1*x^4+1*x^3-19*x^2+11*x+30", -7, 7) 

# 1*x^3 - 2*x^2 +1