import os
from colorama import Fore, Style, init

init()
arquivo_dados = "Produtos.txt"

def cadastro_produto():
    while True:
        produto = input("Digite o nome do produto que será cadastrado: ").title().strip()
        
        if len(produto) == 0:
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL)
        elif not produto.replace(" ", "").isalpha():
            print(Fore.RED + "Erro! Digite somente letras.\n" + Style.RESET_ALL)
        else:
            return produto