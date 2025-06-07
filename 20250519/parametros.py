# def prueba_parametros(nombre, it_obj, dic_obj, mensaje="Hola"):
#     print(f"{mensaje} {nombre}")

#     for i in it_obj:
#         print(f"Imprimiendo cada elemento de *it_obj : {i}")

#     for k, v in dic_obj.items():
#         print(f"Imprimiendo cada elemento de *dic_obj: {k}:{v}")

# prueba_parametros("Lucas", [1,2,3,4,5], {1: 'uno', 2: 'dos', 3: 'tres',})

def prueba_parametros(nombre, mensaje="Hola", *it_obj, **dic_obj):
    print(f"{mensaje} {nombre}")

    for i in it_obj:
        print(f"Imprimiendo cada elemento de *it_obj : {i}")

    for k, v in dic_obj.items():
        print(f"Imprimiendo cada elemento de *dic_obj: {k}:{v}")

prueba_parametros("Lucas", "Hola", 1, 2, 3, 4, 5, a='uno', b='dos', c='tres')
