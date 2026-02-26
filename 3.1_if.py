entrada = float(input("Ingrese un número entre 0 y 10: "))
if entrada == 5: #Condición
    print("Eso es un 5.")
elif entrada > 5: #Segunda condición
    print("El número ", entrada, " es mayor a 5.")
else: #Lo que se hará si no se cumple la segunda condición
    print("El número ", entrada, " es menor a 5.")