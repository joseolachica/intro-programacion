peso =int(input("ingrese su peso:  "))
altura=float(input("ingresa tu altura: "))
edad = int(input("ingresa tu edad "))

imc= peso / (altura*altura)

if edad < 45 and imc < 22.0   :
    print("estas bajo de peso")
if edad <45 and imc >= 22.0 :
   print("medio")
if edad>=45 and imc < 22.0 :
    print("regular")        
if edad >=45 and imc >= 22.0 :
    print ("estas en sobrepeso ")
    
    
print("su indice de masa corporal es : " + str(imc))
