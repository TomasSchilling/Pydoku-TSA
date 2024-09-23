import pygame
import sys
from Sudokuclass import Sudoku
import copy
import numpy as np

def rand_tup():
    return (np.random.randint(255),np.random.randint(255),np.random.randint(255))
 
def num_left(mapa):
    numbers_left = {i: 9 for i in range(1, 10)}
    for row in mapa:
        for num in row:
            if num != 0: 
                numbers_left[num] -= 1

    return numbers_left
    
def GAMING(b,b_solved):
    
    sud=Sudoku(copy.deepcopy(b))
    gano = True
    pygame.init()                                                #inicializar el sistema
    t_inicio = pygame.time.get_ticks()
    
    
    screen_width, screen_height = 1000, 600                      #definir dimencion pantalla y colores
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Py Sudoku")
    
    colors = [(255,255,255),    
              (170,170,170),
              (200,200,200),
              (0,200,205),
              (0,0,0),
              (255,0,0),
              (50, 50, 50)]
    
    screen.fill(colors[4])
    
    
    square_size = 200                                           # dibujar los cuadrados de 3x3
    for i in range(3):
        for j in range(3):
            color = colors[(i+j)%2]
            pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))
          
            
    square_size2 = int(200/3)                                  #dibuja los cuadrados para elegir 
    for i in range(3):
        for j in range(3):
            color = colors[0]
            pygame.draw.rect(screen, colors[0], (i * square_size2+600+square_size2+40*i, j * square_size2+int(square_size2*1.5)+40*j, square_size2, square_size2))
    pygame.draw.rect(screen, colors[0], (878, 15, square_size2, square_size2))    
    
    
    font = pygame.font.SysFont(None, int(square_size/3))     #dibujar los numeros para elegir
    font_2=  pygame.font.SysFont(None, int(square_size/5))
    font_3=  pygame.font.SysFont(None, int(square_size/7))
    for i in range(3):                
        for j in range(3):
                number_text = font.render(str(j*3+i+1), True, (0, 0, 255))  
                text_rect = number_text.get_rect(center=(int(  ((i * square_size2+600+square_size2+40*i)*2 + square_size2)/2 ), int(  (j * square_size2+int(square_size2*1.5)+40*j)*2+ square_size2-20 ) /2  ))                        
                screen.blit(number_text, text_rect)
                
                left_text = font_3.render("left", True, (0, 0, 255))
                left_text_rect = left_text.get_rect(center=(text_rect.centerx+15, text_rect.centery + square_size2 // 2))  
                screen.blit(left_text, left_text_rect)
                
    text = font.render('Current:', True, (255, 255, 255))     # dibujar texto eleccion
    text_rect = text.get_rect(center=(750 , 50))
    screen.blit(text, text_rect)
    
            
    for i in range(9):                                       # dibujar las lineas de cada valor
        pygame.draw.line(screen, colors[6], (i * square_size/3, 0), (i * square_size/3, square_size*3), 1)
        pygame.draw.line(screen, colors[6], (0, i * square_size/3), (square_size*3, i * square_size/3), 1)
    
    
    font = pygame.font.SysFont(None, int(square_size/3))  
    for i,fila in enumerate(sud.tablero):                  # dibujar los numeros iniciales del tablero
        for j,val in enumerate(fila):
            if val == 0:
                continue
            else:
                number_text = font.render(str(val), True, (0, 0, 0))  
                text_rect = number_text.get_rect(center=(int(square_size*3*(i)/9+square_size/6), int(square_size*3*(j)/9)+square_size/6))                              
                screen.blit(number_text, text_rect)
    
    
    
    while True:                                              #Main 
    
        for event in pygame.event.get():                     #Salirse 
            if event.type == pygame.QUIT:
                pygame.quit()
                return sud.tablero
                sys.exit()
                
                
            if event.type == pygame.KEYDOWN:                #Revisar numeros
                if pygame.K_1 <= event.key <= pygame.K_9 or pygame.K_KP1 <= event.key <= pygame.K_KP9:
                    num = event.key - pygame.K_1 + 1 if pygame.K_1 <= event.key <= pygame.K_9 else event.key - pygame.K_KP1 + 1
                    sud.agregar_num(num)
                    pygame.draw.rect(screen, colors[0], (878, 15, square_size2, square_size2))  
                    number_text = font.render(str(sud.num_ag), True, colors[3])  
                    text_rect = number_text.get_rect(center=(878 + square_size2 / 2, 15 + square_size2 / 2))
                    screen.blit(number_text, text_rect)
                    
            if event.type == pygame.MOUSEBUTTONUP:           # detectar el boton del mouse
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                
                if mouse_pos[0]>600 and 400<mouse_pos[1]<500:
                    print(1111)
                    pygame.draw.rect(screen, colors[1], (610, 410, 180, 90))
                    timer_text = font.render("Hint", True, colors[0])       
                    screen.blit(timer_text, (650, 450))
                
                if mouse_pos[0]<600 and mouse_pos[1]<600:       #si el mouse se encuentra en zona de juego
                    sud.agregar_pos( ( int(round(mouse_pos[0]*9/600+0.5,0)),int(round(mouse_pos[1]*9/600+0.5,0))    ))
                    if sud.check_lugar():
                        jugada = sud.check_opcion()
                        center_x= int(mouse_pos[0]/600*9)
                        center_y= int(mouse_pos[1]/600*9)
                        if jugada[0]:     # revisa y dibuja el numero en azul si se puede jugar
                            sud.play()
                            number_text = font.render( str(sud.num_ag), True, colors[3] ) 
                            text_rect = number_text.get_rect(center= (center_x*square_size2 +square_size2/2,center_y*square_size2 +  square_size2/2 )) 
                            screen.blit(number_text, text_rect)
                            
                            numeros = num_left(sud.tablero)
                            for i in range(3):                
                                for j in range(3):
                                        pygame.draw.rect(screen, colors[0], (i * square_size2+600+square_size2+40*i, j * square_size2+int(square_size2*1.5)+40*j, square_size2, square_size2))
                                        number_text = font.render(str(j*3+i+1), True, (0, 0, 255))  
                                        text_rect = number_text.get_rect(center=(int(  ((i * square_size2+600+square_size2+40*i)*2 + square_size2)/2 ), int(  (j * square_size2+int(square_size2*1.5)+40*j)*2+ square_size2-20 ) /2  ))                        
                                        screen.blit(number_text, text_rect)
                                        
                                        left_text = font_3.render(f"{numeros[j*3+i+1]} left", True, (0, 0, 255))
                                        left_text_rect = left_text.get_rect(center=(text_rect.centerx, text_rect.centery + square_size2 // 2))  
                                        screen.blit(left_text, left_text_rect)
    
                            
                            
                        elif jugada[1] ==1:                       # dibuja lineas rojas en la columna y luego devuelve al estado normal            
                            pygame.draw.line( screen, colors[5], (center_x*square_size/3, 0), (center_x*square_size/3, 600), 1)
                            pygame.draw.line( screen, colors[5], ((center_x+1)*square_size/3, 0), ((center_x+1)*square_size/3, 600), 1)
                            number_text = font.render( str(sud.num_ag), True, colors[5] ) 
                            text_rect = number_text.get_rect(center= (center_x*square_size2 +square_size2/2,center_y*square_size2 +  square_size2/2 )) 
                            screen.blit(number_text, text_rect)
                            pygame.display.flip() 
                            pygame.time.delay(1250)
                            pygame.draw.line( screen, colors[6], (center_x*square_size/3, 0), (center_x*square_size/3, 600), 1)
                            pygame.draw.line( screen, colors[6], ((center_x+1)*square_size/3, 0), ((center_x+1)*square_size/3, 600), 1)
                            pygame.draw.rect(screen, colors[(center_x//3+center_y//3)%2 ], (center_x*square_size/3+1, center_y*square_size/3+1, square_size2-2, square_size2-2))
                            pygame.display.flip() 
    
                        elif jugada[1] ==2:                       # dibuja lineas rojas en la fila y luego devuelve al estado normal            
                            pygame.draw.line( screen, colors[5], (0, center_y*square_size/3), (600, center_y*square_size/3), 1)
                            pygame.draw.line( screen, colors[5], (0, (center_y+1)*square_size/3), (600, (center_y+1)*square_size/3), 1)
                            number_text = font.render( str(sud.num_ag), True, colors[5] ) 
                            text_rect = number_text.get_rect(center= (center_x*square_size2 +square_size2/2,center_y*square_size2 +  square_size2/2 )) 
                            screen.blit(number_text, text_rect)
                            pygame.display.flip() 
                            pygame.time.delay(1250)
                            pygame.draw.line( screen, colors[6], (0, center_y*square_size/3), (600, center_y*square_size/3), 1)
                            pygame.draw.line( screen, colors[6], (0, (center_y+1)*square_size/3), (600, (center_y+1)*square_size/3), 1)
                            pygame.draw.rect(screen, colors[(center_x//3+center_y//3)%2 ], (center_x*square_size/3+1, center_y*square_size/3+1, square_size2-2, square_size2-2))
                            pygame.display.flip() 
                            
                        elif jugada[1] ==3:                       # dibuja lineas rojas en el cuadrado y luego devuelve al estado normal            
                            
                            esq_x = (center_x // 3)
                            esq_y = (center_y // 3)
                            pygame.draw.line( screen, colors[5], (esq_x*square_size, esq_y*square_size), ((esq_x+1)*square_size, esq_y*square_size), 1)
                            pygame.draw.line( screen, colors[5], (esq_x*square_size, esq_y*square_size), (esq_x*square_size, (esq_y+1)*square_size), 1)                 
                            pygame.draw.line( screen, colors[5], (esq_x*square_size, (esq_y+1)*square_size), ((esq_x+1)*square_size, (esq_y+1)*square_size), 1)
                            pygame.draw.line( screen, colors[5], ((esq_x+1)*square_size, esq_y*square_size), ((esq_x+1)*square_size, (esq_y+1)*square_size), 1) 
                            number_text = font.render( str(sud.num_ag), True, colors[5] ) 
                            text_rect = number_text.get_rect(center= (center_x*square_size2 +square_size2/2,center_y*square_size2 +  square_size2/2 )) 
                            screen.blit(number_text, text_rect)
                            pygame.display.flip() 
                            
                            pygame.time.delay(1250)
                            pygame.draw.line( screen, colors[6], (esq_x*square_size, esq_y*square_size), ((esq_x+1)*square_size, esq_y*square_size), 1)
                            pygame.draw.line( screen, colors[6], (esq_x*square_size, esq_y*square_size), (esq_x*square_size, (esq_y+1)*square_size), 1)                 
                            pygame.draw.line( screen, colors[6], (esq_x*square_size, (esq_y+1)*square_size), ((esq_x+1)*square_size, (esq_y+1)*square_size), 1)
                            pygame.draw.line( screen, colors[6], ((esq_x+1)*square_size, esq_y*square_size), ((esq_x+1)*square_size, (esq_y+1)*square_size), 1) 
                            pygame.draw.rect(screen, colors[(center_x//3+center_y//3)%2 ], (center_x*square_size/3+1, center_y*square_size/3+1, square_size2-2, square_size2-2))
                            pygame.display.flip() 
    
     
        if gano:
            t_actual = (pygame.time.get_ticks() - t_inicio) // 1000     #dibujar el tiempo que lleva
            minute, seconds = divmod(t_actual, 60)
            formatted_time = f'{minute:02}:{seconds:02}'
            timer_text = font_2.render(f'Time {formatted_time}', True, colors[2])       
            pygame.draw.rect(screen, colors[4],  (700-square_size2/2, 550-square_size2/2, square_size2*5, int(square_size2*1.2)))
            screen.blit(timer_text, (700, 550))
        
        if sud.ganar() and gano:
            for i in range(75):
                timer_text = font.render("¡GANASTEE!", True, rand_tup())       
                screen.blit(timer_text, (np.random.randint(800), np.random.randint(550)))
                pygame.time.delay(75)
                pygame.display.flip() 
            gano = False
            pygame.time.delay(4000)
            pygame.quit()
            sys.exit()
        pygame.display.flip()                               # actualiza el display
        pygame.time.delay(100)
        
    return sud.tablero
    