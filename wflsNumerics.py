
from sympy import *
from sympy.plotting import plot
from matplotlib import pyplot as plt 
import re 
import math
import numpy 
import time

class WflsNumerics(object):
    def __init__(self, expression = 0):
        if expression != 0:
            self.strExpression = expression
            self.expression = sympify(expression)
            self.x = symbols('x')
            self.EA = 1e-8
            self.fx = 0
            self.x = 0

##################################################################
###############          tools functions           ###############
##################################################################
    def evaluateInterval(self, fromm, to, step):
        x = numpy.arange(fromm, to, step)
        s = []
        
        for xi in x:
            print self.evaluateX(xi)
            

    def tableInformation(self, name, i, timeStart, xOld, xNew, error, xi):
        end = time.time()
        header =  str(i) +','+str(error)

        self.fileTable = open(name,'a')
        self.fileTable.write(header)
        self.fileTable.write('\n')
    
        #self.fileTable.write('\n\n')

        self.fileTable.close()

    def getError(self,xNew, xOld):
        error = 0
        if xNew != 0:
            error = abs((xNew - xOld)/(xNew*1.0))*100
        return error

    def findSignusChange(self,a,b,x):
        k = 1
        interval = list(numpy.arange(a,b,x))
        subint   = []
        
        for i,vi in enumerate(interval):
            
            if len(interval)> k+i:
                a = interval[i+i]
                b = interval[i+k]
                fa = self.evaluateX(a)
                fb = self.evaluateX(b)
                if fa*fb <= 0:
                    subint.append( [a,b] )
            elif len(interval) <= k+i:
                a = interval[i-1]
                b = interval[i]               
                fa = self.evaluateX(a)
                fb = self.evaluateX(b)
                if fa*fb <= 0:
                    subint.append( [a,b] )
            k += 1

        return subint

    def getPows(self):
        pows = map(int, re.findall(r"[x^](\d+)", self.strExpression.replace(' ', '')))
        return pows

    def getCoefficents(self):
        coeffs = map(int, re.findall(r"([+-]\d+)", self.strExpression.replace(' ', '')))
        return coeffs

       ### calculate fraction factors
    
    def fractions(self, lastTerm, firstTerm):
        a = []
        for fl in lastTerm:
            for ft in firstTerm:
                s = (1.0*fl)/ft
                if s not in lastTerm and s not in firstTerm: a.append(s)
        return a 

    def evaluateX(self, val):
        s = self.expression.evalf(self.x, val)
        return s

    ### calculate cofficients of a number
    def factorsOf (self, number ):
        factors = []
        for n in range(1,abs(number)+1):
            if abs(number)%n ==0: 
                factors.append(n)
                factors.append(-n)
        return factors

    def maxIterations(self, a,b ):
        maxIt = 0
        if a != 0 or b != 0: 
            maxIt = round( (abs( (math.log(abs(b-a)) - math.log(self.EA))/ math.log(2) )) ,0 )
        return int(maxIt)

##################################################################
###############       interpolation functions      ###############
##################################################################S

### it uses the expression entered to generate an a cheby intepolation
### usign the cheb's polinomial grade that is enteder
    def divDiferencess(self):
        s = []; k = []
        s.append( [self.x] )

        ### calculate differences 
        for div in s:
            print div
            for i, val in enumerate(div):
                if len(div) >= 2:
                    if i >= len(div):
                        si = (self.evaluateX(div[1+i]) - self.evaluateX(div[i]))/div[i+i]-div[i]
                        k.append(si)
                    s.append(k)

       


    def interpolChebyshev(self,n, fromm, to):
        coefs = []
        ### get the chebyshev's nodes o roots 
        chebsRoots = numpy.polynomial.Chebyshev.basis(n+1).roots()
        
        ### calculate the chebyshevs coef's
        for s in range(0,n+1):
            sum = 0
            if s == 0 : 
                for i,val in enumerate(chebsRoots):
                    sum += self.expression.subs(self.x,val).evalf()
                coefs.append( (sum/(n+1.0)) )
                
            else:
                for i,val in enumerate(chebsRoots):
                    c = math.cos( (s*math.pi* ((2*i+1.0))/(2*n+2.0)) )
                    sum += self.evaluateX(val) * c
                coefs.append( abs((2*sum/(n+1.0))) )
        
        x,y = numpy.polynomial.Chebyshev(coefs).linspace()
        return x,y

            

       



    def chebsHomework(self):
        ### calculate function values
        x = numpy.arange(-1,1, 2.0/100)
        f = lambdify(self.x, self.expression, 'numpy') 
        y = f(x)
        plt.plot(x,y, label='f(x)')
        

        ### calculate chebs values
        for i in range(4,8):
            xCheb,yCheb = self.interpolChebyshev(i,-1,1)
            l = 'P'+str(i)
            plt.plot(xCheb,yCheb, label=l)

        plt.legend(loc='best')
        plt.show()



##################################################################
###############          roots functions           ###############
##################################################################S
    def wflsRootsGeneralBissection(self,a,b,x):
        globalInterval = self.findSignusChange(a,b,x)
        functiongrade = max( self.getPows() )
        ### check if there is a signus change in the expression
        roots = [];  findedRoots = 0
        for a,b in globalInterval:
            c = 0; i = 1; z = 0
            ### get the maximum number of iterations
            maxIt = 100#self.maxIterations(a,b) +2
            while maxIt >= i:
                start = time.time()
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
                    error = self.getError(c,z)
                    name = self.strExpression
                    name = name.replace('*','-')
                    name = name.replace('^','-')
                    self.tableInformation('infoBisection'+name+'.txt',i, start, z, c, error,c) 
                    if fca == 0 or error <= self.EA :
                        if c not in roots and functiongrade > findedRoots :
                            ###print table information 
                            
                            roots.append(c)
                            findedRoots += 1
                    ### check root cases
                    elif   fca > 0: a = c
                    elif   fca < 0: b = c
                i += 1
        return roots

    def wflsRootsGeneralNewton(self,a,b,x):
        globalInterval = self.findSignusChange(a,b,x)
        functiongrade = max( self.getPows() )
        ### check if there is a signus change in the expression
        roots = [];  findedRoots = 0
        for a,b in globalInterval:
            ###declate variables
            i = 1; xi = a; xiAnt = 0
            maxIt = 20#self.maxIterations(a,0)
            while maxIt >= i:
                start = time.time()
                ###calculate f'(xi) and f(xi)
                fxi  = self.expression.subs(self.x,xi)
                dfxi = self.expression.diff(self.x).subs(self.x,xi)
                ###save the anterior point
                xiAnt = xi
                ###calculate new point
                if dfxi != 0:
                    xi = round( xi - (fxi/dfxi), 8)
                    error = self.getError(xi,xiAnt)
                    name = self.strExpression
                    name = name.replace('*','-')
                    name = name.replace('^','-')
                    self.tableInformation('infoNewton'+name+'.txt',i, start, xiAnt, xi, error,xi) 
                if fxi == 0 or self.getError(xi,xiAnt) <= self.EA:
                    if xi not in roots and functiongrade > findedRoots :
                        roots.append(xi)
                        findedRoots += 1
                i += 1
        return  roots
    
    def wflsRootsGeneralSecante(self,a,b,x):
        globalInterval = self.findSignusChange(a,b,x)
        functiongrade = max( self.getPows() )
        ### check if there is a signus change in the expression
        roots = [];  findedRoots = 0
        for a,b in globalInterval:
            
            c = 0; i = 1; z = 0
            maxIt = 20#self.maxIterations(a,b)
            while maxIt >= i : 
                start = time.time()
                ###calculate f(a) = f(xi-1)
                fa = self.evaluateX(a)
                ###calculate f(b) = f(xi)
                fb = self.evaluateX(b)
                ###save the old c value
                z = c
                ###calculate f(c) = f(xi+1)
                if(fb-fa != 0):
                    c = a-(fa*(b-a)/(fb - fa))
                else : c= 0
                ###check if xi1 is a valid root
                error = self.getError(c,b)
                name = self.strExpression
                name = name.replace('*','-')
                name = name.replace('^','-')
                self.tableInformation('infoSecamte'+name+'.txt',i, start, z, c, error,c) 
                if self.evaluateX(c) == 0 or self.getError(c,b) <= self.EA:
                    if c not in roots and functiongrade > findedRoots :
                       
                        roots.append(c)
                        findedRoots += 1
                else:
                    a=b; b=c
                i += 1
        return roots

    def wflsRootsGeneralRegulaFalsi(self,a,b,x):
        globalInterval = self.findSignusChange(a,b,x)
        functiongrade = max( self.getPows() )
        ### check if there is a signus change in the expression
        roots = [];  findedRoots = 0
        for a,b in globalInterval:
            c = 0; i = 1; z = 0
            maxIt = 20#self.maxIterations(a,b)
            ### calculate f(a) , f(b)
            while maxIt >= i:
                start = time.time()
                fa = self.expression.subs(self.x, a)
                fb = self.expression.subs(self.x, b)

                ### check if exists a signus change in the interval
                if (fa * fb <= 0):
                    z = c
                    if(fb-fa != 0):
                        c = a-(fa*(b-a)/(fb - fa))
                    else : c= 0
                    ### calculate fa . fc, fb . fc
                    fc = self.expression.subs(self.x, c)
                    ### check root cases
                    error = self.getError(c,z)
                    name = self.strExpression
                    name = name.replace('*','-')
                    name = name.replace('^','-')
                    self.tableInformation('infoRegula'+name+'.txt',i, start, z, c, error,c) 
                    if fc*fa == 0 or self.getError(c,z) <= self.EA: 
                        if c not in roots and functiongrade > findedRoots :
                            
                            roots.append(c)
                            findedRoots += 1
                    else:
                        if fa * fc < 0: b = c
                        else: a = c
                i += 1
        return roots

    
    
    def wflsRootsSimpleNewton(self,a):
        ###declate variables
        i = 0; xi = a; xiAnt = 0
        ###get maximun number of iterations
        #maxIt = self.maxIterations()
        maxIt = self.maxIterations(a,0)
        while maxIt >= i:
            ###calculate f'(xi) and f(xi)
            fxi  = self.expression.subs(self.x,xi)
            dfxi = self.expression.diff(self.x).subs(self.x,xi)
            ###save the anterior point
            xiAnt = xi
            ###calculate new point
            xi = xi - (fxi/dfxi)
            if fxi == 0 or self.getError(xi,xiAnt) <= self.EA:return xi
            i += 1
        return 'nf'
        
    def wflsRootsSimpleBissection(self,a,b):
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

    def wflsRootsSimpleSecante(self,a,b):
        ###declare variables
        c = 0; i = 0; z = 0; maxIt = self.maxIterations(a,b)
        while maxIt >= i : 
            ###calculate f(a) = f(xi-1)
            fa = self.evaluateX(a)
            ###calculate f(b) = f(xi)
            fb = self.evaluateX(b)
            ###save the old c value
            z = c
            ###calculate f(c) = f(xi+1)
            c = b-(fb*(a-b)/(fa-fb))
            ###check if xi1 is a valid root
            if self.evaluateX(c) == 0 or self.getError(c,b) <= self.EA:
                return c
            else:
                a=b; b=c
            i += 1
        return 'nf'

    def wflsRootsSimpleRegulaFalsi(self,a,b):
        ### check if there is a signus change in the expression
        c = 0; i = 0; z = 0
        ### get the maximum number of iterations
        ### sometimes it needs some extra iterations
        maxIt = 100#self.maxIterations(a,b)
        ### calculate f(a) , f(b)
        while maxIt >= i:
            fa = self.expression.subs(self.x, a)
            fb = self.expression.subs(self.x, b)

            ### check if exists a signus change in the interval
            if (fa * fb <= 0):
                z = c
                if(fb-fa != 0):
                    c = a-(fa*(b-a)/(fb - fa))
                else : c= 0
                ### calculate fa . fc, fb . fc
                fc = self.expression.subs(self.x, c)
                ### check root cases
                if fc*fa == 0 or self.getError(c,z) <= self.EA: return c
                else:
                    if fa * fc < 0: b = c
                    else: a = c
            i += 1
        return 'nf'

    def wflsRootshorner(self, expression ):
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

##################################################################
###############        ploting functions           ###############
##################################################################
    def plotIndependetExpression(self, expression, fromm, to):
        x = symbols('x')
        exp = sympify(expression)
        plot(exp, (x,fromm,to), title=expression)
  
    def plotExpression(self):
        plot(self.expression )

    def plotExpressioFromTo(self, fromm, to):
        plot(self.expression, (self.x,fromm,to) )


#resultados = [[3,4,0.3,'+2*x^3-11.7*x^2+17.5*x-5']]

#for a,b,x,exp in resultados:
#    objExp = WflsNumerics(exp)
#    print( 'Function -> '+ objExp.strExpression)
#    print( 'Regula  ->: '+ str(objExp.wflsRootsGeneralRegulaFalsi(a,b,x)))
#    print( 'Bissec  ->: '+ str(objExp.wflsRootsGeneralBissection(a,b,x) ))
#    print( 'newton  ->: '+ str(objExp.wflsRootsGeneralNewton(a,b,x)))
#    print( 'secant  ->: '+ str(objExp.wflsRootsGeneralSecante(a,b,x)))
#    print('\n\n')
#    objExp.plotExpressioFromTo(a,b)


#objExp = WflsNumerics('ln(x+2)')
#objExp = WflsNumerics('exp(x)')
#objExp = WflsNumerics('cos(x)')
#objExp = WflsNumerics('(x+2)^(1/2)')
#objExp = WflsNumerics('(x+2)^(x+2)')
objExp = WflsNumerics('x+2')

#objExp.interpolChebyshev(3,-1,1)
#objExp.chebsHomework()
objExp.evaluateInterval(0,6,1)
#objExp.divDiferencess()
    