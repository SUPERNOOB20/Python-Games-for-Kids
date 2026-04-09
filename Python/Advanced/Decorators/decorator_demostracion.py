def decorator_function(function):
    def wrapper():
        print("Ingresá tus números (sin coma) a sumar:\n")
        a = int(input())
        b = int(input())

        resultado_funcion_envuelta = function(a, b)

        print("El resultado es:", resultado_funcion_envuelta)

    return wrapper


@decorator_function
def add(a, b):
    return a + b


add()