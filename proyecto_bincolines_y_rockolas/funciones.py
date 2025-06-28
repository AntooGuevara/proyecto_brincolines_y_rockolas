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
    print("\t\t 5️⃣  Eliminar Datos")
    print("\t\t 6️⃣  Modificar Disponibilidad")
    print("\t\t 7️⃣  Salir")
    print("\t\t------------------------------")
    opcion = input("\t\t👉 Elige una opción: ").strip().upper()
    return opcion

def agregar_brincolines(lista):
    borrarpantalla()
    print("👤 Agregar Brincolines")
    nombre = input("📝 Ingresa el nombre del brincolín: ").upper().strip()
    capacidad = input("📝 Ingresa la capacidad del brincolín: ").strip()
    estado = "DISPONIBLE"
    lista.append([nombre, capacidad, estado])
    print("✅ Brincolín agregado con éxito")


def mostrar_brincolines(lista):
    borrarpantalla()
    print("\t\t📋 Mostrar Brincolines")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<20} {'Capacidad':<15} {'Disponibilidad':<15}")
        print(f"{'-' * 50}")
        for fila in lista:
            print(f"\t{fila[0]:<20} {fila[1]:<15} {fila[2]:<15}")
        print(f"{'-' * 50}")
        print(f"\t\tTotal: {len(lista)} brincolines")
    else:
        print("❌ LISTA VACÍA")


def agregar_rockolas(lista):
    borrarpantalla()
    print("👤 Agregar Rockolas")
    nombre = input("📝 Ingresa el nombre de la rockola: ").upper().strip()
    capacidad = input("📝 Ingresa la capacidad de la rockola: ").strip()
    estado = "DISPONIBLE"
    lista.append([nombre, capacidad, estado])
    print("✅ Rockola agregada con éxito")

def mostrar_rockolas(lista):
    borrarpantalla()
    print("\t\t📋 Mostrar Rockolas")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<20} {'Capacidad':<15} {'Disponibilidad':<15}")
        print(f"{'-' * 50}")
        for fila in lista:
            print(f"\t{fila[0]:<20} {fila[1]:<15} {fila[2]:<15}")
        print(f"{'-' * 50}")
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

def eliminar_datos(lista_brincolines, lista_rockolas):
    borrarpantalla()
    print("🗑️ Eliminar Datos")
    if len(lista_brincolines) > 0 or len(lista_rockolas) > 0:
        print("1️⃣ Eliminar Brincolines")
        print("2️⃣ Eliminar Rockolas")
        print("3️⃣ Eliminar Todo")
        opcion = input("👉 Elige una opción: ").strip()
        
        if opcion == "1":
            lista_brincolines.clear()
            print("✅ Todos los brincolines han sido eliminados.")
        elif opcion == "2":
            lista_rockolas.clear()
            print("✅ Todas las rockolas han sido eliminadas.")
        elif opcion == "3":
            lista_brincolines.clear()
            lista_rockolas.clear()
            print("✅ Todos los datos han sido eliminados.")
        else:
            print("❌ Opción no válida.")
    else:
        print("❌ No hay datos para eliminar.")
        
def modificar_disponibilidad(lista_brincolines, lista_rockolas):
    borrarpantalla()
    print("🔄 Modificar Disponibilidad")
    if len(lista_brincolines) > 0 or len(lista_rockolas) > 0:
        print("1️⃣ Modificar Brincolines")
        print("2️⃣ Modificar Rockolas")
        opcion = input("👉 Elige una opción: ").strip()
        
        if opcion == "1":
            nombre = input("📝 Ingresa el nombre del brincolín a modificar: ").upper().strip()
            for brincolin in lista_brincolines:
                if brincolin[0] == nombre:
                    while True:
                         nuevo_estado = input("📝 Ingresa el nuevo estado (DISPONIBLE/NO DISPONIBLE): ").upper().strip()
                         if nuevo_estado in ["DISPONIBLE", "NO DISPONIBLE"]:
                          break
                         else:
                            print("❌ Solo se permite 'DISPONIBLE' o 'NO DISPONIBLE'. Intenta de nuevo.")

                    brincolin[2] = nuevo_estado
                    print(f"✅ Estado del brincolín '{nombre}' modificado a '{nuevo_estado}'.")
                    return
            print(f"❌ Brincolín '{nombre}' no encontrado.")
        elif opcion == "2":
            nombre = input("📝 Ingresa el nombre de la rockola a modificar: ").upper().strip()
            for rockola in lista_rockolas:
                if rockola[0] == nombre:
                     while True:
                         nuevo_estado = input("📝 Ingresa el nuevo estado (DISPONIBLE/NO DISPONIBLE): ").upper().strip()
                         if nuevo_estado in ["DISPONIBLE", "NO DISPONIBLE"]:
                          break
                         else:
                            print("❌ Solo se permite 'DISPONIBLE' o 'NO DISPONIBLE'. Intenta de nuevo.")
                rockola[2] = nuevo_estado
                print(f"✅ Estado de la rockola '{nombre}' modificado a '{nuevo_estado}'.")
                return
            print(f"❌ Rockola '{nombre}' no encontrada.")
        else:
            print("❌ Opción no válida.")
    else:
        print("❌ No hay datos para modificar.")
