print("hi there")

is_this_a_tutorial = True

""" if (is_this_a_tutorial == True):
    print("yes")
else:
    print("no") """



def contar_traducciones_iguales2(ingles: dict, aleman: dict) -> int:
    contador: int = 0
    for k in aleman:
        for j in ingles:
            if aleman[k] == ingles[j]:
                contador += 1
    return contador

