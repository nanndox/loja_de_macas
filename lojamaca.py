# 1. Boas-vindas e pergunta o nome
print("********************************************")
print("**    BEM-VINDOS À NOSSA LOJA DE MAÇÃ    **")
print("********************************************\n")

# 2. Pergunta o nome do cliente
print("Por favor, digite o seu nome:")
nome = input()                          # guarda o que a pessoa escreveu
print("Por favor, digite o seu sobrenome:")
sobrenome = input() 
# 3. Cumprimenta pelo nome e mostra quantas maçãs temos
print(f"\nOlá {nome}! Tudo bem?")
print(f"Atualmente temos 20 maçãs disponíveis.")
print(f"Cada maçã custa 5 euros.\n")

# Quantidade inicial de maçãs e preço
macas_disponiveis = 20
preco_por_maca = 5

# 4. Pergunta quantas maçãs a pessoa quer comprar
print("Quantas maçãs você deseja comprar agora?")
quantidade = int(input())               # transforma o texto em número

# 5. Calcula o preço total
preco_total = quantidade * preco_por_maca

# 6. Mostra o que foi comprado e o valor total
print(f"\nVocê comprou {quantidade} maçãs.")
print(f"O preço total é: {preco_total} Euros.")

# 7. Atualiza e mostra quantas maçãs sobraram na loja
macas_disponiveis = macas_disponiveis - quantidade
# ou mais curto: macas_disponiveis -= quantidade

print(f"Agora restam {macas_disponiveis} maçãs na loja.")
print("Obrigado pela compra e volte sempre!")