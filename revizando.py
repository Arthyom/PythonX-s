### revizando los metodos de las clases
    # diccionarios
D = { 1:'1' , 2 :'2', 3:'3', 4:'4'}
print D.has_key(1)
print D.keys()
print D.values()
print D.items()
#print D.remove(1)
print D.pop(2)
print D.popitem()

    #  cadenas
cad = "esta es una cadena de entrada heha para probar algunas cuestines importat"
print cad.count('e')
print cad.find('e')
print cad.partition(' ')
print cad.index('e')
print cad.replace('e','O')
print cad.split(' ')

    # listas
lista = [1,2,3,'esta', "sta es una lista "]
print lista.index(1)
print lista.count(1)
it = ["uno", "dos","tres"]
lista.extend(it)
print lista
lista.append('cien')
print lista
lista.remove('esta')
print lista
lista.insert(1,"esta es una sopa")
print lista
lista.pop(1)
lista.pop(2)
lista.pop(0)
print lista
lista.remove('cien')
print lista
