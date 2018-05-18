from sympy      import *
from numpy      import *
from matplotlib import pyplot as plt
class Funcion:

    def __init__         ( self, rango, funcion_Texto, identificador ):
        ###declarar variables
        self.vals_Rango     = rango
        self.x              = symbols('x')
        self.y              = symbols('y')
        self.funcion_Texto  = funcion_Texto
        self.nombre         = identificador
        self.funcion_Objeto = sympify(funcion_Texto)
        self.rango          = arange(rango[0],rango[1],rango[2])

        ### evaluar la funcion en todos los puntos del rango_X
        f                   = lambdify( self.x, self.funcion_Objeto, 'numpy' )
        self.dominio        = f(self.rango)


    def imprimir_Funcion (self):
        print(self.funcion_Objeto)

    def imprimir_Rango   (self):
        print(self.rango)

    def imprimir_Dominio (self):
        print(self.dominio)

    def graficar         (self, name, tipo='d'):

        if tipo == 'd':
            markerline, stemlines, baseline = plt.stem(self.rango, self.dominio,markerfmt='o',label=self.funcion_Texto)
            plt.legend()
            plt.setp(stemlines, 'color', plt.getp(markerline,'color'))
        else:
            plt.plot(self.rango, self.dominio)

        plt.savefig(name+'.png')


        return name+'.png'

    def limpiar          (self):
        plt.clf()


    ### funciones con tipo de retorno
    #### crea una nueva funcion corrida y la regresa

    def corrimiento      (self, t0):
        ### crea una nueva funcion a partir de la funcion actual
        fn = Funcion(self.vals_Rango, self.funcion_Texto, self.nombre + " corrimiento " + str(t0) )
        nuevo_Dominio = []


        for indx,vals in enumerate( fn.rango ):
            if( indx + t0 < len(fn.rango) ):
                nuevo_Dominio.append( self.dominio[ indx + t0 ] )
            else:
                nuevo_Dominio.append(0.0)

        fn.dominio = nuevo_Dominio

        return fn

    def escalamiento     (self, t0):
        pass

    def inversion        (self, t0):
        pass

    ### volver a evaluar el rango dado
    def reevaluar_Rango  (self, x):
        r = ["Funcion "+ self.funcion_Texto + " Continua y Discreta"]
        self.rango = x
        f = lambdify( self.x, self.funcion_Objeto, 'numpy' )
        self.dominio =  f(x)
        r.append(self.dominio)
        return r


    def __add__          (self, f2 ):
        nuevo_Dominio = []
        f3 = Funcion( self.vals_Rango, self.funcion_Texto + " + " +f2.funcion_Texto, "suma de funciones")
        for f1,f2 in zip(self.dominio, f2.dominio):
            nuevo_Dominio.append(f1+f2)
        f3.dominio = nuevo_Dominio

        return f3

    def __sub__          (self,f2):
        nuevo_Dominio = []
        f3 = Funcion( self.vals_Rango, self.funcion_Texto + " - " +f2.funcion_Texto, "resta de funciones")
        for f1,f2 in zip(self.dominio, f2.dominio):
            nuevo_Dominio.append(f1-f2)
        f3.dominio = nuevo_Dominio
        return f3

    def __mul__          (self,f2):
        nuevo_Dominio = []
        f3 = Funcion( self.vals_Rango, self.funcion_Texto + " * " +f2.funcion_Texto, "multiplicacion de funciones")
        for f1,f2 in zip(self.dominio, f2.dominio):
            nuevo_Dominio.append(f1*f2)
        f3.dominio = nuevo_Dominio
        return f3
