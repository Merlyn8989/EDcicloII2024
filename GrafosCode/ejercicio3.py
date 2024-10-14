
class GrafoCasaComercial:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_transicion(self, nodo_origen, nodo_destino):
        if nodo_origen in self.grafo and nodo_destino in self.grafo:
            self.grafo[nodo_origen].append(nodo_destino)

    def mostrar_grafo(self):
        for nodo, transiciones in self.grafo.items():
            print(f"{nodo} -> {', '.join(transiciones) if transiciones else 'Ninguna'}")

    def buscar_nodo(self, nodo):
        if nodo in self.grafo:
            transiciones = self.grafo[nodo]
            return f"{nodo} ->{', '.join(transiciones) if transiciones else 'Ninguna'}"
        return f"{nodo} no se encuentra en el grafo."

grafoCasaComercial = GrafoCasaComercial()

#nodo principla
grafoCasaComercial.agregar_nodo('Casa comercial')

#categorias
grafoCasaComercial.agregar_nodo('Alimentos')
grafoCasaComercial.agregar_nodo('Limpieza')
grafoCasaComercial.agregar_nodo('Mascotas')

#productos
grafoCasaComercial.agregar_nodo('Café')
grafoCasaComercial.agregar_nodo('Arroz')
grafoCasaComercial.agregar_nodo('Frijoles')
grafoCasaComercial.agregar_nodo('Jabones')
grafoCasaComercial.agregar_nodo('Esponjas')
grafoCasaComercial.agregar_nodo('Detergentes')
grafoCasaComercial.agregar_nodo('Croquetas')
grafoCasaComercial.agregar_nodo('Shampoo')
grafoCasaComercial.agregar_nodo('Juguetes')

#relaciones
grafoCasaComercial.agregar_transicion('Alimentos', 'Café')
grafoCasaComercial.agregar_transicion('Alimentos', 'Arroz')
grafoCasaComercial.agregar_transicion('Alimentos', 'Frijoles')
grafoCasaComercial.agregar_transicion('Limpieza', 'Jabones')
grafoCasaComercial.agregar_transicion('Limpieza', 'Esponjas')
grafoCasaComercial.agregar_transicion('Limpieza', 'Detergentes')
grafoCasaComercial.agregar_transicion('Mascotas', 'Croquetas')
grafoCasaComercial.agregar_transicion('Mascotas', 'Shampoo')
grafoCasaComercial.agregar_transicion('Mascotas', 'Juguetes')
grafoCasaComercial.mostrar_grafo()

nodo_buscar = input("Ingrese el nombre de la canción que desea buscar: ")
resultado = grafoCasaComercial.buscar_nodo(nodo_buscar)
print(resultado)