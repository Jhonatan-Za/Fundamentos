#la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.
import datetime

 

def dmaEdad(fecha):

    fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y').date()

    hoy = datetime.date.today()

    meses = ((hoy.year - fecha.year) *12) + (hoy.month - fecha.month)

    print ('Meses = %s' % (meses))


while True:

    dmaEdad(input('Ingrese la fecha de su nacimiento (dd/mm/YYYY): '))