var = 2 #variable
num = 1.010345 #variable a redondear
var2 = "String" #variable que contiene una cadena
print("Valor original de la variable: ", var) #Necesita la coma, de lo contrario hay error
var **= 2 #abreviación de operaciones
print("Nuevo valor de la variable:", var)
print("Número orginal:", num, "\nNúmero redondeado:", round(num, 2), sep=" ") #Redondeamos num dentro del print, usando round
print("Cadena: " + var2) #Si tenemos una variable que contiene una cadena, podemos imprimirla  en el mismo print usando +