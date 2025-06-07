# def mod(dividendo, divisor):
#     return dividendo % divisor

# dividendo = 10
# divisor = 2

# print(f"El modulo de {dividendo} y {divisor} es: {mod(dividendo, divisor)}")

# def f(x): # f(x)=x**2 + 3.x + 10
#     return x ** 2 + 3 * x + 10
# print(f(1))

def mod(dividendo, divisor):
    return dividendo % divisor

def calculo(numeros): # numeros = [1,2,3,4,5,6,7,8,9,10]
    pares = []
    impares = []
    for i in numeros:
        modulo = mod(i, 2)
        if modulo == 0:
            pares.append(i)
        else:
            impares.append(i)

    print(f"El numero de pares es : {len(pares)}")
    print(f"El numero de impares es : {len(impares)}")

pares = [32, 65]
impares = [32,54,85,52]

calculo([1,2,3,4,5,6,7,8,9,10,12,14])
print(f"Los numero pares son {pares}")
print(f"Los numero impares son {impares}")
