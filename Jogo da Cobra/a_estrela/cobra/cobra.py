from pygame import display, time, draw, QUIT, init, KEYDOWN, K_a, K_s, K_d, K_w
from random import randint
import pygame
from numpy import sqrt
init()

def play_game_a_estrela():
    def getpath(comida1, cobra1):
        comida1.camefrom = []
        for s in cobra1:
            s.camefrom = []
        openset = [cobra1[-1]]
        closedset = []
        dir_array1 = []
        while 1:
            current1 = min(openset, key=lambda x: x.f)
            openset = [openset[i] for i in range(len(openset)) if not openset[i] == current1]
            closedset.append(current1)
            for neighbor in current1.neighbors:
                if neighbor not in closedset and not neighbor.obstrucle and neighbor not in cobra1:
                    tempg = neighbor.g + 1
                    if neighbor in openset:
                        if tempg < neighbor.g:
                            neighbor.g = tempg
                    else:
                        neighbor.g = tempg
                        openset.append(neighbor)
                    neighbor.h = sqrt((neighbor.x - comida1.x) ** 2 + (neighbor.y - comida1.y) ** 2)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.camefrom = current1
            if current1 == comida1:
                break
        while current1.camefrom:
            if current1.x == current1.camefrom.x and current1.y < current1.camefrom.y:
                dir_array1.append(2)
            elif current1.x == current1.camefrom.x and current1.y > current1.camefrom.y:
                dir_array1.append(0)
            elif current1.x < current1.camefrom.x and current1.y == current1.camefrom.y:
                dir_array1.append(3)
            elif current1.x > current1.camefrom.x and current1.y == current1.camefrom.y:
                dir_array1.append(1)
            current1 = current1.camefrom
        for i in range(linhas):
            for j in range(colunas):
                grid[i][j].camefrom = []
                grid[i][j].f = 0
                grid[i][j].h = 0
                grid[i][j].g = 0
        return dir_array1

    class Spot:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.camefrom = []
            self.obstrucle = False
            if randint(1, 101) < 3:
                self.obstrucle = True

        def show(self, color):
            draw.rect(screen, color, [self.x*hr+2, self.y*wr+2, hr, wr])

        def add_neighbors(self):
            if self.x > 0:
                self.neighbors.append(grid[self.x - 1][self.y])
            if self.y > 0:
                self.neighbors.append(grid[self.x][self.y - 1])
            if self.x < linhas - 1:
                self.neighbors.append(grid[self.x + 1][self.y])
            if self.y < colunas - 1:
                self.neighbors.append(grid[self.x][self.y + 1])

    done = False
    PRETO = (0, 0, 0)
    VERDE = (0, 255, 0)
    AMARELO = (255, 255, 0)
    ROXO = (128, 0, 128)

    colunas = 17
    linhas = 17

    largura = 612
    altura = 612
    wr = largura/colunas
    hr = altura/linhas
    direction = 1

    screen = display.set_mode([largura, altura])
    display.set_caption("JOGO DA COBRA COM A*")
    clock = time.Clock()

    grid = [[Spot(i, j) for j in range(colunas)] for i in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            grid[i][j].add_neighbors()

    snake = [grid[round(linhas/2)][round(colunas/2)]]
    food = grid[randint(0, linhas-1)][randint(0, colunas-1)]
    current = snake[-1]
    dir_array = getpath(food, snake)
    food_array = [food]

    while not done:
        clock.tick(30)
        screen.fill(PRETO)
        direction = dir_array.pop(-1)
        if direction == 0:    # PARA BAIXO
            snake.append(grid[current.x][current.y + 1])
        elif direction == 1:  # PARA A DIREITA
            snake.append(grid[current.x + 1][current.y])
        elif direction == 2:  # PARA CIMA
            snake.append(grid[current.x][current.y - 1])
        elif direction == 3:  # PARA A ESQUERDA
            snake.append(grid[current.x - 1][current.y])
        current = snake[-1]

        if current.x == food.x and current.y == food.y:
            while 1:
                food = grid[randint(0, linhas - 1)][randint(0, colunas - 1)]
                if not (food.obstrucle or food in snake):
                    break
            food_array.append(food)
            dir_array = getpath(food, snake)
        else:
            snake.pop(0)

        for spot in snake:
            spot.show(VERDE)
        for i in range(colunas):
            for j in range(colunas):
                if grid[i][j].obstrucle:
                    grid[i][j].show(ROXO)

        food.show(AMARELO)
        snake[-1].show(VERDE)
        display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_w and not direction == 0:
                    direction = 2
                elif event.key == K_a and not direction == 1:
                    direction = 3
                elif event.key == K_s and not direction == 2:
                    direction = 0
                elif event.key == K_d and not direction == 3:
                    direction = 1



if __name__ == '__main__':
    play_game_a_estrela()

