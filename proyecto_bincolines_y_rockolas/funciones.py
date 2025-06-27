def borrarpantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()

def menu_principal():
    print("\n\t\t🎪 Brincolines y Rockolas 🎶")
    print("\t\t------------------------------")
    print("\t\t 1️⃣  Agregar Brincolines")
    print("\t\t 2️⃣  Mostrar Brincolines")
    print("\t\t 3️⃣  Agregar Rockolas")
    print("\t\t 4️⃣  Mostrar Rockolas")
    print("\t\t 5️⃣  SALIR")
    print("\t\t------------------------------")
    opcion = input("\t\t👉 Elige una opción: ").strip().upper()
    return opcion

def agregar_brincolines(lista):
    borrarpantalla()
    print("👤 Agregar Brincolines")
    nombre = input("📝 Ingresa el nombre del brincolín: ").upper().strip()
    capacidad = input("📝 Ingresa la capacidad del brincolín: ").strip()
    lista.append([nombre, capacidad])
    print("✅ Brincolín agregado con éxito")

def mostrar_brincolines(lista):
    borrarpantalla()
    print("\t\t📋 Mostrar Brincolines")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<20} {'Capacidad':<15}")
        print(f"{'-' * 40}")
        for fila in lista:
            print(f"\t{fila[0]:<20} {fila[1]:<15}")
        print(f"{'-' * 40}")
        print(f"\t\tTotal: {len(lista)} brincolines")
    else:
        print("❌ LISTA VACÍA")

def agregar_rockolas(lista):
    borrarpantalla()
    print("👤 Agregar Rockolas")
    nombre = input("📝 Ingresa el nombre de la rockola: ").upper().strip()
    capacidad = input("📝 Ingresa la capacidad de la rockola: ").strip()
    lista.append([nombre, capacidad])
    print("✅ Rockola agregada con éxito")

def mostrar_rockolas(lista):
    borrarpantalla()
    print("\t\t📋 Mostrar Rockolas")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<20} {'Capacidad':<15}")
        print(f"{'-' * 40}")
        for fila in lista:
            print(f"\t{fila[0]:<20} {fila[1]:<15}")
        print(f"{'-' * 40}")
        print(f"\t\tTotal: {len(lista)} rockolas")
    else:
        print("❌ LISTA VACÍA")

def calcular_promedios(lista):
    borrarpantalla()
    print("Calculo de promedios")
    if len(lista) > 0:
        for fila in lista:
            promedio = sum(fila[1:]) / len(fila[1:])
            print(f"Brincolín/Rockola: {fila[0]}, Promedio de capacidad: {promedio:.2f}")
    else:
        print("❌ No hay datos para calcular promedios")  
