### funciones especiales que se pueden usar a parti de otras funciones
def Cuadrado (n):
    """ eleva un numero n a un numero m """
    return n**2

def Par(n):
    """ verificar si un numero es par """
    if n % 2 == 0:
        return n

def suma ( x, y):
    return x+y

lin = (1,2,3,4,5,6)
lout = map(Cuadrado,lin)

print lout

lin2 = (1,2,3,4,5,6,7,8,9)
lout2 = filter(Par,lin2)
print lout2

lin3 = (1,2,3,4,5,6)
lout3 = reduce(suma,lin3)

print lout3


    ### compresion de listas ###
l = [1,2,3,4,5,6,6]
lsc = [ n ** 2 for n in l ]
print lsc



    ### generadores
for n in  ( n ** 2 for n in l ) :
    print n

    ## funcion generador
def generador ( n , m ):
    i = n
    while i <= m :
        yield i
        i += 1

x = generador(1,10)
for n in x :
    print n
