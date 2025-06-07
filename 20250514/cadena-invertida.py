# Se ingresa por pantalla una cadena y se debe invertirla.
# No se puede usar [::-1] ni reverse.
# Si la palabra que se ingreso es capicua/polidromo.

cadena = input('Ingrese una palabra u oracion:')
invertida = ""
# Hola
# h
# inverida = h(letra) + ''(invertida)
# o
# inverida = o(letra) + h(invertida)
# l
# inverida = l(letra) + oh(invertida)
# o
# # inverida = a(letra) + loh(invertida)

for letra in cadena:
    invertida = letra + invertida

print(f"La cadena invertida se ve como: {invertida}")

if (invertida == cadena):
    print(f"La palabra {cadena} es capicua/polidromo")
else:
    print(f"La palabra {cadena} NO es capicua/polidromo")
