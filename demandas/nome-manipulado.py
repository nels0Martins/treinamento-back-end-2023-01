# Entrada: Nome completo 
# Imprimir: maiusculo, minusculo, quantidade de letras (sem espaços), quantidade de letras no primeiro nome

print()
nome = str(input("Qual é o seu nome?\n"))
stripado = nome.strip() # Retirando espaços necessários
replace = stripado.replace(' ', '') # Retirando espaços do meio
splitado = nome.split() # Dividindo a string em uma lista
print()
print("Analisando seu nome...")
print(f"Seu nome em letras maiúsculas: {stripado.upper()}.")
print(f"Seu nome em letras minúsculas: {stripado.lower()}.")
print(f"Quantidade de letras que seu nome possui ao todo: {len(replace)}!")
print(f"Quantidade de letras que o seu nome {splitado[0]} possui {len(splitado[0])}!")
# Uma contagem de letras pode ser feito assim também: len(nome) - count(' ')
print()