def main():
    print("Contactos")

    # Lista
    mascotas = []

    archivo_recuperar = open("dir-mascotas.txt", "r")
    linea = archivo_recuperar.readline()
    while linea:
        mascotas.append(linea.rstrip("\n").split(","))
        linea = archivo_recuperar.readline()
    archivo_recuperar.close()
    
    choice = 0
    while choice != 4:
        print("Seleccione la opción correspondiente \n")
        print("1. Agregar Mascota")
        print("2. Buscar Mascota")
        print("3. Mostrar todas las mascotas")
        print("4. Quitar y guardar")
        choice = int(input())

        if choice == 1:
            print("Agregar una mascota")
            nombre = input("Agrega nombre de la mascota: ")
            owner = input("Agrega nombre del dueño: ")
            telefono = input("Agrega el teléfono del dueño: ")
            mascotas.append([nombre, owner, telefono])

        elif choice == 2:
            print("Busca una mascota")
            keyword = input("Escribe el término buscado: ")
            for mascota in mascotas:
                if keyword in mascota:
                    print(mascota)
        elif choice == 3:
            print("Mostrando todas las mascotas \n")
            for i in range(len(mascotas)):
                print(mascotas[i])
        elif choice == 4:
            print("Saliendo del programa")
        else:
            print("Respuesta inválida")

    archivo_guardar = open("dir-mascotas.txt" ,"w")
    for mascota in mascotas:
        archivo_guardar.write(",".join(mascota) + "\n")
    archivo_guardar.close()

main()