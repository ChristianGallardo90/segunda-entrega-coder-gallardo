class Cliente:
    def __init__(self,nombre,apellido,mail,celular,direccion,):
        self.nombre = nombre
        self.apellido  = apellido
        self.mail = mail
        self.celular = celular
        self.direccion = direccion
        self.carrito = []

    def mostrarDatos(self):
        print("Datos del cliente")
        print(f"Nombre: {self.nombre}")
        print(f"mail: {self.mail}")
        print(f"Celular: {self.celular}")
        print(f"Direccion: {self.direccion}")

    def agregarProductos(self,producto):
          self.carrito.append(producto)
          print(f"\n✅ el producto >> {producto} << se agrego al carrito de {self.nombre}")

    def listaProductos(self):
        print(f"Estos son los objetos que actualmente tenes en tu carrito: ")
        for objeto in self.carrito:
            print(f"• {objeto}")

    def __str__(self):
        return self.name

