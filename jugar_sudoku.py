from Sudokuclass import Sudoku
from graficador import GAMING
from menu import open_main_menu,start_game
from Solver import rell_M1_2,rell_M3
from generador_mapa import generate_sudoku
dif={1:"easy",2:"medium",3:"hard",4:"hardest"}


mapa = generate_sudoku(dif[open_main_menu()])


sudu= Sudoku(mapa)

GAMING(mapa)

print(sudu.tablero)
sudu.tablero=rell_M1_2(sudu)

if not sudu.ganar():
    sudu.tablero= rell_M3(sudu)
    print("check")

GAMING(sudu.tablero) 

