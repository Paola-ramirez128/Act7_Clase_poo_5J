print("Programacion POO")
# definiciom de clase
class Perro:
# funciones dentro de la clase 
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f" Nombre: {nombre} edad: {edad}")

# zona de creacion de objetos
pitbull = Perro()

# zona de uso de objetos
pitbull.Datos_perro("Bobby" ,4)
pitbull.morder()