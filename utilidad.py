import json



#se crea un diccionrio que va a contener todos los 
#productos que ingresarán.
productos = {}


            
#crearemos una funcion para realizar el registro de los productos.
def ingresar_prod():
    nombre = input("Ingrese nombre del producto: ")
    categoria = input("Ingrese categoria del producto: ")
    precio = input("ingrese precio del producto: ")

    productos = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria
    }

    print("se han ingresado correctamente")  


def listar_prod():
    if not productos:
        print("no hay productos ingresados")
    else:
        for info in productos.items():
            print("")
            print(f" nombre: {info['nombre']}")
            print(f" precio: {info['precio']}")
            print(f" categoria: {info['categoria']}")
            print("")











#creamos una funcion para crear las opciones del menu que aparecera al usuario en pantalla
def menu():
    while True:
        print("--- MENU TIENDA ---")
        print("1) Registrar producto")
        print("2) Listar todos los productos")
        print("3) Buscar producto por categoria")
        print("4) Precio promedio de los productos")
        print("5) Salir del programa y guardar")

    
        opcion = int(input("Favor seleccione una opción"))
        if opcion == 1:
            ingresar_prod()
        elif opcion == 2:
            listar_prod()
        elif opcion == 3:
            print("3")
        elif opcion ==4:
            print("4")
        elif opcion ==5:
            print("5")
            with open("archivo.txt","a") as file:
                json.dump(productos, file, indent=4)
            break
        else:
            print("Favor de escribir opcion de 1 a 5")


                        

            






    