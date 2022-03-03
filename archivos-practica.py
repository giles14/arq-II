def main():
    import pickle
    print("Contactos")

    ### Modifica desde aquí, para que al correr el programa en vez de usar el archivo binario pickle, obtenga la lista de mascotas desde el arhivo de texto que previamente creaste 
    # Recuerda que, deberás usar la forma apropiada de lectura de archivo según corresponda: r, w, x, etc.
    # deberás de llenar la variable mascotas con los elementos que cargaste desde el documento de texto

    # Obtiene la Lista de mascotas
    mascotas = pickle.load(open( "todo.pickle", "rb" ))
   
    choice = 0
    while choice != 4:
        print("\n Seleccione la opción correspondiente \n")
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

    ### Modifica desde aquí para que al cerrar usando la opción 4 en vez de guardar un archivo Binario lo guarde en un archivo de texto separado por comas,
    # Recuerda que a diferencia del arhivo binario pickle, cuando se graba un archivo en un documento de texto, este se irá añadiendo línea por línea
    # Por lo que deberás usar un iterador y un marcador de fin de línea "/n" para delimitar cada mascota.
    pickle_file = open('todo.pickle', 'wb')
    pickle.dump(mascotas, pickle_file)
    ### Modifica hasta aquí
main()