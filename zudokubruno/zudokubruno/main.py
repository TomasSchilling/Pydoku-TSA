import pygame 
import parameters as p
from objects import Sudoku

pygame.init()
pygame.font.init()

screen  = pygame.display.set_mode(p.screen_size)

S = Sudoku(screen)

grupo_celdas = pygame.sprite.Group()
grupo_mouse = pygame.sprite.Group()
mouse_sprite = pygame.sprite.Sprite()
grupo_mouse.add()

for row in S.celdas:
    for celda in row:
        grupo_celdas.add(celda)
grupo_celdas.update()


game = True 
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            S = Sudoku(screen)
            grupo_celdas = pygame.sprite.Group()
            for row in S.celdas:
                for celda in row:
                    grupo_celdas.add(celda)
            grupo_celdas.update()
    pygame.display.flip()
