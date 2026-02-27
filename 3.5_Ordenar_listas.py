#Ordenar una lista ascendente
lista = []
cambio = True
num = int(input("¿Cuántos elementos deseas ordenar?: ")) #Usuario ingresa la cantidad de número que tendrá la lista

for i in range(num): #Ingreso de los números de la lista
    val = float(input("Ingresa un elemento de la lista: "))
    lista.append(val)

while cambio: #Orden de los número en la lista (ascendente)
    cambio = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            cambio = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nOrdenada:")
print(lista) #Imprimimos la lista ordenada
#sort para que ordenar la lista de forma sencilla
my_list = [11, 1, 6, 2, 5]
my_list.sort()
#.reverse() las ordenaría en sentido contrario
print(my_list)