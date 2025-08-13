# Juego de tres en raya para dos jugadores

def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    print('  1 2 3')
    for i, fila in enumerate(tablero, start=1):
        print(f"{i} {'|'.join(fila)}")
        if i < 3:
            print('  -----')

def hay_ganador(tablero, jugador):
    # Comprobar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):
            return True
        if all(tablero[j][i] == jugador for j in range(3)):
            return True
    # Comprobar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(celda != ' ' for fila in tablero for celda in fila)

def pedir_movimiento(jugador, tablero):
    while True:
        try:
            entrada = input(f"Jugador {jugador}, introduce fila y columna (1-3) separadas por espacio: ")
            fila_str, col_str = entrada.strip().split()
            fila, col = int(fila_str) - 1, int(col_str) - 1
            if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
                return fila, col
            else:
                print('Movimiento inválido. Intenta de nuevo.')
        except (ValueError, IndexError):
            print('Entrada inválida. Usa dos números del 1 al 3.')

def jugar():
    tablero = crear_tablero()
    jugador_actual = 'X'
    while True:
        imprimir_tablero(tablero)
        fila, col = pedir_movimiento(jugador_actual, tablero)
        tablero[fila][col] = jugador_actual
        if hay_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f'¡Jugador {jugador_actual} ha ganado!')
            break
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print('¡Empate!')
            break
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

if __name__ == '__main__':
    jugar()
