from busca_largura.snake import *
from os import environ


def draw_screen(surface):
    surface.fill(COR_TABULEIRO)


def draw_grid(surface):
    x = 0
    y = 0
    for r in range(LINHAS):
        x = x + SQUARE_SIZE
        y = y + SQUARE_SIZE
        pygame.draw.line(surface, COR_GRID, (x, 0), (x, ALTURA))
        pygame.draw.line(surface, COR_GRID, (0, y), (LARGURA, y))


def play_game_busca_largura():
    pygame.init()
    environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("JOGO DA COBRA COM BFS")
    game_surface = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    snake = Snake(game_surface)

    mainloop = True
    while mainloop:
        draw_screen(game_surface)
        draw_grid(game_surface)

        snake.update()

        clock.tick(30)
        pygame.display.update()


if __name__ == '__main__':
    play_game_busca_largura()


