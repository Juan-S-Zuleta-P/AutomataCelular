import numpy as np

class Celda:
    def __init__(self, fila, columna, vivo=False):
        self.fila = fila  # Asigna la fila de la celda al atributo "fila"
        self.columna = columna  # Asigna la columna de la celda al atributo "col"
        self.vivo = vivo  # Asigna el estado de vida de la celda al atributo "vivo"

    def estaVivo(self):
        return self.vivo  # Devuelve el estado de vida de la celda

    def setEstado(self, vivo):
        self.vivo = vivo  # Establece el estado de vida de la celda

class Board:
    def __init__(self, filas, columnas):
        self.filas = filas  # Asigna el número de filas al atributo "filas"
        self.columnas = columnas  # Asigna el número de columnas al atributo "columnas"
        self.celdas = np.ndarray((filas, columnas), dtype=Celda)  # Crea una matriz de celdas vacías con las dimensiones especificadas
        for i in range(filas):
            for j in range(columnas):
                self.celdas[i][j] = Celda(i, j)  # Inicializa cada celda en la matriz con una instancia de la clase "Celda"

    def getCelda(self, fila, columna):
        return self.celdas[fila][columna]  # Devuelve la celda en la posición especificada

    def setCelda(self, fila, columna, value):
        self.celdas[fila][columna].setEstado(value)  # Establece el estado de vida de la celda en la posición especificada

    def contador_Vecinos(self, fila, columna):
        count = 0  # Inicializa el contador de vecinos vivos
        for i in range(max(0, fila-1), min(fila+2, self.filas)):
            for j in range(max(0, columna-1), min(columna+2, self.columnas)):
                if i == fila and j == columna:
                    continue  # Omite la celda actual, ya que no se considera como vecino
                if self.celdas[i][j].estaVivo():
                    count += 1  # Incrementa el contador si la celda vecina está viva
        return count  # Devuelve el número de vecinos vivos

    def sobrevive(self):
        new_board = Board(self.filas, self.columnas)  # Crea un nuevo tablero vacío
        for i in range(self.filas):
            for j in range(self.columnas):
                celda = self.celdas[i][j]  # Obtiene la celda actual
                neighbors = self.contador_Vecinos(i, j)  # Cuenta los vecinos vivos de la celda
                if celda.estaVivo() and (neighbors == 2 or neighbors == 3):
                    new_board.setCelda(i, j, True)  # Establece la celda como viva en el nuevo tablero si cumple las condiciones
                elif not celda.estaVivo() and neighbors == 3:
                    new_board.setCelda(i, j, True)  # Establece la celda como viva en el nuevo tablero si cumple las condiciones
        self.celdas = new_board.celdas  # Actualiza el tablero actual con el nuevo tablero

class JuegoDeLaVida:
    def __init__(self, board):
        self.board = board  # Asigna el tablero

    def actualizar_Board(self):
        self.board.sobrevive()  # Actualiza el estado del tablero llamando al método sobrevive() del objeto board

    def correr(self, num_generations):
        for generation in range(num_generations):
            print(f"Generación {generation+1}:")  # Imprime el encabezado de la generación actual
            for i in range(self.board.filas):
                fila = ""
                for j in range(self.board.columnas):
                    fila += " ◆ " if self.board.getCelda(i, j).estaVivo() else " ▢ "  # Construye la cadena de caracteres para representar el tablero
                print(fila)  # Imprime la representación visual del tablero
            self.actualizar_Board()  # Actualiza el estado del tablero en cada generación


if __name__ == "__main__":
    # Ejemplo de uso 1
    """board = Board(10, 10)
    board.setCelda(1, 2, True)
    board.setCelda(2, 3, True)"""

    # Ejemplo de uso 2
    """board = Board(10, 10)
    board.setCelda(1, 2, True)
    board.setCelda(1, 4, True)
    board.setCelda(2, 2, True)
    board.setCelda(2, 3, True)
    board.setCelda(3, 3, True)
    board.setCelda(3, 4, True)"""

    # Ejemplo de uso 3
    """board = Board(10, 10)
    board.setCelda(1, 2, True)
    board.setCelda(2, 3, True)
    board.setCelda(3, 3, True)"""
    
    """# Ejemplo de uso 4
    board = Board(10, 10)
    board.setCelda(1, 2, True)
    board.setCelda(2, 2, True)
    board.setCelda(3, 4, True) 

    game = JuegoDeLaVida(board) 

    game.correr(2)  # Ejecuta el juego durante 2 generaciones"""

    
    # Ejemplo https://adntro.com/wp-content/uploads/2022/08/conway_planeador.jpg
    board = Board(11, 11)
    board.setCelda(4, 5, True) # Establece una celda como viva en la posición (2, 5)
    board.setCelda(5, 6, True)
    board.setCelda(6, 6, True) 
    board.setCelda(6, 5, True) 
    board.setCelda(6, 4, True) 

    game = JuegoDeLaVida(board)  # Crea una instancia del juego de la vida con el tablero creado

    game.correr(5)  # Ejecuta el juego durante 2 generaciones
