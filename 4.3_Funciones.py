lista = [1, 4, 10]
verificar = False 
num = None

def esta_en_lista(num, verificar): #Definimos una función dentro de nuestro código, así evitamos repetir las mismas líneas de código
    if num in lista:
        print(num, "estaba en la lista. \nAcertaste.")
        verificar = True
        return verificar
    else:
        print(num, "no estaba en la lista.")
        return verificar
 
print("Hay una lista con números secretos, del 0 al 10, incluyendo esos dos. ¿Puedes adivinar alguno?")
while verificar == False:
    num = int(input("Dime un número..."))
    verificar = esta_en_lista(num, verificar)
