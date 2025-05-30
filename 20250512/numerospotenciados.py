# Crear una lista nueva con los elementos potenciados por si mismos
# 0 ** 0, 4 ** 4...
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# numeros_potenciados = [x ** x for x in numbers]
# print(numeros_potenciados)

# numeros_potenciados = [pow(x, x) for x in numbers]
# print(numeros_potenciados)

lenguajes_p = ['java', 'python', 'go', 'rust']
len_corregidas = [leng[0].upper() + leng[1::] for leng in lenguajes_p]
print(len_corregidas)