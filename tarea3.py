# Verificar si un numero es positvo y de 4 digitos

print("---------------------------------")
print("-----Positivo y de 4 digitos-----")
print("---------------------------------")

# input

a = int(input("Digite el número: "))

# processing and output

if a > 0 and a >= 1000 and a <= 9999:
    print("El número tiene cuatro digitos y es positivo")
else:
    print("El número no cumple con las condiciones")
   

print("---------------------------------")