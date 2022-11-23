
from datetime import datetime
from xmlrpc.client import boolean 


def parse_fecha(cadena):
    fecha = str(datetime.strptime(cadena,'%d/%m/%Y').date())
    return fecha
    #Necesario para crear una función especifica para cambiar el formato de texto para que lea el formato de la fecha.


def parse_lista(cadenas):
    lista = []
    lista_pal = cadenas.split(',')
    for palabra in lista_pal:
        num = str(palabra)
        lista.append(num)
    return lista
    #Creada para evitar algún fallo en la lectura de la descripción, y que salga todo de seguido en el mismo formato.


def parse_bool(cadenass):
    if cadenass == 'Y':
        boolean = True
    else:
        boolean = False
    return boolean
    #Como la co_producción puede existir o no, creamos una función de condicion para que nos detecte si tiene o no.



