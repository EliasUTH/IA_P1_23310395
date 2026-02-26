#and, or, not
#operaciones bit a bit & (conjuncion), | (disyuncion), ~ (negacion), ^ (xor), y tienen abreviacion
print("((x == y) and (x == y)) or not(x == y)")
x = input("Dame un valor para x, 1 o 0...")
y = input("Dame un valor para y, 1 o 0...")
z = ((x == y) and (x == y)) or not(x == y)
print(z)