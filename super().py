#metodo SUPER()

class Mamifero:
    def __init__(self,nombre):
        print(nombre,"es un animal de sangre caliente")
        
class Leon(Mamifero):
    def __init__(self):
        print("el leon es un animal de cuatro patas")
        
# =============== Cosas que son iguales =======================================
        # super().__init__("Simba")
        
        Mamifero.__init__(self, "Simba")
      
# =============================================================================


nuevo_leon = Leon()

