#polimorfismo por funcion

class Tomate:
    def tipo(self):
        print("Fruta")
    def color(self):
        print("rojo")
    
class Banana:
    def tipo(self):
        print("Fruta")
    def color(self):
        print("amarillo")
        
def funcion(objeto):
    objeto.tipo()
    objeto.color()
    
nuevo_tomate = Tomate()

funcion(nuevo_tomate)

nuevo_banana = Banana()

funcion(nuevo_banana)