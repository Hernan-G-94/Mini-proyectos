class persona():
    def __init__(self, nombre,edad,nacionalidad,localidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.localidad = localidad

    def mostrar_info(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}, nacionalidad: {self.nacionalidad}, localidad: {self.localidad}")

    
