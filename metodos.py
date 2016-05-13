    #### revizando los metodos de las structuras principales
    # diccionarios

D = {1:"alfredo", 2:"aldo", 3:"alberto",4:"angel"}
print D.has_key(9)
print D.items()
print D.keys()
##print D.pop(1)

#lista = [1,2]
#print D.pop(1[0,1])
print D.values()
print D

    # cadenas
cadena = "esta es una cadena de prueba esta cadena es una prueba"
print cadena.count('esta')
print cadena.find('una')
print cadena.partition(',')
print cadena.replace('e', 'E')
print cadena
print cadena.split(' ')

    # listas
lst = [1,2,3,4,5,6,7,8]
print lst.append(1)
print lst
print lst.count(1)
print lst.index(4)
print lst.insert(3,12)
print lst
print lst.pop(3)
print lst.pop()
print lst.pop()
print lst.pop()
print lst
it = [1,'3',1,"cadena"]
print lst.extend(it)
#lst.append(1,'3',1,"cadena")
lst.remove("cadena")
print lst
lst.reverse()
print lst
lst.sort(reverse=True)
print lst
