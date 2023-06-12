#Programación estructurada
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

# Programación Orientada a Objetos

class Inmueble():

    def __init__(self,metros,habitaciones,garaje,zona,estado):
        self.__año = None
        self.metros = metros
        self.habitaciones = habitaciones
        self.garaje = garaje
        self.zona = zona
        self.estado = estado

    def __str__(self):
        return f"Año: {self.__año}\nMetros: {self.metros}\nHabitaciones: {self.habitaciones}\nGaraje: {self.garaje}\nZona: {self.zona}\nEstado: {self.estado}"
    
    def set_año(self,año):
        if año >= 2000:
            self.__año = año
        else:
            print('El año es menor a 2000')

inmueble1 = Inmueble(150,4,True,'C','Disponible')
inmueble2 = Inmueble(150,4,True,'C','Disponible')
inmueble1.set_año(2005)
print(inmueble1)