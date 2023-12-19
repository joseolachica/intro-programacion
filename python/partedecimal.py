# Solicitar al usuario que ingrese un número real
numero_real = float(input("Ingrese un número real: "))

# Obtener la parte decimal utilizando el operador %
parte_decimal = numero_real % 1

# Mostrar la parte decimal
print("La parte decimal de  "+str(numero_real) +"es: " +str(parte_decimal))
