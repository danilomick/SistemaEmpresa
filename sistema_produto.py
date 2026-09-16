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
            
def cadastro_quantidade(nome_produto):
    while True:
        quant = input(f"Digite a quantidade de {nome_produto}: ").strip()
        
        if len(quant) == 0:
            print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL)
            continue
            
        try:
            # quantidade é convertido em int agora, porque não é aceito strip em entrada int
            quantidade = int(quant)
            if quantidade < 0:
                print(Fore.RED + "Erro! A quantidade não pode ser negativa.\n" + Style.RESET_ALL)
                continue
            return quantidade 
        except ValueError:
            print(Fore.RED + "Erro! Quantidade inválida. Digite um número inteiro.\n" + Style.RESET_ALL)
            
def iniciar_sistema_produto():
    produto = cadastro_produto()
    valor = cadastro_valor(produto)
    quantidade = cadastro_quantidade(produto)
    
    with open(arquivo_dados, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Produto: {produto}; Valor: R${valor:.2f}; quantidade: {quantidade}\n")
        
    print(Fore.GREEN + f"\nSucesso! {produto} foi cadastrado no sistema.\n" + Style.RESET_ALL)

def lista_produtos():
    if not os.path.exists(arquivo_dados):
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL)
        return
    
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        
    if len(linhas) == 0:
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL)
        return
    
    largura = 70 
    
    print(Fore.CYAN + "=" * largura)
    print("PRODUTOS CADASTRADOS".center(largura))
    print("=" * largura + Style.RESET_ALL)
    
    # As larguras de colunas definidas aqui (25, 20, 25)
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}")
    print("-" * largura)
    
    for linha in linhas:
        dados = linha.strip().split(";")
        
        if len(dados) == 3: 
            
            # Remove os prefixos para o terminal, assim a tabela não quebra o alinhamento
            nomeProduto = dados[0].replace("Produto:", "").strip()
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").strip()
            quantidadeProduto = dados[2].replace("quantidade:", "").strip()
            
            valorExibicao = f"R$ {valorProduto}".replace(".",",")
                
            print(f"{nomeProduto:<25}{valorExibicao:<20}{quantidadeProduto:<25}")       
    print()
    
def alterar_produto():
    if not os.path.exists(arquivo_dados):
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL)
        return
    
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
            
    if len(linhas) == 0:
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL)
        return
    
    largura = 70
    print(Fore.CYAN + "=" * largura)
    print("PRODUTOS CADASTRADOS".center(largura))
    print("=" * largura + Style.RESET_ALL)
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}")
    print("-" * largura)
    
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            nomeProduto = dados[0].replace("Produto:", "").strip()
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").replace(".",",").strip()
            quantidadeProduto = dados[2].replace("quantidade:", "").strip()
            print(f"{nomeProduto:<25}R$ {valorProduto:<17}{quantidadeProduto:<25}")
            
    encontrado = input(Fore.LIGHTBLUE_EX + "\nDigite o nome do produto que deseja alterar: " + Style.RESET_ALL).strip().title()
    lista_nova = []
    produto_achado = False
    
    for linha in linhas:
        dados = linha.strip().split(";")
        
        if len(dados) == 3:
            nome_atual = dados[0].replace("Produto:", "").strip().title()
            valor_atual = dados[1].replace("Valor:", "").replace("R$", "").strip()
            quant_atual = dados[2].replace("quantidade:", "").strip()
            
            if nome_atual == encontrado:
                produto_achado = True
                
                while True:   
                    novo_nome = input(Fore.LIGHTBLUE_EX + f"Digite o novo nome (Atual: {nome_atual}): " + Style.RESET_ALL).strip().title()
                    if len(novo_nome) == 0 or not novo_nome.replace(" ", "").isalpha():
                        print(Fore.RED + "Erro: Nome inválido. Digite apenas letras.\n" + Style.RESET_ALL)
                    else:
                        break
                        
                while True:
                    preco = input(Fore.LIGHTBLUE_EX + f"Digite o novo valor (Atual: R${valor_atual}): " + Style.RESET_ALL).strip().replace(',', '.')
                    if len(preco) == 0:
                        print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL)
                        continue 
                    try:
                        novo_valor = float(preco)
                        if novo_valor <= 0:
                            print(Fore.RED + "Erro! O valor deve ser maior que zero\n" + Style.RESET_ALL)
                            continue
                        break
                    except ValueError:
                        print(Fore.RED + "Erro: Digite somente números válidos.\n" + Style.RESET_ALL)
                        
                while True:
                    quant = input(Fore.LIGHTBLUE_EX + f"Digite a nova quantidade (Atual: {quant_atual}): " + Style.RESET_ALL).strip()
                    if len(quant) == 0:
                        print(Fore.RED + "Erro! Este campo não pode ficar em branco.\n" + Style.RESET_ALL)
                        continue 
                    try:
                        nova_quantidade = int(quant)
                        if nova_quantidade < 0:
                            print(Fore.RED + "Erro! A quantidade não pode ser negativa.\n" + Style.RESET_ALL)
                            continue
                        lista_nova.append(f"Produto: {novo_nome}; Valor: R${novo_valor:.2f}; quantidade: {nova_quantidade}\n")
                        print(Fore.GREEN + "Produto alterado com sucesso!\n" + Style.RESET_ALL)
                        break
                    except ValueError:
                        print(Fore.RED + "Erro: Digite um número inteiro válido.\n" + Style.RESET_ALL)
            else:
                lista_nova.append(linha)
                
    if produto_achado:
        with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(lista_nova)
    else:
        print(Fore.LIGHTYELLOW_EX + f"Produto '{encontrado}' não foi encontrado no sistema.\n" + Style.RESET_ALL)
        
def excluir_produto():
    if not os.path.exists(arquivo_dados):
        print(Fore.LIGHTYELLOW_EX + "Nenhum arquivo de cadastro foi criado\n" + Style.RESET_ALL)
        return
        
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
                
    if len(linhas) == 0:
        print(Fore.LIGHTYELLOW_EX + "Nenhum produto cadastrado\n" + Style.RESET_ALL)
        return
    
    largura = 70
    print(Fore.CYAN + "=" * largura)
    print("PRODUTOS CADASTRADOS".center(largura))
    print("=" * largura + Style.RESET_ALL)
    print(f"\n{'PRODUTO':<25}{'VALOR':<20}{'QUANTIDADE':<25}")
    print("-" * largura)
    
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            nomeProduto = dados[0].replace("Produto:", "").strip()
            valorProduto = dados[1].replace("Valor:", "").replace("R$", "").replace(".",",").strip()
            quantidadeProduto = dados[2].replace("quantidade:", "").strip()
            print(f"{nomeProduto:<25}R$ {valorProduto:<17}{quantidadeProduto:<25}")
            
    encontrado = input(Fore.LIGHTMAGENTA_EX + "\nDigite o nome do produto que deseja EXCLUIR: " + Style.RESET_ALL).strip().title()
    
    lista_nova = []
    produto_achado = False
    
    for linha in linhas:
        dados = linha.strip().split(";")
        
        if len(dados) == 3:
            nome_atual = dados[0].replace("Produto:", "").strip().title()
            
            if nome_atual == encontrado:
                produto_achado = True
                print(Fore.GREEN + f"Produto '{nome_atual}' excluído com sucesso!\n" + Style.RESET_ALL)
            else:
                # Se não for o produto procurado, adicionamos ele na lista nova para ser mantido
                lista_nova.append(linha)
                
    #Salvamos as alterações caso algo tenha sido excluído
    if produto_achado:       
        with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(lista_nova)
    else:
        print(Fore.LIGHTYELLOW_EX + f"Produto '{encontrado}' não encontrado.\n" + Style.RESET_ALL)
        