'''
Operadores aritméticos

Os operadores aritméticos são utilizados para executar as operações que
 a sua aplicação utilizar para gerar um resultado

 Básicos:
    * Adição: + 
    * Subtração: -
    * Divisão: /
    * Divisão inteira: //
    * Multiplicação: *
    * Módulo: % (Resto da divisão)
    * Exponenciação: **

Atribuição:
    * x += 3 -> x = x + 3
    * x -= 3 -> x = x - 3 
    * x /= 3 -> x = x / 3
    * x //= 3 -> x = x // 3
    * x *= 3 -> x = x * 3
    * x %= 3 -> x = x % 3
    * x **= 3 -> x = x ** 3

Precedência de operadores: 
    1. () -> Agrupamento
    2. ** -> Exponenciação           
    3. *, /, %, // -> Multiplicação, Divisão, Resto e Divisão inteira
    4. +, - -> Soma e subtração 

'''
n1, n2 = 8, 6
media = (n1 + n2) / 2
print(media)
print(f"O valor da variável teste é: {media:.3f}")