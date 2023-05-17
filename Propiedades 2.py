#propiedades() 2

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre 
        self.__salario = salario
   #esto te da el nombre
    def __getnombre(self):
        return self.__nombre
    def __getsalario(self):
        return self.__salario
    #definis un nombre para la variable
    def __setnombre(self,nombre):
        self.__nombre = nombre
    def __setsalario(self,salario):
        self.__salario = salario
    #borrar las cosas    
    def __delnombre(self):
        del self.__nombre
    def __delsalario(self):
        del self.__salario
        
    
    nombre = property(fget=__getnombre,
                      fset=__setnombre,
                      fdel=__delnombre,
                      doc = "soy la propiedad del 'nombre' ")
    
    salario = property(fget=__getsalario)


empleado_1 = Empleado("victor", 2000)

empleado_1.nombre = "sara"
print(empleado_1.nombre,empleado_1.salario)
print(help(empleado_1))