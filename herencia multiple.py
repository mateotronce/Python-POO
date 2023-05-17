#herencia multiple

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando...")
    def ocupado(self):
        print("ocupado")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("tomando fotos")
        
class Reproducir:
    def __init__(self):
        pass
    def Musica(self):
        print("reproduciendo musica")
    def video(self):
        print("reproduciendo video")
    
        
class smartphone(Telefono,Camara,Reproducir):
    def __del__(self):
        print("Telefono apagado")
        
        
movil = smartphone()

print(movil.llamar() )