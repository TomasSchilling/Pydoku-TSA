import copy

class Sudoku:
    
    def __init__(self,tablero):
        self.tablero = tablero
        self.valido_gen = True
        self.valido_loc = True
        self.jugada = True
        self.num_ag = 0
        
    def check_gen(self):
        if len(self.tablero) ==9:
            for i in self.tablero:
                if len(i) == 9:
                    continue
                else:
                    self.valido_gen = False
                    break
        else:
            self.valido_gen = False
        
        if not (self.check_columna() and self.check_fila() and self.check_cuadrado()):
            self.valido_gen = False
            
        if not self.valido_gen:
            print("El tablero no es valido, revisar")
        else:
            print("El talbero es valido")
        
    def check_fila(self): #Checkea cada fila si tiene numeros distintos, no cuenta el 0
        
        for i in self.tablero:
            i_0 = [x for x in i if x != 0]
            if len(i_0) != len(set(i_0)):
                print("error en filas")
                return False
        return True
    
    def check_columna(self):  #Checkea cada columna si tiene numeros distintos, no cuenta el 0
        
        for i in range(len(self.tablero)):
            i_0 = [col[i] for col in self.tablero if col[i] !=0 ]
            if len(i_0) != len(set(i_0)):
                print("error en columnas")
                return False
        return True
                 
    def check_cuadrado(self):  #Checkea cada cuadrado de 3x3 si tiene numeros distintos, no cuenta el 0
        for i in range(3):
            for j in range(3):
                i_0 = [x for x in (self.tablero[i*3+0][j*3:j*3+3]+
                                   self.tablero[i*3+1][j*3:j*3+3]+
                                   self.tablero[i*3+2][j*3:j*3+3])   if x != 0]
                if len(i_0) != len(set(i_0)):
                    print("error en bloques 3x3")
                    return False
        return True
        
    def agregar_num(self,num):        #escribe el numero entregado por el input (teclado)
        self.num_ag=int(num)
        
    def agregar_pos(self,par):           #escribe la posicion entregada por el boton (click)
        
        self.pos_ag= [par[0],par[1]]
    
    def check_lugar(self):     # chequea si el espacio esta libre para poner un numero
        
        if self.num_ag > 9 or self.num_ag < 1 :
            return False
        if self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] !=0:
            print("jugada no valida")
            return False
        return True
    
    def check_opcion(self):     # chequea si se puede aplicar la jugada en el campo
        
        self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = self.num_ag
        
        for i in self.tablero:
            i_0 = [x for x in i if x != 0]
            if len(i_0) != len(set(i_0)):
                self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = 0
                return (False, 1)
        
        for i in range(len(self.tablero)):
            i_0 = [col[i] for col in self.tablero if col[i] !=0 ]
            if len(i_0) != len(set(i_0)):
                self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = 0
                return (False,2  )     
            
        for i in range(3):
            for j in range(3):
                i_0 = [x for x in (self.tablero[i*3+0][j*3:j*3+3]+
                                   self.tablero[i*3+1][j*3:j*3+3]+
                                   self.tablero[i*3+2][j*3:j*3+3])   if x != 0]
                if len(i_0) != len(set(i_0)):
                    self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = 0
                    return (False,3)
        self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = 0
        return (True,0)
        
    
        
    
    def play(self):   # actualiza el numero en el tablero
        
        self.tablero[self.pos_ag[0]-1][self.pos_ag[1]-1] = self.num_ag


    def ganar(self):
        for i in self.tablero:
            for j in i:
                if j == 0:
                    return False
        return True

