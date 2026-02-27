#Listas, en este caso numbers contiene 5 enteros
numbers = [10, 5, 7, 2, 1]
print("Contenido original de la lista:", numbers)
numbers[0] = numbers[4] #Cambiamos el primer número, ahora es igual al 5to
print("Nuevo contenido de la lista:", numbers)
print("Longitud de la lista:", len(numbers))  #Así imprimimos la longitud de la lista
del numbers[1] #Eliminamos el 2do número de la lista
print("\nNueva longitud:", len(numbers)) #Imprimimos la nueva longitud y luego la lista
print("Nueva lista:", numbers)
print(numbers[-1]) #Mostrará el último número de la lista
print(numbers[-2]) #Mostrará eñ anterior al último (penúltimo)
print("Vamos a cambiar el último número de la lista:")
numbers[-1] = int(input("Dime un número entero...")) #Pedimos el que será el nuevo último número de la lista
print(numbers)
#append añade un nuevo elemento al final de la lista
numbers.append(int(input("Dime un número entero para añadirlo a la lista...")))
print("Nueva lista:", numbers, "\nVamos a añadir un número entero, en cualquier posición de la lista:")
#insert añade un nuevo elemento en la posición que queramos
numbers.insert(int(input("¿En que posición? 0, 1, 2, 3 o 4 ")), int(input("¿Qué número? ")))
print("Nueva lista:", numbers)