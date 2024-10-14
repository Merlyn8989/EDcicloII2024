class GrafoGeneroMusical:
    def __init__(self):
        self.grafo = {}

    def agregar_artista(self, artista):
        if artista not in self.grafo:
            self.grafo[artista] = []

    def agregar_transicion(self, artista_origen, artista_destino):
        if artista_origen in self.grafo and artista_destino in self.grafo:
            self.grafo[artista_origen].append(artista_destino)

    def mostrar_grafo(self):
        for artista, transiciones in self.grafo.items():
            print(f"{artista} -> {', '.join(transiciones) if transiciones else 'Ninguna'}")

    def buscar_artista(self, artista):
        if artista in self.grafo:
            transiciones = self.grafo[artista]
            return f"{artista} ->{', '.join(transiciones) if transiciones else 'Ninguna'}"
        return f"{artista} no se encuentra en el grafo."

generoMusical = GrafoGeneroMusical()
generoMusical.agregar_artista('Cumbia')
generoMusical.agregar_artista('Selena')
generoMusical.agregar_artista('Maribel Guardia')
generoMusical.agregar_artista('Natalia Lafourcade')
generoMusical.agregar_transicion('Cumbia', 'Selena')
generoMusical.agregar_transicion('Cumbia', 'Maribel Guardia')
generoMusical.agregar_transicion('Cumbia', 'Natalia Lafourcade')
generoMusical.mostrar_grafo()

artista_buscar = input("Ingrese el nombre de la canción que desea buscar: ")
resultado = generoMusical.buscar_artista(artista_buscar)
print(resultado)
