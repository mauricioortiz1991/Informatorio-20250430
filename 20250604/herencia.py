# Clase Padre - Abstracto
class Vehiculo():

    def __init__(self, ruedas, modelo, motor, chasis):
        self.ruedas = ruedas
        self.modelo = modelo
        self.motor = motor
        self.chasis = chasis

    def __str__(self):
        return f"Esto es un vehiculo de Ruedas: {self.ruedas} Modelo: {self.modelo} Motor: {self.motor}"
    
    def sonido(self):
        pass

# Clase Hijo

class Auto(Vehiculo):
    def __init__(self, ruedas, modelo, motor, chasis, puertas):
        super().__init__(ruedas, modelo, motor, chasis)
        self.puertas = puertas

    def sonido(self):
        return "PIPIP 🚗"
    
# Clase Hijo

class Moto(Vehiculo):
    def __init__(self, ruedas, modelo, motor, chasis, color):
        super().__init__(ruedas, modelo, motor, chasis)
        self.color = color

    def sonido(self):
        return "PIIP 🏍"

auto_1 = Auto(4, "2024", "V8", "MASDJ-34", 5)

moto_1 = Moto(2, "2022", "103", "MA-4", "Azul")

# print(auto_1.sonido())
# print(moto_1.sonido())

print(auto_1)
print(moto_1)
