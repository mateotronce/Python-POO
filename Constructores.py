class Persona:
    pass
    def __init__(self, nombre,año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return "{} tiene {}".format(self.nombre, self.año)
    
    
    def comentario(self, frase):
        return "{} dice {}".format(self.nombre,frase)
    
    
    
    
doctor = Persona("Victor" , 22 )

print(doctor.descripcion())
print(doctor.comentario("la concha de la lora"))