from Sudokuclass import Sudoku
from graficador import GAMING
from menu import open_main_menu,start_game
from Solver import rell_M1_2,rell_M3
from generador_mapa import generate_sudoku
dif={1:"easy",2:"medium",3:"hard",4:"hardest"}
import copy

mapa = generate_sudoku(dif[open_main_menu()])
mapa_solved= copy.deepcopy(mapa)

sudu= Sudoku(mapa)
sudu_solved = Sudoku(mapa_solved)




sudu_solved = rell_M1_2(sudu_solved)

try:
    
    if not sudu_solved.ganar():
        sudu_solved= rell_M3(sudu_solved)
        print("check")
except:
    pass

GAMING(sudu.tablero, sudu_solved.tablero) 


