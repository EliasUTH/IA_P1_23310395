#Para afectar una variable global dentro de una función podemos usar global variable
a = 350
print("La variable a vale:", a)

def modificar():
    global a
    a = int(input("Dime un número entero: "))
    b = 2

modificar()
print("Nuevo valor de la función a:", a)