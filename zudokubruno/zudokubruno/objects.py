import pygame
import random
import numpy as np
import funtions as f
import parameters as p

class Sudoku:
    def __init__(self, screen, dificultad  = 50):
        self.screen = screen
        self.crear_sudoku_aleatorio()
        self.crear_mapa(dificultad)
        self.crear_celdas()
    
    def crear_sudoku_aleatorio(self):
        mapa = np.array(((1,2,3,4,5,6,7,8,9),
                         (4,5,6,7,8,9,1,2,3),
                         (7,8,9,1,2,3,4,5,6),
                         (2,3,4,5,6,7,8,9,1),
                         (5,6,7,8,9,1,2,3,4),
                         (8,9,1,2,3,4,5,6,7),
                         (3,4,5,6,7,8,9,1,2),
                         (6,7,8,9,1,2,3,4,5),
                         (9,1,2,3,4,5,6,7,8)))
        
        for i in range(20):
            for j in range(20):
                mapa = f.swap_row(mapa)
            mapa = f.swap_numbers(mapa)
            mapa = np.transpose(mapa)

        self.mapa = mapa
        if not self.check_map():
            self.crear_sudoku_aleatorio()
        else:
            self.solution = mapa
    
    def crear_mapa(self, dificultad):
        mapa = np.zeros((9,9), dtype=np.int8)
        lista = [i for i in range(81)]
        lista = np.random.choice(lista, dificultad, replace=False)
        for i in range(9):
            for j in range(9):
                if i*9+j in lista:
                    mapa[i][j] = self.solution[i][j]
        
        self.mapa = mapa
    
    def crear_celdas(self):
        celdas = []
        for i in range(9):
            celdas.append([])
            for j in range(9):
                celdas[i].append(Celda(self.mapa[j][i],j,i,self.screen))
        self.celdas = celdas

    def check_list(self, lista):
        valido = True
        for i in range(9):
            if i+1 not in lista:
                valido = False
        return valido  

    def check_column(self, column):
        lista = []
        for i in range(9):
            lista.append(self.mapa[i][column])
        return self.check_list(lista)
    
    def check_row(self, row):
        lista = self.mapa[row]
        return self.check_list(lista)
    
    def check_square(self, square):
        lista = []
        n1 = square//3
        n2 = square%3
        for i in range(3):
            for j in range(3):
                lista.append(self.mapa[n1*3+i][n2*3+j])
        return self.check_list(lista)

    def check_map(self):
        valido = True
        for i in range(9):
            if not (self.check_column(i) and self.check_row(i) and self.check_square(i)):
                valido = False
        return valido


class Celda(pygame.sprite.Sprite):
    def __init__(self, number, x, y, screen):
        super().__init__()

        self.number = number
        self.screen = screen
        s = p.square_size
        self.row = y
        self.column = x
        self.x = x*s
        self.y = y*s
        self.Font = pygame.font.SysFont("Arial", 50)
        self.rect = pygame.Rect(self.x, self.y, s, s)
        self.surface = pygame.surface.Surface((s,s))

        if self.number == 0:
            self.modificable = True
        else:
            self.modificable = False

    def update(self):
        if (self.row//3 == 1) != (self.column//3 == 1):
            pygame.draw.rect(self.surface, p.LIGHT_GRAY, (0,0,63,63))
        else:
            pygame.draw.rect(self.surface, p.GRAY, (0,0,63,63))
        if self.number != 0:
            if self.modificable:
                color = p.DARK_GRAY
            else:
                color = p.BLACK
            text = self.Font.render(f"{self.number}", False, color)
            self.surface.blit(text, (18,3))
        self.screen.blit(self.surface, (self.x, self.y))