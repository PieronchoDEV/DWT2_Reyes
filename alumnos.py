#Creando la clase alumnos
import pickle

class alumnos:
    def __init__(self,nombre,apellido,edad,nota,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nota=nota
        self.nacionalidad=nacionalidad
        
    def leerNota(self):
        return self.nota
    
    def registrarNota(self,notaAlumno):
        self.nota=notaAlumno
    
    def imprimirDatos(self):
        print(f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Nota: {self.nota}, Nacionalidad: {self.nacionalidad}')
    

    