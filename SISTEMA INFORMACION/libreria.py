class libro:
    def __init__(self, nombre, autor, año, editorial):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.editorial = editorial
    
    #Imprimiendo con un metodo
    def buscar(self):
        
      print("|                                                                                       |")
      print("|========================================================================================")
      print(f"Nombre: {self.nombre}, Autor: {self.autor}, Añor: {self.año}, Editoral: {self.editorial}")
      print("|========================================================================================")
      print("|                                                                                       |")

libro1 = libro("Lugares Asombrosos", "Luis Arturo Villar Sudek","2019" ,"Penguin Random House")
libro2 = libro("El guardián entre el centeno","J.D. Salinger","1951","Alianza Editorial")
libro3 = libro("Cien años de soledad", "Gabriel García Márquez", "1967", "Editorial Sudamericana (primera edición) / Diana / Alfaguara")
libro4 = libro("El atlas de las fronteras curiosas","Zoran Nikolic","2020","Geoplaneta")
libro5 = libro("Hacia rutas salvajes (Into the Wild)", "Jon Krakauer", "1996", "B / Zeta Bolsillo")


libro1.buscar()
libro2.buscar()
libro3.buscar()
libro4.buscar()
libro5.buscar()

