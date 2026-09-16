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
