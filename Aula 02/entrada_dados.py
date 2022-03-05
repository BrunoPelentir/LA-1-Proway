'''
Entrada de dados

Em Python, podemos obter as info. do usuário através da função input().
'''
nome = input("Digite seu nome: ")
print(nome)

# Type Casting - Convertendo os tipos de dados em tempo de execução (str para int)
idade = int(input("Digite sua idade: ")) 
print(type(idade))
ano_nascimento = 2022 - idade
print(ano_nascimento)

# Outros casts
a = str(3) # '3'
b = int("3") # 3
c = float("3") # '3'