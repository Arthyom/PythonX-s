import matplotlib.pyplot as plt
import math as mat
import numpy as num

def graph_Escalon(x):
    r = ["Funcion Escalon Discreta y Continua"]
    y = [ ]
    for xs in x:
        if xs >= 0:
            y.append(1)
        elif xs < 0:
            y.append(0)
    r.append(y)
    return r

def graph_Impulso(x):
    r = ["Funcion Impulso Discreta y Continua"]
    y = []
    for xs in x:
        if xs == 0:
            y.append(1)
        elif xs != 0:
            y.append(0)
    r.append(y)
    return r

def graph_Exponencial(x):
    a = float(raw_input("\tFuncion Exponencial [e^(at)]\n\t\tEscriba el valor de [a] "))
    r = ['Funcion Exponencial Discreta y Continua']
    y = [ a * mat.exp(xs) for xs in x ]
    r.append(y)
    return r

def graph_Senoidal(x):
    print("\tFuncion Senoidal [A0 * Sen(wt + o)]")

    a0  = float(raw_input("\t\t\tEscriba el valor de [a0] "))
    omg = float(raw_input("\t\t\tEscriba el valor de [w]  "))
    fi  = float(raw_input("\t\t\tEscriba el valor de [fi] "))

    r = ["Funcion Senoidal Discreta y Continua"]
    y = [ a0 * mat.sin( (xs*omg) + fi) for xs in x ]
    r.append(y)
    return r

def graph_Cosenoidal(x):
    print("\tFuncion Cosenoidal [A0 * Cos(wt + o)]")

    a0  = float(raw_input("\t\t\tEscriba el valor de [a0] "))
    omg = float(raw_input("\t\t\tEscriba el valor de [w]  "))
    fi  = float(raw_input("\t\t\tEscriba el valor de [fi] "))

    r = ["Funcion Cosenoidal Discreta y Continua"]
    y = [ a0 * mat.cos( (xs*omg) + fi) for xs in x ]
    r.append(y)
    return r

def graph_CosenoExponencial(x):
    print("\tFuncion Coseno Exponencial [C e^(rt) * Cos(wt)]")
    c    = float(raw_input("\t\t\tEscriba el valor de [C] "))
    r1   = float(raw_input("\t\t\tEscriba el valor de [r] "))
    omg  = float(raw_input("\t\t\tEscriba el valor de [w] "))

    r = ["Funcion Coseno Exponencial Discreta y Continua"]
    y = [  c * mat.exp(r1*xs) * mat.cos( xs*omg ) for xs in x ]
    r.append(y)

    return r

def desplegar_Menu ():
    print "Seleccione la funcion a graficar"
    print "\t[1] Funcion Escalon"
    print "\t[2] Funcion Impulso"
    print "\t[3] Funcion Exponencial"
    print "\t[4] Funcion Senoidal"
    print "\t[5] Funcion Cosenoidal"
    print "\t[6] Funcion Coseno Exponencial"

    return int( raw_input("\t->") )

def preparar_Rango ():
    y = []
    y.append( float(raw_input("Escriba el inicio      del rago [a] ")))
    y.append( float(raw_input("Escriba el final       del rago [b] ")))
    y.append( float(raw_input("Escriba el incrementos del rago [c] ")))
    print (" ")

    return y

def prepararGrafico(x):
    r = 0; y = 0; k = desplegar_Menu()

    if k == 1 :
        r,y = graph_Escalon(x)

    elif k == 2:
        r,y = graph_Impulso(x)

    elif k == 3:
        r,y = graph_Exponencial(x)

    elif k == 4:
        r,y = graph_Senoidal(x)

    elif k == 5:
        r,y = graph_Cosenoidal(x)

    elif k == 6:
        r,y = graph_CosenoExponencial(x)

    print('\tGraficando..... ')

    plt.subplot(2,1,1)
    plt.title(r)
    plt.grid(True)
    plt.ylabel('s')
    plt.xlabel('t')
    plt.stem(x,y,'r')
    plt.plot(x,y)

    plt.subplot(2,1,2)
    plt.grid(True)
    plt.ylabel('s')
    plt.xlabel('t')
    plt.plot(x,y)


def main ():
    a, b, c = preparar_Rango()
    x = num.arange(a,b,c)
    prepararGrafico(x)
    plt.show()

main()
