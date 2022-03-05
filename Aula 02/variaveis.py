'''
Variáveis 

As variáveis são espaços na memória que sua aplicação utiliza para armazenar os dados em tempo de execução.


Regras de nomenclatura:
   *Não pode começar com símbolos (exceção do_) e números.
   *Os nomes devem ser descritivos e de simples entendimentos
   *Cada nova palavra da variável deve ser separada por _. (Python) 
   
   Linguagens dinâmicamente tipadas x linguagens estaticamente tipadas.

'''




nome: str = "Bruno"
cpf: str = "090.200.019-57"
idade: int = 19
altura: float = 1,80
presente: bool = True
vazio = None

print(cpf)
print(type(nome))
print(type(vazio))
print(hex(id(cpf)))

valor1, valor2 = 10, 20
print(valor1, valor2)

a, b = 1, 2
auxiliar = a # a = 1, b = 2, auxiliar = 1
a = b # a = 2, b = 2, auxiliar = 1
b = auxiliar # a = 2, b = 1, auxiliar = 1
print(a, b)

# ação exclusiva do Python (simplificar/resumir)
c, d = 1, 2
d, c = c, d
print(c, d)  
