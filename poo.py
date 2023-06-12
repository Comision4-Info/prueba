class Titular:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuit = None

    def __get_cuit(self):
        return self.__cuit

    def __set_cuit(self,cuit):
        if len(cuit) >=10:
            self.__cuit = cuit
        else:
            print('El cuit ingresado no es correcto')

class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
        self.__cuit = None

    def __get_cuit(self):
        return self.__cuit

    def __set_cuit(self,cuit):
        if len(cuit) >=10:
            self.__cuit = cuit
        else:
            print('El cuit ingresado no es correcto')


class CuentaBancaria(Titular,Banco):
    def __init__(self, nombre_titular,apellido_titular,edad,nombre_banco,saldo=0):
        super().__init__(nombre_titular,apellido_titular,edad)
        Banco.__init__(self,nombre_banco)
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente.")



# Ejemplo de uso
cuenta1 = CuentaBancaria('Juan','Perez',30,'Hipotecario',5000)
cuenta1._Banco__set_cuit('1111111111')
cuenta1._Titular__set_cuit('2222222222')
print(cuenta1._Banco__get_cuit())
print(cuenta1._Titular__get_cuit())
'''print(f"Saldo inicial: {cuenta1.saldo}")
cuenta1.depositar(100)
print(f"Saldo después de depositar: {cuenta1.saldo}")
cuenta1.retirar(50)
print(f"Saldo después de retirar: {cuenta1.saldo}")'''

class Persona:

    def __str__(self):
        return 'Hola soy una persona'

class Empleado(Persona):

    def __str__(self):
        return super().__str__() + ' y soy empleado'

persona1 = Persona()
empleado = Empleado()
print(persona1)
print(empleado)