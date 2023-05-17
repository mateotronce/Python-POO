#Polimorfismo con herencia

class Aves:
    def volar(self):
        print("la mayoria de las aves pueden volar pero algunas no")
        
class Aguila(Aves):
    def volar(self):
        print("las aguilas pueden volar")
        
class Gallina(Aves):
    def volar(self):
        print("la gallina no puede volar")
        
        
obj_ave,obj_gallina = Aves(),Gallina()


obj_ave.volar() 
obj_gallina.volar()