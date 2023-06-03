from paquete.cliente import Cliente
from paquete import login

datosDelCliente = {}
cliente = None

# def ingreso():

def main():
    global cliente

    print("🛒 Bienvenido a mercado Coder 🛒".center(30, "-"))

    while True:
        opcionesLogin = input(
            f"\n-------------MENU-----------------\nSeleccione el número correspondiente a su elección:\n1) Iniciar sesión\n2) Registrarse\n3) Salir\n------------------------------\n")

        if opcionesLogin == '1':
            login.crearArchivoJson()
            datosDelCliente = login.iniciarSesion()
            if cliente is None:
                cliente = Cliente(datosDelCliente['nombre'], datosDelCliente['apellido'], datosDelCliente['mail'],
                                  datosDelCliente['celular'], datosDelCliente['direccion'])

            while True:
                opcionesCompra = input(
                    f"\n-------------MENU-----------------\nSeleccione una de las siguientes opciones: \n1) Mostrar datos del cliente\n2) Comprar productos\n3) Mostrar carrito\n4) Salir\n------------------------------\n")
                if opcionesCompra == "1":
                    cliente.mostrarDatos()
                elif opcionesCompra == "2":

                    productosDisponibles = {
                        "1": "Tv",
                        "2": "Pc de escritorio",
                        "3": "Monitor",
                        "4": "Teclado mecanico",
                        "5": "Mouse gamer"
                    }


                    while True:
                        print("-----------------------------------\nLista de productos a comprar 👇")
                        print("1) tv\n2) pc de escritorio\n3) monitor\n4) teclado mecanico\n5) mouse gamer\n")
                        productoOpcion = input("Seleccione el producto (presione '0' para terminar la compra): ")

                        if productoOpcion != "0":
                            productoElegido = productosDisponibles[productoOpcion]
                            cliente.agregarProductos(productoElegido)
                        else:
                            break



                elif opcionesCompra == "3":
                    cliente.listaProductos()
                elif opcionesCompra == "4":
                    break

            print("✅ Adios, sesion cerrada".center(30, "-"))


        elif opcionesLogin == '2':
            login.crearArchivoJson()
            login.registroDeUsuario()
        elif opcionesLogin == "3":
            break

    print("Adios".center(30, "-"))


main()
