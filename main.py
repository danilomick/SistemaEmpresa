import sistema_produto #importa o sistema de produto
import sistema_cadastro #importa o sistema de cliente
from colorama import Fore, Style, init #importa os recursos do colorama

init() #inicializa o colorama


def menu_principal(): #define a função do menu principal
    while True: #loop infinito que faz o programa rodar
        print(Fore.CYAN + "=" * 70) #decoração de 70 caracteres em ciano
        print("SISTEMA PRINCIPAL".center(70)) #titulo do sistema principal
        print("=" * 70 + Style.RESET_ALL) #decoração de 70 carcateres em ciano

        print(Fore.GREEN + "1. Sistema de Clientes" + Style.RESET_ALL) #opção 1 que chama o sistema clientes
        print(Fore.BLUE + "2. Sistema de Produtos" + Style.RESET_ALL)  #opção 2 que chama o sistema produtos
        print(Fore.RED + "0. Sair" + Style.RESET_ALL)  #opção 0 que sai do sistema

        opcao = input("\nEscolha uma opção: ").strip() #pede que o usuario digite uma opção

        if opcao == "1": #se a opção for opção 1
            sistema_cadastro.menu() #chama o menu do cadastro de cliente

        elif opcao == "2": #se opção for 2
            sistema_produto.main() #chama o menu do cadastro de produto

        elif opcao == "0": #se opção for 0
            print(Fore.LIGHTYELLOW_EX + "Sistema encerrando..." + Style.RESET_ALL) #mensagem dizendo que o sistema está encerrando
            break #para o sistema

        else: #caso escolher opção invalida
            print(Fore.RED + "Escolha uma opção válida!\n" + Style.RESET_ALL) #imprime mensagem de erro em vermelho



menu_principal() #chama o menu principal