# TAMANHOS E CORES
LARGURA = 612   
ALTURA = 612  
LINHAS = 17 # NUMERO DE LINHAS E COLUNAS DO TABULEIRO
SQUARE_SIZE = LARGURA // LINHAS # TAMANHO DOS QUADRADOS
GAP_SIZE = 2  # ENTRE PÍXELS (QUADRADOS) DO TABULEIRO

COR_TABULEIRO = (15, 15, 15)
COR_GRID = (20, 20, 20)
COR_COBRA = (0, 255, 0)
COR_COMIDA = (255, 255, 0)
COR_CABECA = (0, 255, 0)
COR_COBRA_VIRTUAL = (0, 255, 0)


# CONFIGS INICIAIS DO JOGO
TAMANHO_INICIAL_COBRA = 3
PAUSA_PARA_REINICIO = 15  # PAUSA ANTES DE REINICIAR O JOGO
MOVIMENTOS_SEM_COMER = LINHAS * LINHAS * LINHAS * 2  # FINALIZA O JOGO SE FICAR MUITO TEMPO SEM COMER
TAM_MAX_COBRA = LINHAS * LINHAS - TAMANHO_INICIAL_COBRA  # NUMERO MAXIMO DE PEÇAS QUE A COBRA PODE TER

# PARA O BFS
GRID = [[i, j] for i in range(LINHAS) for j in range(LINHAS)]

def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors


def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 - y1)


# USANDO TUPLAS POR SER LINGUAGEM PYTHON
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
