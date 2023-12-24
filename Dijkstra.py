import sys

class Dijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0 if i == j else float('inf') for j in range(vertices)] for i in range(vertices)]
        self.visitado = [False] * vertices
        self.caminho = [float('inf')] * vertices
        self.anterior = [-1] * vertices
        self.origem = 0
        self.destino = 0

    def definirGrafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i == j:
                    self.grafo[i][j] = 0
                else:
                    temp = int(input(f"mAdj({i + 1},{j + 1}): "))
                    self.grafo[i][j] = temp if temp >= 0 else float('inf')

    def definirOrigem(self):
        temp = int(input("origem: "))
        self.origem = temp - 1

    def definirDestino(self):
        temp = int(input("destino: "))
        self.destino = temp - 1

    def encontrarMinimo(self):
        minimo = float('inf')
        indiceMin = 0
        for i in range(self.vertices):
            if self.caminho[i] < minimo and not self.visitado[i]:
                minimo = self.caminho[i]
                indiceMin = i
        return indiceMin

    def caminhoMaisCurto(self):
        self.definirDestino()
        self.caminho[self.origem] = 0

        for _ in range(self.vertices):
            maisProximo = self.encontrarMinimo()
            self.visitado[maisProximo] = True
            for j in range(self.vertices):
                if self.grafo[maisProximo][j] != float('inf') and not self.visitado[j]:
                    if self.caminho[maisProximo] + self.grafo[maisProximo][j] < self.caminho[j]:
                        self.caminho[j] = self.caminho[maisProximo] + self.grafo[maisProximo][j]
                        self.anterior[j] = maisProximo

        if self.caminho[self.destino] == float('inf'):
            print("custo: Inf")
            print(f"nao existe um caminho entre {self.origem + 1} e {self.destino + 1}")
            return

        print(f"custo: {self.caminho[self.destino]}")
        print("caminho: ", end='')
        mostrarCaminho = []
        temp = self.destino
        while temp != self.origem:
            mostrarCaminho.append(temp)
            temp = self.anterior[temp]
        print(self.origem + 1, end='')
        for i in range(len(mostrarCaminho) - 1, -1, -1):
            temp = mostrarCaminho[i] + 1
            print(f"->{temp}", end='')
        print()

    def executarAlgoritmo(self):
        self.definirGrafo()
        self.definirOrigem()
        resposta = input("mostrar caminho ('s' ou 'n'): ")
        if resposta == 'n':
            return
        while resposta == 's':
            self.caminhoMaisCurto()
            resposta = input("mostrar caminho ('s' ou 'n'): ")
        if resposta == 'n':
            return
        self.definirDestino()

if __name__ == "__main__":
    nos = int(input("informe a quantidade de nos no grafo: "))
    if nos < 1:
        sys.exit(1)

    dijkstra = Dijkstra(nos)
    dijkstra.executarAlgoritmo()