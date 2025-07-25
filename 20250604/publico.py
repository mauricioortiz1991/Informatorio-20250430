class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def mostrar_nombre(self):
        return self.__nombre
    
persona = Persona("Juan")
# print(persona._nombre)
# print(persona._Persona_nombre)
nombre = persona.mostrar_nombre()
print(nombre)
