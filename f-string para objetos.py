#f-string

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return f" hola soy {self.nombre} {self.apellido} y tengo {self.edad}"
    
    
    
nuevo_estudiante = Estudiante("victor","ramon",22)

print(f"{nuevo_estudiant1e}")