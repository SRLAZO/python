#OPERACIONES BASICAS
import numpy as np

#----------------------------------------------------------------------------

#SUMA
#Dos array
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])

#Los sumamos
#print(arr_1 + arr_2)

#Si no tienen la misma forma no podemos sumarlos
arr_3 = np.array([9, 10])
#print(arr_2 + arr_3) #Devuelve error por no ser equivalentes


#----------------------------------------------------------------------------

#RESTA
#Dos array

#print(arr_2 - arr_1)

#----------------------------------------------------------------------------

#PRODUCTO
#Dos array

print(arr_2 * arr_1)