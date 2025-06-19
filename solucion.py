
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}


def turistas_por_pais(turistas):
    paises = {}
    for id, datos in turistas.items():
        nombre, pais, _ = datos
        if pais not in paises:
            paises[pais] = []
        paises[pais].append((id, nombre))
    
    print("\n*** Turistas por país ***")
    for pais, lista in paises.items():
        print(f"\n{pais}:")
        for id, nombre in lista:
            print(f"  ID: {id} - Nombre: {nombre}")


def turistas_por_mes(turistas):
    mes = input("Ingrese el número del mes (01 a 12): ")
    print(f"\n*** Turistas que ingresaron en el mes {mes} ***")
    encontrados = False
    for id, datos in turistas.items():
        nombre, pais, fecha = datos
        if fecha[3:5] == mes:
            print(f"ID: {id} - Nombre: {nombre} - País: {pais} - Fecha: {fecha}")
            encontrados = True
    if not encontrados:
        print("No se encontraron turistas para ese mes.")


def eliminar_turista(turistas):
    id = input("Ingrese el ID del turista a eliminar: ")
    if id in turistas:
        print(f"Eliminando turista: {turistas[id][0]}")
        del turistas[id]
    else:
        print("ID no encontrado.")


def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turistas por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            turistas_por_pais(turistas)
        elif opcion == "2":
            turistas_por_mes(turistas)
        elif opcion == "3":
            eliminar_turista(turistas)
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opción no valida")


main()
