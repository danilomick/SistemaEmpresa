import os  # importa o módulo os, que permite trabalhar com arquivos e pastas do sistema
from colorama import Fore, Style, init  # importa recursos do colorama para adicionar cores aos textos

init()  # inicia o colorama para permitir o uso das cores no terminal

ARQUIVO = "clientes.txt"  # cria uma variável que armazena o nome do arquivo onde os clientes serão salvos

def salvar_clientes_arquivo(nome, email, telefone):  # define a função responsável por salvar um cliente no arquivo
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:  # abre o arquivo no modo append para adicionar os dados
        arquivo.write(f"{nome};{email};{telefone}\n")  # escreve os dados do cliente no arquivo

def ler_clientes_arquivo():  # define a função responsável por ler os clientes salvos no arquivo
    clientes = []  # cria uma lista vazia para armazenar os clientes

    if not os.path.exists(ARQUIVO):  # verifica se o arquivo de clientes existe
        return clientes  # retorna a lista vazia caso o arquivo não exista

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:  # abre o arquivo no modo leitura
        linhas = arquivo.readlines()  # lê todas as linhas do arquivo

        for linha in linhas:  # percorre cada linha encontrada no arquivo
            dados = linha.strip().split(";")  # remove espaços e separa os dados pelo ponto e vírgula

            if len(dados) == 3:  # verifica se existem os três dados esperados
                nome = dados[0]  # pega o primeiro dado, que corresponde ao nome
                email = dados[1]  # pega o segundo dado, que corresponde ao email
                telefone = dados[2]  # pega o terceiro dado, que corresponde ao telefone

                clientes.append({"nome": nome, "email": email, "telefone": telefone})  # adiciona o cliente à lista

    return clientes  # retorna a lista com todos os clientes

def reescrever_arquivo(clientes):  # define a função responsável por reescrever o arquivo com os dados atualizados
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:  # abre o arquivo no modo escrita, apagando o conteúdo anterior

        for cliente in clientes:  # percorre cada cliente da lista
            arquivo.write(f"{cliente['nome']};{cliente['email']};{cliente['telefone']}\n")  # escreve os dados atualizados no arquivo

def cadastrar_clientes():  # define a função responsável por cadastrar um novo cliente
    print(Fore.GREEN + "\nCADASTRAR CLIENTES" + Style.RESET_ALL)  # exibe o título da função na cor verde
    
    while True:  # inicia um loop para validar o nome
        nome = input("Digite o nome do cliente: ").strip()  # solicita o nome e remove espaços extras

        if not nome:  # verifica se o nome está vazio
            print(Fore.RED + "Erro! O nome não pode estar vazio." + Style.RESET_ALL)  # mostra uma mensagem de erro
            continue  # volta para o início do loop

        if nome.replace(" ", "").isalpha():  # verifica se o nome possui apenas letras, ignorando espaços
            break  # encerra o loop caso o nome seja válido
        else:  # executa caso o nome possua caracteres inválidos
            print(Fore.RED + "Erro! O nome deve conter apenas letras." + Style.RESET_ALL)  # mostra uma mensagem de erro

    while True:  # inicia um loop para validar o email
        email = input("Digite o email do cliente: ").strip()  # solicita o email e remove espaços extras

        if "@" not in email:  # verifica se o email possui o caractere @
            print(Fore.RED + 'Erro! O email deve conter "@" .' + Style.RESET_ALL)  # mostra uma mensagem de erro
            continue  # volta para o início do loop

        break  # encerra o loop caso o email seja válido

    while True:  # inicia um loop para validar o telefone
        telefone = input("Digite o telefone do cliente: ")  # solicita o telefone
        limite_de_numeros = 13  # define a quantidade esperada de caracteres

        try:  # tenta verificar se o telefone possui somente números
            telefone_int = int("".join(telefone.replace("-", "").split()))  # remove hífen e espaços e converte para inteiro
        except:  # executa caso ocorra um erro na conversão
            print(Fore.RED + "Erro! O telefone deve ser só numeros" + Style.RESET_ALL)  # mostra uma mensagem de erro
            continue  # volta para o início do loop

        if len(telefone) == limite_de_numeros:  # verifica se o telefone possui 13 caracteres
            break  # encerra o loop caso o telefone seja válido
        else:  # executa caso o telefone tenha tamanho incorreto
            print(Fore.RED + 'Erro! o telefone deve ser no formato "xx xxxxx-xxxx"' + Style.RESET_ALL)  # mostra o formato correto
            continue  # volta para o início do loop

    salvar_clientes_arquivo(nome, email, telefone)  # chama a função que salva o cliente no arquivo
    print(Fore.GREEN + "Cliente cadastrado com sucesso!\n" + Style.RESET_ALL)  # mostra uma mensagem de sucesso

def listar_cliente():  # define a função responsável por listar os clientes
    if not os.path.exists(ARQUIVO):  # verifica se o arquivo de clientes existe
        print(Fore.YELLOW + "Não há nenhum cliente cadastrado\n" + Style.RESET_ALL)  # mostra uma mensagem caso o arquivo não exista
        return  # encerra a função

    clientes = ler_clientes_arquivo()  # chama a função para ler os clientes do arquivo

    if not clientes:  # verifica se a lista de clientes está vazia
        print(Fore.YELLOW + "Não há nenhum cliente cadastrado!\n" + Style.RESET_ALL)  # mostra uma mensagem caso não existam clientes
        return  # encerra a função

    print(Fore.CYAN + "\nLISTA DE CLIENTES" + Style.RESET_ALL)  # exibe o título da lista
    print(f"{'NOME':<25}{'E-MAIL':<50}{'TELEFONE':<13}")  # cria o cabeçalho da tabela
    print("-" * 100)  # imprime uma linha para separar o cabeçalho dos dados

    for cliente in clientes:  # percorre todos os clientes da lista
        print(f"{cliente['nome'].lower():<25}{cliente['email']:<50}{cliente['telefone']:<13}")  # exibe os dados organizados em colunas

    print()  # imprime uma linha vazia
def alterar_cliente():  # define a função responsável por alterar os dados de um cliente
    listar_cliente()  # chama a função de listar para mostrar os clientes antes da alteração
    clientes = ler_clientes_arquivo()  # lê os clientes do arquivo e armazena todos em uma lista
    if not clientes:  # verifica se não existem clientes cadastrados
        print(Fore.YELLOW + "Não há nenhum cliente cadastrado para alterar!\n" + Style.RESET_ALL)  # informa que não há clientes para alterar
        return  # encerra a função

    print(Fore.CYAN + "\nALTERAR CLIENTE" + Style.RESET_ALL)  # exibe o título da alteração na cor ciano
    email_busca = input("Digite o E-MAIL do cliente que deseja alterar: ").strip()  # solicita o email usado para encontrar o cliente
    cliente_encontrado = False  # cria uma variável para controlar se o cliente foi encontrado

    for cliente in clientes:  # percorre todos os clientes da lista
        if cliente["email"] == email_busca:  # verifica se o email informado pertence ao cliente atual
            cliente_encontrado = True  # informa que o cliente foi encontrado
            print(Fore.YELLOW + f"Alterando os dados de: {cliente['nome'].upper()}" + Style.RESET_ALL)  # mostra o nome do cliente que será alterado

            while True:  # inicia um loop para validar o novo nome
                novo_nome = input(f"Novo nome (Atual: {cliente['nome']}): ").strip()  # solicita o novo nome e remove espaços extras
                if not novo_nome:  # verifica se o novo nome está vazio
                    print(Fore.RED + "Erro! O nome não pode estar vazio." + Style.RESET_ALL)  # mostra uma mensagem de erro
                    continue  # volta para o início do loop
                if novo_nome.replace(" ", "").isalpha():  # verifica se o novo nome possui apenas letras, ignorando espaços
                    cliente["nome"] = novo_nome  # substitui o nome antigo pelo novo nome
                    break  # encerra o loop
                else:  # executa caso o novo nome tenha caracteres inválidos
                    print(Fore.RED + "Erro! O nome deve conter apenas letras." + Style.RESET_ALL)  # mostra uma mensagem de erro

            while True:  # inicia um loop para validar o novo email
                novo_email = input(f"Novo e-mail (Atual: {cliente['email']}): ").strip()  # solicita o novo email
                if "@" not in novo_email:  # verifica se o novo email possui o caractere @
                    print(Fore.RED + 'Erro! O email deve conter "@" .' + Style.RESET_ALL)  # mostra uma mensagem de erro
                    continue  # volta para o início do loop
                cliente["email"] = novo_email  # substitui o email antigo pelo novo
                break  # encerra o loop

            while True:  # inicia um loop para validar o novo telefone
                novo_telefone = input(f"Novo telefone (Atual: {cliente['telefone']}): ")  # solicita o novo telefone
                try:  # tenta verificar se o telefone contém apenas números, espaços e hífen
                    int("".join(novo_telefone.replace("-", "").split()))  # remove espaços e hífen e tenta converter o resultado para inteiro
                except:  # executa caso a conversão apresente erro
                    print(Fore.RED + "Erro! O telefone deve ser só numeros" + Style.RESET_ALL)  # mostra uma mensagem de erro
                    continue  # volta para o início do loop

                if len(novo_telefone) == 13:  # verifica se o telefone possui 13 caracteres
                    cliente["telefone"] = novo_telefone  # substitui o telefone antigo pelo novo
                    break  # encerra o loop
                else:  # executa caso o telefone tenha tamanho diferente de 13
                    print(Fore.RED + 'Erro! o telefone deve ser no formato "xx xxxxx-xxxx"' + Style.RESET_ALL)  # mostra o formato esperado
                    continue  # volta para o início do loop

            break  # encerra o loop de procura do cliente

    if cliente_encontrado:  # verifica se algum cliente foi encontrado
        reescrever_arquivo(clientes)  # reescreve o arquivo com os dados atualizados
        print(Fore.GREEN + "Cliente alterado com sucesso!\n" + Style.RESET_ALL)  # informa que a alteração foi realizada
    else:  # executa caso nenhum cliente tenha sido encontrado
        print(Fore.RED + "Erro: Cliente não encontrado!\n" + Style.RESET_ALL)  # exibe uma mensagem de erro

def excluir_cliente():  # define a função responsável por excluir um cliente
    listar_cliente()  # mostra a lista de clientes antes de realizar a exclusão
    clientes = ler_clientes_arquivo()  # lê os clientes salvos e armazena em uma lista
    if not clientes:  # verifica se não existem clientes cadastrados
        print(Fore.YELLOW + "Não há nenhum cliente cadastrado para excluir!\n" + Style.RESET_ALL)  # informa que não há clientes para excluir
        return  # encerra a função

    print(Fore.CYAN + "\nEXCLUIR CLIENTE" + Style.RESET_ALL)  # exibe o título da opção excluir
    email_busca = input("Digite o E-MAIL do cliente que deseja excluir: ").strip()  # solicita o email usado para localizar o cliente
    
    for i, cliente in enumerate(clientes):  # percorre a lista e também obtém a posição de cada cliente
        if cliente["email"] == email_busca:  # verifica se o email informado corresponde ao cliente atual
            print(Fore.YELLOW + f"Cliente encontrado: {cliente['nome'].upper()}" + Style.RESET_ALL)  # mostra o cliente encontrado
            confirmacao = input("Tem certeza que deseja excluir? (S/N): ").strip().lower()  # pede confirmação e transforma a resposta em letras minúsculas
            
            if confirmacao == 's':  # verifica se o usuário confirmou a exclusão
                del clientes[i]  # remove o cliente da lista usando sua posição
                reescrever_arquivo(clientes)  # atualiza o arquivo com a lista sem o cliente excluído
                print(Fore.GREEN + "Cliente excluído com sucesso!\n" + Style.RESET_ALL)  # mostra a mensagem de sucesso
            if confirmacao == "n":  # verifica se o usuário cancelou a exclusão
                print(Fore.YELLOW + "Exclusão cancelada pelo usuário.\n" + Style.RESET_ALL)  # informa que a exclusão foi cancelada
            else:  # executa quando a resposta não for a esperada
                print('Erro! Digite apenas "S" ou "N" ')  # mostra uma mensagem informando as opções válidas
            return  # encerra a função após encontrar o cliente

    print(Fore.RED + "Erro: Cliente não encontrado!\n" + Style.RESET_ALL)  # informa que nenhum cliente com aquele email foi encontrado


def menu():  # define a função responsável por exibir e controlar o menu principal
    largura = 70  # define a largura do menu como 70 caracteres
    while True:  # inicia um loop infinito para manter o menu funcionando
        print(Fore.CYAN + "=" * largura)  # imprime uma linha decorativa com 70 sinais de igual
        print("SISTEMA DE CLIENTES".center(largura))  # exibe o título centralizado dentro dos 70 caracteres
        print("=" * largura + Style.RESET_ALL)  # imprime outra linha decorativa e reseta a cor
        
        print(Fore.GREEN + "1. Cadastrar Cliente" + Style.RESET_ALL)  # exibe a opção de cadastrar cliente na cor verde
        print(Fore.CYAN + "2. Listar Clientes" + Style.RESET_ALL)  # exibe a opção de listar clientes na cor ciano
        print(Fore.LIGHTMAGENTA_EX + "3. Alterar Cliente" + Style.RESET_ALL)  # exibe a opção de alterar cliente na cor magenta
        print(Fore.RED + "4. Excluir Cliente" + Style.RESET_ALL)  # exibe a opção de excluir cliente na cor vermelha
        print(Fore.BLACK + "0. Sair" + Style.RESET_ALL)  # exibe a opção de sair do sistema
        
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL).strip()  # solicita ao usuário uma opção e remove espaços extras
        
        if opcao == "1":  # verifica se o usuário escolheu a opção 1
            cadastrar_clientes()  # chama a função responsável por cadastrar um cliente
        elif opcao == "2":  # verifica se o usuário escolheu a opção 2
            listar_cliente()  # chama a função responsável por listar os clientes
        elif opcao == "3":  # verifica se o usuário escolheu a opção 3
            alterar_cliente()  # chama a função responsável por alterar um cliente
        elif opcao == "4":  # verifica se o usuário escolheu a opção 4
            excluir_cliente()  # chama a função responsável por excluir um cliente
        elif opcao == "0":  # verifica se o usuário escolheu a opção 0
            print(Fore.LIGHTYELLOW_EX + "Sistema encerrando...\n" + Style.RESET_ALL)  # exibe uma mensagem informando que o sistema será encerrado
            break  # interrompe o loop e encerra o menu
        else:  # executa caso o usuário escolha uma opção que não existe
            print(Fore.RED + "Escolha uma opção valida!\n" + Style.RESET_ALL)  # mostra uma mensagem de erro