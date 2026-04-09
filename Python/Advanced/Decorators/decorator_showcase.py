def decorator_function(function):
    def wrapper():
        print("Ingresá tus números a sumar:\n")
        a = input()
        b = input()

        function()


@decorator_function
def add(a, b):
    resultado = a + b


add()