import os #importa o sistema operacional
from colorama import Fore, Style, init #importa as funções do colorama

init() #inicia o colorama 
arquivo_dados = "Produtos.txt" #variavel que armazena o arquivo 

def cadastro_produto():#define uma função para começar o cadastro do produto validando o nome
    while True: #incia um loop para validar o nome do produto
        produto = input("Digite o nome do produto que será cadastrado: ").title().strip() #pede que o usuario digite o nome do produto
        
        if len(produto) == 0: #verifica se o campo foi preenchido
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL) #mensagem de erro caso o campo não foi preenchido
        elif not produto.replace(" ", "").isalpha(): #verifica se o nome do produto só contem letras, ignorando espaçamentos
            print(Fore.RED + "Erro! Digite somente letras.\n" + Style.RESET_ALL) #mensagem de erro caso o usuario não digite somente letrs
        else: #se der tudo certo
            return produto #retornar a função
        
def cadastro_valor(nome_produto): #define uma função para validar o valor do produto
    while True: #incia um loop para validar o valor do produto
        preco = input(Fore.LIGHTWHITE_EX+f"Digite o valor de {nome_produto}: "+ Style.RESET_ALL).strip().replace(',', '.') #pede que o usuario digte o valor do produto
        
        if len(preco) == 0: #verifica se o campo foi preenchido
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL) #mensagem de erro caso o campo não foi preenchido
            continue #continua o loop
            
        try: #verifica se o valor é valido
            valor = float(preco) #converte o valor para float para ver se ele é valido
            if valor <= 0: #ve se valor é maior ou igual a 0
                print(Fore.RED + "Erro! O valor deve ser maior que zero\n" + Style.RESET_ALL) #mensagem de erro caso valor for 0 ou negativo
                continue #continua o loop
            return valor #retorna a função
        except ValueError: #se der erro convertendo a float
            print(Fore.RED + "Erro! Valor inválido. Digite um número.\n" + Style.RESET_ALL) #mensagem de erro dizendo que o valor está invalido
            
def cadastro_quantidade(nome_produto): #define uma função para validar a quantidade do produto
    while True: #inicia um loop para validar a quantidade do produto
        quant = input(f"Digite a quantidade de {nome_produto}: ").strip() #pede que o usuario digite a quantidade do produto
        
        if len(quant) == 0: #verifica se o campo foi preenchido
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL) #mensagem de erro caso o campo não foi preenchido
            continue #continua o loop
            
        try: #verifica se a quantidade é valida
            quantidade = int(quant) #verifica se o número digitado é inteiro
            if quantidade < 0: #verifica se a quantidade é menor que 0
                print(Fore.RED + "Erro! A quantidade não pode ser negativa.\n" + Style.RESET_ALL) #mensagem de erro caso a quantidade for menor que 0
                continue #continua o loop
            return quantidade #retorna a função
        except ValueError: #se a quantidade der erro quando for convertida para float
            print(Fore.RED + "Erro! Quantidade inválida. Digite um número inteiro.\n" + Style.RESET_ALL) #mensagem de erro caso a quantidade não for numero inteiro
            
def iniciar_sistema_produto(): #define a função de iniciar o sistema
    produto = cadastro_produto() #faz com que o resultado de cadastro produto seja guardado na variavel produto
    valor = cadastro_valor(produto) #faz com que o resultado de cadastro valor seja guardado na variavel valor
    quantidade = cadastro_quantidade(produto) #faz com que o resultado de cadastro de quantidade seja guardado na variavel quantidade
    #OBS - O (produto), usa o produto cadastrado como base 
    with open(arquivo_dados, "a", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de adicionar dados
        arquivo.write(f"Produto: {produto}; Valor: R${valor:.2f}; quantidade: {quantidade}\n") #escreve as informações no arquivo
        
    print(Fore.GREEN + f"\nSucesso! {produto} foi cadastrado no sistema.\n" + Style.RESET_ALL) #mensagem de sucesso dizendo que o produto foi cadastrado no arquivo

def lista_produtos(): #define a função de listar produtos
    if not os.path.exists(arquivo_dados): #verifica se o arquivo de cadastro de produtos foi criado 
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL) #mensagem de alerta caso o arquivo não foi criado
        return #retorna a função
    
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de leitura
        linhas = arquivo.readlines() #le as linhas do arquivo com ele aberto
        
    if len(linhas) == 0: #ve se existe alguma linha no arquivo
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL) #mensagem de alerta caso não houver nenhum produto cadastrado
        return #retorna a funçao
    
    largura = 70 # define largura de 70 caracteres
    
    print(Fore.CYAN + "=" * largura) #decoração em ciano de 70 caracters
    print("PRODUTOS CADASTRADOS".center(largura)) #titulo de exibição em ciano
    print("=" * largura + Style.RESET_ALL) # decoração em ciano de 70 caracteres
    
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}")  #as larguras de colunas definidas aqui (25, 20, 25)
    print("-" * largura) #imprime 70 vezes - como decoração
    
    for linha in linhas: #inicia um loop para percorrer cada linha da lista linhas
        dados = linha.strip().split(";") #remove espaços e quebras de linhas nas pontas
        
        if len(dados) == 3: #verifica se tem os 3 dados esperados  
            
            nomeProduto = dados[0].replace("Produto:", "").strip() #remove o texto produto e remove espaços em branco
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").strip() #remove o texto valor e o R$, removendo espaços em branco
            quantidadeProduto = dados[2].replace("quantidade:", "").strip() #remove o texto quantidade e remove os espaços em branco
            
            valorExibicao = f"R$ {valorProduto}".replace(".",",") #adiciona o simbolo R$ e troca . por ,
                
            print(f"{nomeProduto:<25}{valorExibicao:<20}{quantidadeProduto:<25}") #as larguras de colunas definidas aqui (25, 20, 25)  
    print() #imprime linha em branco para espaçar
    
def alterar_produto(): #define a função de alterar produto
    if not os.path.exists(arquivo_dados): #verifica se o arquivo do cadastro de produto existe
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL) #mensagem de alerta caso o arquivo não tiver sido criado
        return #retorna a função
    
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de leitura
        linhas = arquivo.readlines() #le as linhas do arquivo com ele aberto
            
    if len(linhas) == 0: #verifica se o arquivo está vazio
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL) #mensagem de alerta caso não houver nenhum produto cadastrado
        return #retorna a função
    
    largura = 70 #define largura de 70 caracteres
    print(Fore.CYAN + "=" * largura) #decoração de 70 caracteres em ciano
    print("PRODUTOS CADASTRADOS".center(largura)) #titulo de exibição em ciano
    print("=" * largura + Style.RESET_ALL) #decoração de 70 caracteres em ciano
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}") #as larguras de colunas definidas aqui (25, 20, 25) 
    print("-" * largura) #imprime 70 vezes - como decoração
    
    for linha in linhas:# inicia um loop para percorrer cada linha em linhas
        dados = linha.strip().split(";") #remove espaços e quebras de linhas nas pontas
        if len(dados) == 3: #verifica se tem os 3 dados esperados
            nomeProduto = dados[0].replace("Produto:", "").strip() #remove o texto produto e os espaços em branco
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").replace(".",",").strip() #remove valor e o simbolo R$, substituindo . por , e removendo os espaços em branco
            quantidadeProduto = dados[2].replace("quantidade:", "").strip() #remove quantidade e remove os espaços em branco
            print(f"{nomeProduto:<25}R$ {valorProduto:<17}{quantidadeProduto:<25}") #as larguras de colunas definidas aqui (25, 17, 25) 
            
    encontrado = input(Fore.LIGHTBLUE_EX + "\nDigite o nome do produto que deseja alterar: " + Style.RESET_ALL).strip().title() #pede para digitar o nome do produto a ser alterado
    lista_nova = [] #cria uma nova lista para armazenar as linhas atualizadas
    produto_achado = False #indica se o produto foi encontrado ou não
    
    for linha in linhas: #inicia um loop para percorrer cada linha em linhas
        dados = linha.strip().split(";") #remove quebras de linha e espaços nas pontas
        
        if len(dados) == 3: #verifica se tem os 3 dados esperados
            nome_atual = dados[0].replace("Produto:", "").strip().title() #remove o texto produto e os espaços em branco, deixando a primeira letra maiuscula
            valor_atual = dados[1].replace("Valor:", "").replace("R$", "").strip() #remove o valor e o simbolo R$ e espaços em brancos
            quant_atual = dados[2].replace("quantidade:", "").strip() #remove quantidade e remove espaços em branco
            
            if nome_atual == encontrado: #se o nome atual foi encontrado
                produto_achado = True #marca que o produto foi encontrado

                while True: #inicia um loop para validar o novo nome
                    novo_nome = input(Fore.LIGHTBLUE_EX + f"Digite o novo nome (Atual: {nome_atual}): " + Style.RESET_ALL).strip().title() #pede que o usuario digite o novo noem do produto, removendo espaços em branco e deixando a primeira letra maiuscula
                    if len(novo_nome) == 0 or not novo_nome.replace(" ", "").isalpha(): #verifica se o campo foi prenchido e se o novo nome contem apenas letras do alfabeto ignorando espaçamentos
                        print(Fore.RED + "Erro: Nome inválido. Digite apenas letras.\n" + Style.RESET_ALL) # mensagem de erro caso o campo estiver em branco, ou não conter apenas letras
                    else: #caso o nome for valido
                        break #para o loop
                        
                while True: #inicia um loop para validar o novo valor 
                    preco = input(Fore.LIGHTBLUE_EX + f"Digite o novo valor (Atual: R${valor_atual}): " + Style.RESET_ALL).strip().replace(',', '.') #pede que o usuario digite o novo valor, removendo os espaços em branco e substituindo a , por .
                    if len(preco) == 0: #verifica se o campo foi preenchido
                        print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL) #mensagem de erro caso o campo não foi preenchido
                        continue # continua o loop
                    try: #verifica se o novo valor é valido
                        novo_valor = float(preco) #converte o novo valor para floar
                        if novo_valor <= 0: #verifica se o novo valor é menor ou igual a 0 
                            print(Fore.RED + "Erro! O valor deve ser maior que zero\n" + Style.RESET_ALL) #mensagem de erro caso o novo valor for negativo ou 0
                            continue #continua o loop
                        break #para o loop
                    except ValueError: # caso der erro na conversão para float
                        print(Fore.RED + "Erro: Digite somente números válidos.\n" + Style.RESET_ALL) #mensagem de erro caso o usuario não digitar numeros validos
                        
                while True: #inicia um loop para validar a nova quantidade 
                    quant = input(Fore.LIGHTBLUE_EX + f"Digite a nova quantidade (Atual: {quant_atual}): " + Style.RESET_ALL).strip() #pede que o usuario digite a nova quantidade 
                    if len(quant) == 0: #verifica se o campo foi preenchido
                        print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL) #mensagem de erro caso o campo ficar em branco
                        continue #continua o loop
                    try: #tenta validar a nova quantidade
                        nova_quantidade = int(quant) #converte a nova quantidade para inteiro
                        if nova_quantidade < 0: #verifica se a nova quantidade é menor que 0
                            print(Fore.RED + "Erro! A quantidade não pode ser negativa.\n" + Style.RESET_ALL) #mensagem de erro caso a quantidade for menor que 0
                            continue #continua o loop
                        lista_nova.append(f"Produto: {novo_nome}; Valor: R${novo_valor:.2f}; quantidade: {nova_quantidade}\n") #insere a nova linha na nova lista
                        print(Fore.GREEN + "Produto alterado com sucesso!\n" + Style.RESET_ALL) #mensagem de sucesso quando registra os novos dados
                        break #para o loop
                    except ValueError: #caso der erro convertendo a quantidade para inteiro
                        print(Fore.RED + "Erro: Digite um número inteiro válido.\n" + Style.RESET_ALL) #mensagem de erro pedindo para digitar um valor válido
            else:
                lista_nova.append(linha) #insere a nova linha na nova lista
                
    if produto_achado: #se o produto foi encontrado
        with open(arquivo_dados, "w", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de escrita
            arquivo.writelines(lista_nova) #escreve os dados alterados na nova lista
    else: #caso não encontrar o produto
        print(Fore.LIGHTYELLOW_EX + f"Produto '{encontrado}' não foi encontrado no sistema.\n" + Style.RESET_ALL) #mensagem de alerta dizendo que o produto não foi cadastrado no sistema
        
def excluir_produto(): #define a função de excluir o produto
    if not os.path.exists(arquivo_dados): #verifica se o arquivo de cadastro de produtos existe
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL) #mensagem de alerta caso o arquivo não existir
        return #retorna a função
        
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de leitura
        linhas = arquivo.readlines() #le as linhas do arquivo
                
    if len(linhas) == 0: #verifica se existe alguma linha no arquivo
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL) #alerta caso nenhuma linha seja encontrada
        return #retorna a função
    
    largura = 70 #define largura de 70 caracteres
    print(Fore.CYAN + "=" * largura) #decoração de 70 caracteres em ciano
    print("PRODUTOS CADASTRADOS".center(largura)) #titulo de exibição em ciano
    print("=" * largura + Style.RESET_ALL) #decoração de 70 caracteres em ciano
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}") #as larguras de colunas definidas aqui (25, 20, 25)
    print("-" * largura) #imprime 70 vezes - como decoração
    
    for linha in linhas: #inicia um loop para percorrer todas as linhas em linhas
        dados = linha.strip().split(";") #remove quebras de linha e espaços nas pontas
        if len(dados) == 3: #verifica se tem os 3 dados esperados
            nomeProduto = dados[0].replace("Produto:", "").strip() #remove o texto produto e os espaços e, branco
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").replace(".",",").strip() #remove o texto valor e o simbolo R$, substituindo . por , e remove espaços em branco
            quantidadeProduto = dados[2].replace("quantidade:", "").strip() #remove o texto quantidade e os espaços em branco
            print(f"{nomeProduto:<25}R$ {valorProduto:<17}{quantidadeProduto:<25}") #as larguras de colunas definidas aqui (25,17,25)
            
    encontrado = input(Fore.LIGHTMAGENTA_EX + "\nDigite o nome do produto que deseja EXCLUIR: " + Style.RESET_ALL).strip().title() #solicita que o usuario digite o noem do produto que deseja excluir
    
    lista_nova = [] #cria uma nova lista para armazenar as linhas atualizadas
    produto_achado = False #indica se o produto foi encontrado ou não
    
    for linha in linhas: #inicia um loop para percorrer cada linha em linhas 
        dados = linha.strip().split(";") #remove quebras de linha e espaços nas pontas
        
        if len(dados) == 3: #verifica se tem os 3 dados esperados
            nome_atual = dados[0].replace("Produto:", "").strip().title() #remove o texto produto, remove o espaço em branco e deixa a primeira letra em maiusculo
            
            if nome_atual == encontrado: #se o nome atual foi encontrado
                produto_achado = True #marca que o produto foi encontrado
                print(Fore.GREEN + f"Produto '{nome_atual}' excluído com sucesso!\n" + Style.RESET_ALL) #mensagem de sucesso dizendo que o produto foi excluido
            else: #se o produto não for encontrado 
                lista_nova.append(linha) #deixa o produto na lista nova
                
    if produto_achado: #se o produto foi encontrado       
        with open(arquivo_dados, "w", encoding="utf-8") as arquivo: #abre o arquivo com o metodo de escrita
            arquivo.writelines(lista_nova) #escreve as linhas novas apagando o produto excluido
    else: #caso produto não for encontrado
        print(Fore.LIGHTYELLOW_EX + f"Produto '{encontrado}' não encontrado.\n" + Style.RESET_ALL) #mensagem de alerta dizendo que o produto não foi encontrado
        
def menu_inicial(): #define a função menu inicial
    largura = 70 #define largura de 70 caracteres
    
    print(Fore.CYAN + "="*largura) #decoração em ciano de 70 caracteres
    print("CADASTRO DOS PRODUTOS".center(largura)) #titulo do menu em ciano
    print("="*largura + Style.RESET_ALL) #decoração em ciano de 70 caracteres
    print(Fore.GREEN+"1.Cadastrar Produto"+Style.RESET_ALL) #opção 1 de cadastrar produtos em verde
    print(Fore.CYAN+"2.listar Produtos"+Style.RESET_ALL) #opção 2 listar produtos em ciano
    print(Fore.LIGHTMAGENTA_EX+"3.Alterar Produto"+Style.RESET_ALL) #opção 3 alterar prodtuos em magenta claro
    print(Fore.RED+"4.Excluir Produto"+Style.RESET_ALL) #opção 4 excluir produto em vermelho
    print(Fore.BLACK+"0.Sair"+Style.RESET_ALL) #opção 0 sair em preto
    
def main_produto(): #define a função main, que chama as opções
    while True: #inicia um loop para escolher uma opção enquanto o menu roda
        menu_inicial() #chama o menu inicial
        
        try: #iniia um loop para validar a opção
            escolha = int(input("\nEscolha alguma das opções: ")) #solicita que o usuario digite uma das opções
        except ValueError: #se o valor não for inteiro
            print(Fore.RED + "Erro: Digite apenas números.\n" + Style.RESET_ALL) #mensagem de erro dizendo para digitar apenas numeros
            continue #continua o loop
            
        if escolha < 0 or escolha > 4: #verifica se a escolha esta entre 0 e 4
            print(Fore.RED + "Escolha uma opção válida\n" + Style.RESET_ALL) #mensagem de erro caso não estiver
            
        elif escolha == 1: #caso escolha for 1
            iniciar_sistema_produto() #inicia o sistema de cadastro
            
        elif escolha == 2: #caso escolha for 2 
            lista_produtos() #inicia a função de listar produto
        
        elif escolha == 3: #caso escolha for 3
            alterar_produto() #inicia a função de alterar o produto
            
        elif escolha == 4: #caso escolha for 4
            excluir_produto() #inicia a funçãod e excluir o produto
        
        elif escolha == 0: #caso escolha for 0
            print(Fore.LIGHTYELLOW_EX + "Sistema encerrando..." + Style.RESET_ALL) #encerra o sistema
            break #para o loop