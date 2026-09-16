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
