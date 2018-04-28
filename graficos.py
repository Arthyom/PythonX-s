import matplotlib.pyplot as plt
import math as mat
import numpy as num

def graph_EscalonContinuo (rango):
    x = range(rango[0], rango[1])
    y = []

    for xs in x:
        if xs >= 0:
            y.append(1)
        elif xs < 0:
            y.append(0)

    plt.plot(x,y)


def graph_EscalonDiscreto (rango):
    pass

def graph_ImpulsoUnitarioContinuo (rango):
    x = range(rango[0], rango[1])
    y = []

    for xs in x:
        if xs == 0:
            y.append(1)
        elif xs == 0:
            y.append(0)

    plt.plot(x,y)

def graph_ImpulsoUnitarioDiscreto (rango):
    pass


def graph_ExponencialContinuo (a,rango):
    x = range(rango[0], rango[1])
    y = []
    for xs in x:
        y.append(mat.exp(xs))
    plt.plot(x,y)


def graph_ExponencialDiscreto(a, rango):
    pass


def graph_SenoidalContinua(a0, omg, fi, rango):
    x = num.arange(rango[0],rango[1])
    y = []
    for xs in x:
        y.append( a0 * (180.0/mat.pi) * mat.sin( (omg * xs) )+ fi )
    plt.plot(x,y)



def graph_CosenoidalContinua(a0, omg, fi, rango):
    pass

def graph_SenoidalDiscreta(a0, omg, fi, rango):
    pass

def graph_CosenoidalDiscreta(a0, omg, fi, rango):
    pass

def graph_CosenoExponencialContinua(c,omg,r, rango):
    pass


def graph_CosenoExponencialDiscreta(c,omg,r, rango):
    pass


def main ():
    #graph_ExponencialContinuo(1,(-100,100))
    #graph_SenoidalContinua(1,mat.pi*2,0,(0,6))

    graph_EscalonContinuo((-100,100))
    plt.show()

main()
