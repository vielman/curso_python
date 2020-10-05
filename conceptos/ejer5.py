import os
os.system('cls')
#Calcular la cantidad de segundos que le toma a la luz viajar 
# del sol a Marte y mostrar el resultado en pantalla.

print('Cantidad de segundos que le toma a la luz viajar del sol a Marte')
print('Afelio: punto de la órbita más alejado del Sol.')
print('Perihelio: punto de la órbita más próximo al Sol.')
print('En el afelio Marte se encuentra a 249,1 millones de km del Sol.')
print('En el perihelio Marte se encuentra a 206,7 millones de km del Sol')
print('Velocidad de la Luz 300.000 Km por segundos')

afelio = 249100000
perihelio = 206700000
luz = 300000
afelio_tiempo = afelio / luz
perihelio_tiempo = perihelio / luz

print('Tiempo en Afelio: ', afelio_tiempo)
print('Tiempo en Perihelio ', perihelio_tiempo)