import sys

### leer la matriz numerica de una imagen guardada como archivo de texto
def ReadMatrix(RutaArchiTexto):

    ### leer todo el archivo
    TextoMatriz = open(RutaArchiTexto, "r")

    ### leer todos los valores numericos restantes
    NumVals = TextoMatriz.read().split('\n')

    TextoMatriz.close()

    return NumVals
 
### cambiar el valor de los pixeles segun la transformacion lineal
def LinealTransform( vectInt ):

    intencidadSalida = []

    for linea in vectInt:
        lineaPura = linea.split(' ')
        for numero in lineaPura:
            intencidadSalida.append( int(numero) + 1 )

    return intencidadSalida 

## escribir en un archivo de texto la matriz tranformada
def EscribirMatrizNumerica ( NombreArchivo, VectorSalida ):
    escritor  = open(NombreArchivo+"Trans.txt", "w")
    for numero in VectorSalida:
        escritor.write( str(numero)+' ')
    escritor.close()



nombre = 'read1.txt'
nomCor = nombre.split('.')
intencidadesEntrad = ReadMatrix(nombre)
intencidadesSalida = LinealTransform(intencidadesEntrad)
EscribirMatrizNumerica(nomCor[0], intencidadesSalida)