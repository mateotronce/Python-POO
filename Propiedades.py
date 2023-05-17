#propiedades()

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre 
        self.__salario = salario
   #esto te da el nombre
    def getnombre(self):
        return self.__nombre
    def getsalario(self):
        return self.__salario
    #definis un nombre para la variable
    def setnombre(self,nombre):
        self.__nombre = nombre
    def setsalario(self,salario):
        self.__salario = salario
    #borras el nombre    
    def delnombre(self):
        del self.__nombre
    def delsalario(self):
        del self.__salario
        
        
empleado_1 = Empleado("Juan", 1000)
print(empleado_1.getnombre(), " gana ", empleado_1.getsalario())

empleado_1.setnombre("raul")
print(empleado_1.getnombre(), " gana ", empleado_1.getsalario())

empleado_1.setsalario(2000)
print(empleado_1.getnombre(), " gana ", empleado_1.getsalario())

empleado_1.delnombre()
print("empleado_1.getnombre()", " gana ", empleado_1.getsalario())

