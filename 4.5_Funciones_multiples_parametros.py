valor = ""

def imc(peso, altura): #definimos función con múltiples parámetros
    return (peso / altura ** 2) #* 10000

def estado(imc):
    global valor
    if imc < 18.5:
        valor = "peso bajo"
    elif imc <= 24.9:
        valor = "peso normal"
    elif imc <= 29.9:
        valor = "sobrepeso"
    elif imc <= 34.9:
        valor = "obesidad I"
    elif imc <= 39.9:
        valor = "obesidad II"
    else:
        valor = "Obesidad III"
    return round(imc, 2)
 
peso = float(input("Dime tu peso en kg: "))
altura = float(input("Dime tu altura en metros: "))
print("\nTu imc es:", estado(imc(peso, altura)), "\nTienes", valor)
