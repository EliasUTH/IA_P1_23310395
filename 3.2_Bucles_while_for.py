var = ""
word_without_vowels = ""
print("_Devorador de vocales_") #Función del código
while var != "n": #Mientras la condición se cumpla seguirá dentro del bucle
    user_word = input("Ingrese una palabra... ")
    user_word = user_word.upper() #La palabra ingresada pasa a mayúsculas
    for letter in user_word:
        if letter == 'A':
            continue
        elif letter == 'E':
            continue
        elif letter == 'I':
            continue
        elif letter == 'O':
            continue
        elif letter == 'U':
            continue
        else: 
            word_without_vowels += letter
    print(word_without_vowels)
    word_without_vowels = ""
    var = input("¿Continuamos? Escribe s para continuar, n para salir.")
    if var != 's' and var !='n': #And equivalente a &&
        print("De esa no hay.")
        continue
print("Hasta luego.")
# También podemos usar un else después de un bucle, ya sea for o while