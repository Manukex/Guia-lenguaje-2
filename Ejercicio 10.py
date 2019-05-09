a = int(raw_input("Ingrese un numero par: "))
b = a/2
int(raw_input("Ingrese un numero impar"))  
if b % 2 != 0:    # Comprobamos que la mitad del numero ingresado sea impar
    print a, "es el doble de ", b, " que es impar"
raw_input()