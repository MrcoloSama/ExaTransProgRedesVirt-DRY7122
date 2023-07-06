integrantes = [
    "Marco Hernandez",
    "Diego Zuñiga",
    # Agrega los nombres y apellidos de los integrantes del grupo aquí
]

def mostrar_integrantes():
    for integrante in integrantes:
        print(integrante)

while True:
    opcion = input("Ingrese una opción ('integrantes' para mostrar la lista, 'salir' para terminar): ")
    
    if opcion.lower() == "integrantes":
        mostrar_integrantes()
    elif opcion.lower() == "salir":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

