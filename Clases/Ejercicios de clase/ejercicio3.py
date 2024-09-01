
print("Bienvenido, ingrese una de las opciones")
print(f"\n 1: Fecha de Inscripción del ciclo I 2025"+
      "\n 2: Fecha de Inicio del ciclo I 2025" +
      "\n 3: Fecha de finalización ciclo I 2025" +
      "\n 4: Salir")

while True:
    seleccion = input("Ingrese una opción ").strip()

    if seleccion == "1":
        print("La fecha de inscripción es de 01/01/2025 al 16/01/2025")

    elif seleccion == "2":
        print("La fecha de inicio de ciclo es: 16/01/2025")

    elif seleccion == "3":
        print("La fecha de finalización de ciclo es: 16/06/2025")

    elif seleccion == "4":
        print("Vuelva pronto")
        break
    
    else:
        print("Su selección no es válida")