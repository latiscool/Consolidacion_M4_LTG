from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv

# Implementación del programa principal
# Creación de automóviles

print(
    "----------------------------PARTE 1 -------------------------------------------------------------"
)


def crear_automoviles():
    automoviles = []
    cantidad = int(input("¿Cuántos vehículos desea insertar? "))

    # bucle que se repetirá cantidad veces, dependera de la cantidad que ingrese el usuario.
    for i in range(cantidad):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        # Creando Objeto Automovil con los datos ingresados
        automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        automoviles.append(automovil)
    return automoviles


def mostrar_automoviles(automoviles):
    # Función para mostrar la información de los automóviles
    print("\nImprimiendo por pantalla los Vehículos:")
    # enumerate(automoviles, 1) genera pares de (índice, elemento) para cada elemento en automoviles, comenzando la numeración desde 1
    for i, auto in enumerate(automoviles, 1):
        print(f"Datos del automóvil {i} : {auto.mostrar_informacion()}")
    print(
        "-------------------------------------------------------------------------------------------------\n"
    )


# Parte 3
def guardar_datos_csv(vehiculos):
    try:
        # Abrimos el archivo 'vehiculos.csv' en modo escritura
        with open("vehiculos.csv", "w", newline="") as archivo:
            # Creamos un objeto writer de csv
            writer = csv.writer(archivo)
            # Iteramos sobre cada vehículo en la lista
            for vehiculo in vehiculos:
                # Preparamos los datos a escribir
                datos = [
                    f"<class 'Vehiculo.{type(vehiculo).__name__}'>",  # Nombre de la clase
                    str(vehiculo.__dict__),  # Diccionario de atributos del vehículo
                ]
                # Escribimos los datos en el archivo CSV
                writer.writerow(datos)
        print(
            "-----------------------------------PARTE 3------------------------------------------------\n"
        )
        print("Datos guardados correctamente en vehiculos.csv")
    except Exception as e:
        # Capturamos cualquier error que pueda ocurrir
        print(f"Error al guardar los datos: {str(e)}")


def recuperar_datos_csv():
    try:
        # Abrimos el archivo 'vehiculos.csv' en modo lectura
        with open("vehiculos.csv", "r") as archivo:
            # Creamos un objeto reader de csv
            reader = csv.reader(archivo)
            # Leemos y mostramos cada fila del archivo

            for row in reader:
                print(row)
    except FileNotFoundError:
        # Manejamos el caso en que el archivo no exista
        print("El archivo vehiculos.csv no existe.")
    except Exception as e:
        # Capturamos cualquier otro error que pueda ocurrir
        print(f"Error al leer los datos: {str(e)}")


def leer_datos_csv():
    try:
        # Abrimos el archivo 'vehiculos.csv' en modo lectura
        with open("vehiculos.csv", "r") as archivo:
            # Creamos un objeto reader de csv
            reader = csv.reader(archivo)
            # Iteramos sobre cada fila del archivo
            print(
                "----------------------------------------------------------------------------------\n"
            )
            for row in reader:
                # Extraemos el nombre de la clase
                clase = row[0].split(".")[-1][:-2]
                # Convertimos la cadena de atributos en un diccionario
                datos = eval(row[1])
                # Imprimimos la información formateada
                print(f"Lista de Vehiculos {clase}")
                print(datos)
    except FileNotFoundError:
        print("Error: El archivo vehiculos.csv no existe.")
    except PermissionError:
        print("Error: No se tiene permiso para leer el archivo vehiculos.csv.")
    except csv.Error as e:
        print(f"Error en la lectura del archivo CSV: {str(e)}")
    except SyntaxError:
        print("Error: El archivo contiene datos en un formato incorrecto.")
    except Exception as e:
        print(f"Error inesperado al leer los datos: {str(e)}")


# llamo a funciones en un orden específico con main().
def main():
    # Parte 1
    automoviles = crear_automoviles()
    mostrar_automoviles(automoviles)

    # Parte 2: Crear instancias de las nuevas clases
    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Asignando a una lista todos los vehiculos
    vehiculos = [particular, carga, bicicleta, motocicleta]
    print(
        "----------------------------PARTE 2 -------------------------------------------------------------"
    )

    print("\nImprimiendo por pantalla INSTANCIAS:")
    for i in vehiculos:
        print(i.mostrar_informacion())

    # Verificar las relaciones de herencia
    print(
        f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}"
    )
    print(
        f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}"
    )
    print(
        f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}"
    )
    print(
        f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}"
    )
    print(
        f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}"
    )
    print(
        f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}"
    )
    print(
        "-------------------------------------------------------------------------------------------------\n"
    )

    # Parte 3
    guardar_datos_csv(vehiculos)
    recuperar_datos_csv()
    leer_datos_csv()


if __name__ == "__main__":
    main()
