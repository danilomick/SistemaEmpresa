import os  # importa o módulo os, que permite trabalhar com arquivos e pastas do sistema
from colorama import Fore, Style, init  # importa recursos do colorama para adicionar cores aos textos

init()  # inicia o colorama para permitir o uso das cores no terminal

ARQUIVO = "clientes.txt"  # cria uma variável que armazena o nome do arquivo onde os clientes serão salvos

def salvar_clientes_arquivo(nome, email, telefone):  # define a função responsável por salvar um cliente no arquivo
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:  # abre o arquivo no modo append para adicionar os dados
        arquivo.write(f"{nome};{email};{telefone}\n")  # escreve os dados do cliente no arquivo
