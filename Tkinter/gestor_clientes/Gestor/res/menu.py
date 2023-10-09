import res.database as db
import os
import res.helpers

def iniciar():
    while True:
        res.helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al gestor  ")
        print("========================")
        print("[1] Listar los clientes ")
        print("[2] Buscar un cliente   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el gestor    ")
        print("========================")

        opcion = input("> ")
        res.helpers.limpiar_pantalla()
        if opcion == '1':
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == '2':
            print("Buscando un cliente...\n")
            dni = res.helpers.leer_texto(3,3, "DNI (2 ins y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        if opcion == '3':
            print("Añadiendo un cliente...\n")

            dni = None
            while True:
                dni = res.helpers.leer_texto(3, 3, "DNI (2 ins y 1 char)").upper()
                if res.helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = res.helpers.leer_texto(2, 30, "Nombre (2 ins y 30 chars)").capitalize()
            apellido = res.helpers.leer_texto(2, 30, "Apellido (2 ins y 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
            

        if opcion == '4':
            print("Modificando un cliente...\n")
            dni = res.helpers.leer_texto(3, 3, "DNI (2 ins y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = res.helpers.leer_texto(
                    2, 30, f"DNI (2 ins y 30 chars) [{cliente.nombre}]").capitalize()
                apellido = res.helpers.leer_texto(
                    2, 30, f"DNI (2 ins y 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
            else:
                print("Cliente no encontrado.")

        if opcion == '5':
            print("Borrando un cliente...\n")
            dni = res.helpers.leer_texto(3, 3, "DNI (2 ins y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(f"Cliente [{cliente.nombre} {cliente.apellido}] borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado")
   
        if opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")