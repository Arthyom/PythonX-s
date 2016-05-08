	# prueba para compilar desde la rpi
class Prueba():

	def __init__(self):
		self.__NumPrueba = 0
		self.__RegPrueba = 'vacio'
		self.__NomPrueba = 'vacio'

	def SetNumber (self,NumPrueba):
		self.__NumPrueba = NumPrueba
	
	def GetNumber (self):
		return self.__NumPrueba
	
	NumeroPrueba =  property(GetNumber, SetNumber)			
	
	### script principal ###
p1 = Prueba()
print( p1.GetNumber() )
