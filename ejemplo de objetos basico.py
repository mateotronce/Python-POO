#clase que represeta una persona

class Persona:
    "clase que representa una persona"
    pass
    "estos son los atributos"
    cedula = "V-26938401"
    nombre = "Leonardo"
    apellido = "Caballero"
    sexo = "masculino"
    "estos son los metodos"
    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje
    
macagua = Persona
"Atributos"

print(type(macagua),
dir(macagua),
macagua.cedula,
macagua.nombre,
macagua.apellido,
macagua.sexo)

"""""si el nombre de un atributo esta entre doble _ estonces es
un atributo espercial"""

"""
__name__, describe el nombre del objeto o del método.
"""
print(macagua.__name__)

"""
__doc__, contiene la documentación de un módulo, una clase, o método especifico, escrita en el formato docstrings.
"""
print(macagua.__doc__)

"Metodos"