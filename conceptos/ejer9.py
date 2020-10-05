import os
from datetime import date
from datetime import datetime
os.system('cls')

# Mostrar en pantalla la cantidad de meses
# transcurridos desde la fecha de nacimiento de un usuario.
print('Meses transcurridos desde la fecha de nacimiento')
year = int(input("Ingrese año de nacimiento: "))
mont = int(input("Ingrese mes de nacimiento: "))
day = int(input("Ingrese dia de nacimiento: "))

hoy = datetime.now()
fecha = datetime(year,mont,day)
total_dias = (hoy - fecha).days
total_year = total_dias/365
total_mes = total_year*12

print(int(total_mes))


