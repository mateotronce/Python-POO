#ejercicio de herencia

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
        
    def ingresardato(self):
        self.datos = [int(input("ingresar datos " +str(i+1) + "=")) for i in range(self.n)]


class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
       a,b = self.datos
       s = a + b
       print("el resultado es: ", s)
       
    def resta(self):
       a,b = self.datos
       r = a - b
       print("el resultado es: ", r)
       
       
class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a = self.datos[0]
        print("el resultado es", math.sqrt(a) )
    
objeto = op_basicas()

# Me sirve para ver si tiene herencia de la funcion que le di
#print(isinstance(objeto,op_basicas))

#me sirve para comprobar la herencia de la clase
#op_basicas es una clase hijo y Calculadora es una clase padre
#print(issubclass(op_basicas,Calculadora)) 



