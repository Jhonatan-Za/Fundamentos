#Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta es de 50 cm
Diametro = 50 
Recorrido = 100000
pi = 3.1416
print('Primero debemos encontrar la longitud de la llanta, cuanto recorre por cada vuelta.')
lon = pi * Diametro
print ('En cada vuelta recorre',(lon))
A = lon / Recorrido
print (A)
V = 1/A
print ('El numero de vueltas que da la llanta es de:',round(V))