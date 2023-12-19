horaactual= int(input("ingrese la hora actual : "))
cantidad_de_horas= int(input("ingrese las cantidades de horas: "))
cantidad_de_horas = (horaactual + cantidad_de_horas) %  24
print("En " + str(horaactual)+ "horas, el reloj marcara las " + str(cantidad_de_horas))
    
     

