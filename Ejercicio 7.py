#Ejercicio 7/Nayla Cala/2211870

import time

class Vehiculo:
    def __init__(self, velocidad, posicion):
        self.velocidad = velocidad
        self.posicion = posicion
    
    def mover(self):
        self.posicion += self.velocidad
    
    def __str__(self):
        return f"Vehículo - Posición: {self.posicion}, Velocidad: {self.velocidad}"
        

class Semáforo:
    def __init__(self):
        self.estado = "rojo"
    
    def cambiar_estado(self):
        if self.estado == "rojo":
            self.estado = "verde"
        else:
            self.estado = "rojo"
    
    def __str__(self):
        return f"Semáforo - Estado: {self.estado}"
        

class Cruce:
    def __init__(self):
        self.semaforo = Semáforo()
        self.vehiculos = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def simular(self):
        for _ in range(10):
            print("Estado de la simulación:")
            
            # Mostrar el estado de los vehículos
            for vehiculo in self.vehiculos:
                print(vehiculo)
            
            # Mostrar el estado del semáforo
            print(self.semaforo)
            print()
            
            # Simular el movimiento de los vehículos
            for vehiculo in self.vehiculos:
                vehiculo.mover()
            
            # Verificar el estado del semáforo y detener/permitir el movimiento de los vehículos
            if self.semaforo.estado == "rojo":
                for vehiculo in self.vehiculos:
                    vehiculo.velocidad = 0
            else:
                for vehiculo in self.vehiculos:
                    vehiculo.velocidad = 5
            
            # Cambiar el estado del semáforo cada 5 segundos
            if _ % 5 == 0:
                self.semaforo.cambiar_estado()
            
            time.sleep(1)


def agregar_vehiculo(cruce, velocidad, posicion):
    vehiculo = Vehiculo(velocidad, posicion)
    cruce.agregar_vehiculo(vehiculo)
    print(f"Se agregó un nuevo vehículo al cruce: {vehiculo}")


# Crear vehículos
vehiculo1 = Vehiculo(5, 0)
vehiculo2 = Vehiculo(3, 10)

# Crear cruce
cruce = Cruce()

# Agregar vehículos al cruce
cruce.agregar_vehiculo(vehiculo1)
cruce.agregar_vehiculo(vehiculo2)

# Simular tráfico en el cruce
cruce.simular()

# Agregar nuevos vehículos durante la simulación
agregar_vehiculo(cruce, 4, 5)
agregar_vehiculo(cruce, 2, 15)

# Continuar simulación con los nuevos vehículos agregados
cruce.simular()
