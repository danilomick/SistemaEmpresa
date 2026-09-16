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
        
def cadastro_valor(nome_produto):
    while True:
        preco = input(Fore.LIGHTWHITE_EX+f"Digite o valor de {nome_produto}: "+ Style.RESET_ALL).strip().replace(',', '.')
        
        if len(preco) == 0:
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL)
            continue 
            
        try:
            # preco é convertido em Float agora, porque não é aceito strip em entrada float
            valor = float(preco)
            if valor <= 0:
                print(Fore.RED + "Erro! O valor deve ser maior que zero\n" + Style.RESET_ALL)
                continue
            return valor
        except ValueError:
            print(Fore.RED + "Erro! Valor inválido. Digite um número.\n" + Style.RESET_ALL)