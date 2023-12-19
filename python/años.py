import datetime

def calcular_edad(fecha_nacimiento):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.datetime.now()

    # Verificar si el cumpleaños ya ha ocurrido este año
    if (fecha_actual.month, fecha_actual.day) >= (fecha_nacimiento.month, fecha_nacimiento.day):
        edad = fecha_actual.year - fecha_nacimiento.year
    else:
        edad = fecha_actual.year - fecha_nacimiento.year - 1

    return edad

# Solicitar la fecha de nacimiento al usuario
while True:
    try:
        fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
        break
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, ingresa la fecha en el formato correcto.")

# Calcular la edad del usuario
edad_usuario = calcular_edad(fecha_nacimiento)

# Mostrar la edad del usuario
print("Tu edad es:", edad_usuario, "años.")
