#CLASE Y ESTATICA

class Torta:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
        
    def __repr__(self):
        return f"pastel({self.ingredientes !r})"
        
    @classmethod
    def Torta_chocolate(cls):
        return cls(["Harina","huevo","leche","chocolate"])
        
    @classmethod
    def Torta_vainilla(cls):
         return cls(["]harina","leche","vainilla","huevo"])


print(Torta.Torta_chocolate())