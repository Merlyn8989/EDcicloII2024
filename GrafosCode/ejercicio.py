class GrafoRutina:
    def __init__(self):
        self.grafo = {}

    def agregar_actividad(self, actividad):
        if actividad not in self.grafo:
            self.grafo[actividad] = []

    def agregar_transicion(self, actividad_origen, actividad_destino, tiempo_horas):
        if actividad_origen in self.grafo and actividad_destino in self.grafo:
            self.grafo[actividad_origen].append((actividad_destino, tiempo_horas))

    def mostrar_grafo(self):
        for actividad, transiciones in self.grafo.items():
            transiciones_str = ', '.join(f"{destino} (tiempo: {tiempo} horas)" for destino, tiempo in transiciones)
            print(f"{actividad} -> {transiciones_str if transiciones else 'Ninguna'}")

    def buscar_actividad(self, actividad):
        if actividad in self.grafo:
            transiciones = self.grafo[actividad]
            return f"{actividad} puede saltar a: {', '.join(f'{destino} (tiempo: {tiempo} horas)' for destino, tiempo in transiciones) if transiciones else 'Ninguna'}"
        return f"{actividad} no se encuentra en el grafo."


rutina = GrafoRutina()
rutina.agregar_actividad('Levantarme')
rutina.agregar_actividad('Alistarme')
rutina.agregar_actividad('Comer')
rutina.agregar_actividad('Ir en transporte')
rutina.agregar_actividad('Recibir clases')

rutina.agregar_transicion('Levantarme', 'Alistarme', 0.5)  
rutina.agregar_transicion('Alistarme', 'Comer', 1)        
rutina.agregar_transicion('Comer', 'Ir en transporte', 0.75) 
rutina.agregar_transicion('Ir en transporte', 'Recibir clases', 1.5)  
rutina.agregar_transicion('Recibir clases', 'Comer', 2)   

rutina.mostrar_grafo()

actividad_buscar = input("Ingrese el nombre de la actividad que desea buscar: ")
resultado = rutina.buscar_actividad(actividad_buscar)
print(resultado)

