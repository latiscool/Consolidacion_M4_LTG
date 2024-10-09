# ++++++ Parte 1: Implementación de las clases de vehículos +++++++++
# Definición de la clase Vehículo


# Parte 1
class Vehiculo:
    # Inicializa los atributos de la clase Vehiculo
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    # Metodo con la información básica del vehículo

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro. ruedas: {self.num_ruedas}"


# Definición de la clase hija Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        # Inicializa los atributos heredados de Vehiculo
        super().__init__(marca, modelo, num_ruedas)
        # Agrega atributos específicos de Automovil
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    # Método mostrar_informacion sobrescribe el de la clase padre  para incluir información adicional
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Velocidad: {self.velocidad} Km/h, Cilindrada:{self.cilindrada} cc"


# Parte 2
# Definición de las clases Particular y Carga
class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        # Inicializa los atributos heredados de Automovil, Metodo constructor de la clase padre
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        # Agrega atributos específicos de Particular
        self.num_puestos = num_puestos

    # Metodo mostrar_informacion sobrescribe el de la clase padre para incluir información adicional
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Nro. puestos: {self.num_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        # Inicializa los atributos heredados de Automovil,Metodo constructor de la clase padre
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        # Agrega atributos especificos de Carga
        self.peso_carga = peso_carga

        # Metodo mostrar_informacion sobrescribe el de la clase padre para incluir informacion adicional

    def mostrar_informacion(self):
        return super().mostrar_informacion()


# Definición de las clases Bicileta y Motocicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        # Inicializa los atributos heredados de Vehiculos, Metodo constructor de la clase padre
        super().__init__(marca, modelo, num_ruedas)
        # Agrego el atributo especifico de Bicicleta
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, nro_radios, cuadro, motor):
        # Inicializa los atributos heredados de Bicicleta
        super().__init__(marca, modelo, num_ruedas, tipo)
        # Agrego atributos especificos de Motocicleta
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Nro radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motro: {self.motor}"
