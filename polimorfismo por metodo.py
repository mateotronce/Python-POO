#polimorfismo con metodo

class Colombia:
    def Capital(self):
        print("Bogota")
    def Idioma(self):
        print("Español")
        
class Argentina:
    def Capital(self):
        print("Buenos Aires")
    def Idioma(self):
        print("Español")
        
colombiano = Colombia()
argentina = Argentina()

for pais in (colombiano,argentina):
    pais.Capital()	
    pais.Idioma()