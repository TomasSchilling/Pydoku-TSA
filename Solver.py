#Solver de sudokus

from Sudokuclass import Sudoku
import copy
import numpy as np

# Metodo 1   Revisar espacios unicos
def rell_M1_2(sud):
    
    b =np.array(sud.tablero)
    for iteracion in range(15):
        solution_i = np.zeros((9,9),dtype=object)
        for i in range(81):
            
            if b[(divmod(i, 9))]==0:      #revisa si hay numero solos
                ret=False
                num=[]
                for j in range(1,10):
                    sud.agregar_num(j)
                    sud.agregar_pos(  (i//9+1,i%9+1)  )
                    
                    if sud.check_opcion()[0]:
                        num.append(j)
                        ret=True
                if ret:
                    solution_i[(divmod(i, 9))] = num
                    
                try:
                    if len(num)==1:
                        sud.agregar_num(num[0])
                        sud.play()
                except:
                    pass
        for i in range(9):       #revisa una fila entera
            colecc_fil= list(solution_i[i,:])
            nums=[]
            for num_i,grupo in enumerate(colecc_fil):
                if colecc_fil[num_i] !=0:
                    nums.append(colecc_fil[num_i])
                flat_list = [item for sublist in nums for item in sublist]
            for kk in range(1,10):
                if flat_list.count(kk) ==1:
                    for num_i,grupo in enumerate(colecc_fil):
                        try:
                            if kk in grupo:
                               sud.tablero[i][num_i] = kk
                        except:
                            pass
                           
        for i in range(9):      #revisa una columna entera
            colecc_col= list(solution_i[:,i])
            nums=[]
            for num_i,grupo in enumerate(colecc_col):
                if colecc_col[num_i] !=0:
                    nums.append(colecc_col[num_i])
                flat_list = [item for sublist in nums for item in sublist]
            for kk in range(1,10):
                if flat_list.count(kk) ==1:
                    for num_i,grupo in enumerate(colecc_col):
                        try:
                            if kk in grupo:
                               sud.tablero[num_i][i] = kk
                        except:
                            pass 
                        
        for i in range(3):      # revisa un cuadrado entero
            for j in range(3):
                nums=[]
                colecc_cub= solution_i[i*3:i*3+3,j*3:j*3+3]
                for num_i,grupo1 in enumerate(colecc_cub):
                    for num_j,grupo2 in enumerate(grupo1):
                        if grupo2 != 0:
                            nums.append(grupo2)
                            
                flat_list = [item for sublist in nums for item in sublist]
                
                for kk in range(1,10):
                    if flat_list.count(kk) ==1:
                        
                        for num_i,grupo1 in enumerate(colecc_cub):
                            for num_j,grupo2 in enumerate(grupo1):
                                try:
                                    
                                    if kk in grupo2:
                                        sud.tablero[num_i+i*3][num_j+j*3] = kk
                                except:
                                    pass
                        
    
    
        if sud.ganar():
            print("Izzzy lvl")     
            return sud
            
        b =np.array( copy.deepcopy(sud.tablero))  
    return sud

def rell_M3(sud):   # Metodo 3 a la fuerza bruta
    for i in range(9):
        for j in range(9):
            if sud.tablero[j][i] == 0: 
                for k in range(1, 10):
                    sud.agregar_num(k)
                    sud.agregar_pos((j+1,i+1))
        
                    if sud.check_opcion()[0]:  
                        sud.tablero[j][i] = k  
                        if sud.ganar():  
                            return sud
                        if rell_M3(sud):
                            return sud
                    sud.tablero[j][i] = 0
                
                return False
    
    return sud  






                






            
            
        
        
         
 
 