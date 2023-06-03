import json
import os

baseDeDatos = []

def crearArchivoJson():
    if not os.path.isfile("baseDeDatos.json"):
        with open("baseDeDatos.json", "w") as archivo:
            json.dump([], archivo)

def registroDeUsuario():
    print("Bienvenido al registro de usuario".center(30, "-"))
    print("Completa los siguientes campos para poder registrarte")

    mail = input("Mail: ")
    password = input("Contraseña: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    celular = input("Celular: ")
    direccion = input("Direccion: ")

    user = {
        "mail": mail,
        "password": password,
        "nombre": nombre,
        "apellido": apellido,
        "celular": celular,
        "direccion": direccion


    }

    with open("baseDeDatos.json", "r") as archivo:
         baseDeDatos = json.load(archivo)

    baseDeDatos.append(user)

    with open("baseDeDatos.json", "w") as archivo:
        json.dump(baseDeDatos, archivo)


def iniciarSesion():
    print("Iniciar sesión".center(30, "-"))

    mail = input("Ingrese su mail: ")
    password = input("ingrese su contraseña: ")

    loginExitoso = False
    datosDelUsuario = {}

    with open("baseDeDatos.json", "r") as archivo:
        usuariosCargados = json.load(archivo)

    for e in usuariosCargados:
        if e["mail"] == mail and e["password"] == password:
            loginExitoso = True
            datosDelUsuario = e

    if loginExitoso:
        print("👉 Inicio de sesion exitoso ✅")
        return datosDelUsuario
    else:
        print("Mail o contraseña incorrectos ⛔".center(40, " "))

