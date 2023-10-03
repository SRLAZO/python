import numpy as np

#CREAR UN ARRAY UNIDIMENCIONAL DE CEROS
array = np.zeros(3)

#print(array)

#----------------------------------------------------------------------------
#CREAR ARRAY BIDIMENCIONAL DE CEROS
array = np.zeros([3,3])
#print(array)


#----------------------------------------------------------------------------
#CREAR ARRAY DE UNOS
array = np.ones([3,3])
#print(array)

#----------------------------------------------------------------------------
#ARRAY DE IDENTIDAD
array = np.eye(3)
#print(array)

#----------------------------------------------------------------------------
#ARRAY DE RANGOS

##Rango de 0 a 4
array = np.arange(4)
#print(array)

##Rango de 0 a 4 decimal
array = np.arange(4.)
#print(array)

##Rango de -3 a 4
array = np.arange(-3, 4)
#print(array)

##Rango de 20 numeros a partir de 0 cada 5 numeros
array = np.arange(0, 20, 5)
print(array)