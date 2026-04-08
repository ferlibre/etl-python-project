import csv

clientes = []

# EXTRAÇÃO (ler o CSV)
with open("clientes.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        clientes.append(linha)

# TRANSFORMAÇÃO + CARGA
with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
    for cliente in clientes:
        nome = cliente["nome"]
        conta = cliente["conta"]
        
        mensagem = f"Olá {nome}, sua conta {conta} tem uma oferta especial!"
        
        print(mensagem)
        arquivo_saida.write(mensagem + "\n")