import csv
import random
from faker import Faker

fake = Faker()

# Número de linhas a serem geradas
num_linhas = 50

# Nome do arquivo CSV
nome_arquivo = "soda.csv"

# Cabeçalho do CSV
cabecalho = ["ID", "Volume_Refrigerante", "Temperatura_Envase", "Hora_Envase", "Peso_Tampinha"]

# Geração de dados
dados = []
for i in range(1, num_linhas + 1):
    linha = [
        i,
        random.randint(350, 360),  # Volume_Refrigerante entre 350 e 360 ml
        random.randint(5, 8),      # Temperatura_Envase entre 5 e 8 graus
        fake.time(pattern="%H:%M"),  # Hora_Envase no formato HH:MM
        random.randint(2, 4),      # Peso_Tampinha entre 2 e 4 gramas
    ]
    dados.append(linha)

# Escrevendo no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    
    # Escrevendo o cabeçalho
    escritor_csv.writerow(cabecalho)
    
    # Escrevendo os dados
    escritor_csv.writerows(dados)

print(f"{num_linhas} linhas foram geradas e salvas em {nome_arquivo}.")
