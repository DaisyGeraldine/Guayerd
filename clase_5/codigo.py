#Menu simple que solo muestra la opcion seleccionada
while True:
    print("\n Menu Principal")
    print("1. Primer Opcion")
    print("2. Segunda Opcion")
    print("3. Tercera Opcion")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == '1':
        print("Has seleccionado la Primer Opcion.")
    elif opcion == '2':
        print("Has seleccionado la Segunda Opcion.")
    elif opcion == '3':
        print("Has seleccionado la Tercer Opcion.")
    elif opcion == '4':
        print("Saliendo del menu...")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion del 1 al 4.")
        