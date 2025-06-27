import funciones as f

def main():
    datos_brincolines = []
    datos_rockolas = []
    
    opcion = True
    while opcion:
        f.borrarpantalla()
        opcion = f.menu_principal()
        
        match opcion:
            case "1":
                f.agregar_brincolines(datos_brincolines)
                f.esperartecla()
            case "2":
                f.mostrar_brincolines(datos_brincolines)
                f.esperartecla()
            case "3":
                f.agregar_rockolas(datos_rockolas)
                f.esperartecla()
            case "4":
                f.mostrar_rockolas(datos_rockolas)
                f.esperartecla()
            case "5":
                opcion = False
            case _:
                f.borrarpantalla()
                print("❌ INGRESA UNA OPCIÓN VÁLIDA")
                f.esperartecla()

if __name__ == "__main__":
    main()
