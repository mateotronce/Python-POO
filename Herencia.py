#Herencia

"""
class NombrSubClase (NombreClaseSuperior)

class ClaseBase:
    Cuerpo de la clase base
    
class DerivadoClase(ClaseBase):
    Cuerpo de clase derivada
    
"""
class pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return "{} es del tipo {}".format(self.nombre,self.tipo)
    
class pikachu(pokemon):
    def ataque(self,ataque):
        return "{} tipo de ataque {}".format(self.nombre,ataque)
    
class charmander(pokemon):
   def ataque(self,ataque):
       return "{} tipo de ataque {}".format(self.nombre,ataque)


nuevo_pokemon = pikachu("jose","electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impctrueno"))