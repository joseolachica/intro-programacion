def dibujar_rectangulo(altura, ancho):
    for i in range(altura):
        for j in range(ancho):
            print("*", end="")
        print()

def obtener_entrada_usuario():
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))
    return altura, ancho


altura, ancho = obtener_entrada_usuario()


dibujar_rectangulo(altura, ancho)
    
