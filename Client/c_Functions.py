from datetime import datetime
from psutil import *
from GPUtil import *
import os

FORMAT = 'utf-8'
SIZE = 2048
PATH = "./Server/Archives"
#Client functions
def menu():
    print(
""" 
OPÇOES:
1 - DADOS DO SERVER: 
2 - HORA ATUAL:
3 - BAIXAR ARQUIVO:
4 - LISTAR ARQUIVOS:
5 - SAIR:
""")
