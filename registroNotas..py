from alumnos import alumnos
import pickle

def guardar_alumnos(lista_alumnos,archivo):
    with open(archivo,'wb') as f: #wb es modo de escritura
        pickle.dump(lista_alumnos,f) #Con esto, dentro del archivo f se guarda la lista de productos

def cargar_alumnos(archivo):
    try: #open() es un metodo que nos permite trabajar con archivos
        with open(archivo, 'rb') as f: #Recibe 2 parametros: el nombre del archivo y el modo (rb es modo lectura)
            alumnos_datos=pickle.load(f)
            return alumnos_datos
    except FileNotFoundError:
        return []

def main():
    #alumno1=alumnos('Piero','Reyes',20,'','Peruano')
    #alumno2=alumnos('Yuriko','Rojas',15,'','Peruano')
    #lista_alumnos=[alumno1,alumno2]
    #print(alumno1.nombre)
    archivo_alumnos='alumnosInfo.pkl'
    lista_alumnos=cargar_alumnos(archivo_alumnos)#Nombre del archivo que queremos buscar
    
    while True: #Hasta que no se rompa este bucle con un break, se seguira ejecutando
        print('Bienvenidos al registro de notas')
        print('-----------------------------------')
        opcion = input("Ingrese comando(R,C,P,S o X): ")
        
        if opcion == 'R':
            print('Ha elegido la opcion de REGISTRAR ALUMNO')
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            edad = input('Ingrese su edad: ')
            nacionalidad = input('Ingrese su nacionalidad: ')
            
            alumno =alumnos(nombre,apellido,edad,0,nacionalidad)
            lista_alumnos.append(alumno)
        elif opcion == 'C':
            print('Ha elegido la opcion de CALIFICAR ALUMNOS')
            while True:
                for notaAlumno in lista_alumnos:
                    while True:
                        while True:
                            try:
                                nota = int(input(f'Alumno {notaAlumno.apellido}, ingrese nota: '))
                                break
                            except ValueError:
                                print('El dato ingresado no es válido, debe ingresar un numero')
                        if nota>=0 and nota<=20:
                            notaAlumno.registrarNota(nota)
                            break
                        else:
                            print('El dato ingresado esta fuera del rango permitido') 
                    print(f'La nota del alumno {notaAlumno.apellido} fue ingresada con exito')
                break
        elif opcion == 'P':
            sumaNotas=0
            cantAlumnos=len(lista_alumnos)
            for alumno in lista_alumnos:
                notaIndividual=alumno.leerNota()
                sumaNotas=sumaNotas+notaIndividual
            print(f'El promedio de notas de los {cantAlumnos} alumnos es: {sumaNotas/cantAlumnos}')
        elif opcion == 'S':
            sumaNotas=0
            cantAlumnos=len(lista_alumnos)
            for alumno in lista_alumnos:
                notaIndividual=alumno.nota
                sumaNotas=sumaNotas+notaIndividual
            print(f'La suma de notas de los {cantAlumnos} alumnos es: {sumaNotas}')
        elif opcion == 'X':
            guardar_alumnos(lista_alumnos,archivo_alumnos)
            print('Saliendo de la aplicacion...')
            break
        elif opcion == 'L': #Opcion extra que puse solo para consultar la lista de alumnos
            for alumnoInfo in lista_alumnos:
                alumnoInfo.imprimirDatos()
        else:
            print('Has ingresado una opcion no válida')

#Cuando ejecutemos nuestro script de Python, se buscara primero este codigo
if __name__ == "__main__":
    main() #Y ejecutara este metodo  