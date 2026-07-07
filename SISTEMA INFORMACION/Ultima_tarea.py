class Libro:

    def __init__(self, nombre, autor, año, editorial, paginas, disponible):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.editorial = editorial
        self.paginas = paginas
        self.disponible = disponible

    def imprimir(self):
        print("\n------------------------------")
        print("Nombre:", self.nombre)
        print("Autor:", self.autor)
        print("Año:", self.año)
        print("Editorial:", self.editorial)
        print("Páginas:", self.paginas)

        if self.disponible:
            print("Estado: Disponible")
        else:
            print("Estado: Prestado")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.nombre}' ha sido prestado.")
        else:
            print(f"El libro '{self.nombre}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.nombre}' ha sido devuelto.")
        else:
            print(f"El libro '{self.nombre}' ya estaba disponible.")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943,
               "Reynal & Hitchcock", 96, True)

libro2 = Libro("1984", "George Orwell", 1949,
               "Secker & Warburg", 328, False)


libro1.imprimir()
libro1.prestar()
libro1.imprimir()

libro2.imprimir()
libro2.devolver()
libro2.imprimir()