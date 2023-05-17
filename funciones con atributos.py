#funciones para atributos

class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Argentina"
    
doctor = Persona()
"""
print("la edad es: ", doctor.edad)

print("la edad es: ", getattr(doctor,"edad"))
"""

"""
obtener una valor
print("el doctor tiene una edad?", hasattr(doctor,"edad"))
print("el doctor tiene una edad?", hasattr(doctor,"apellido"))
"""

"""
modificar un valor
print("Antes tenia: ", doctor.edad)
setattr(doctor,"edad", 30)
print("Ahora tiene: ",doctor.edad)
"""

"""
eliminar un atributo
delattr(Persona,"pais")
"""
