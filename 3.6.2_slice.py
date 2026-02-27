# Copiando la lista completa.
list_1 = [1] #Lista original 1
list_2 = list_1[:] #Copiamos lista original 1
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2] #Lista original 2
new_list = my_list[1:3] #Copiamos lista original 2, solo posiciones 1 y 2
#El primer elemento si va incluido en la rebanada, el último no
list_1[0] = 2
print(new_list)