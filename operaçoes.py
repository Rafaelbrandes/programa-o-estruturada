#Operaçãoes aritméticas
#dois operandos numéricos
x=10
y=5.0

print (x+y) #soma
print (x-y) #subtração
print (x*y) #multiplicação
print (x/y) #divisão
print (x**y) #potência
print (x//y) #divisão inteira
print (x%y) #módulo

# round(valor, número de digitos)
print(round(x-y, 2))

#um operando é uma str
print("-" + "-") #concatenação de strings
print("-" + 30) #multiplicação de strings

# operações de atribuição
x = 10

# mais comuns
x *=2  #x = x +2
x *=3  #x = x -3
#menos comuns
x *=5
x /=4
x **= 2
x //= 6
x %= 2
print(x)
print(y)

#operações de comparação
# resultam em valor booleano (true or false)
print(x > y) #maior que 
print(x >= y) #maior ou igual a
print(x < y) #menor que
print(x <= y) #menor ou igual a
print(x == y) #igual a
print(x != y) #diferente de

#comparação entre strings - tabela ASCII
# https://pt.wikipedia.org/wiki/ASCII

print("-"*30)
x= "fbc"
y = "abc"
print(x > y) #maior que 
print(x >= y) #maior ou igual a
print(x < y) #menor que
print(x <= y) #menor ou igual a
print(x == y) #igual a
print(x != y) #diferente de

# operadores lógicos
print("-" * 30)

x=True
y=False
print (x and y) #E
print (x or y) #OU
print (not y) #NÃO

# type casting
x = 9
print(float(x))
print(int("10"))

# em python, tudo que for diferente de "", 0, 0,0, é true
print(bool(x))
print(bool(0))

print("abc" and 16)
print(0 and 16)
print(False and 16)
print("" and 16)

print("abc" or 16)
print(10,5 or 16)
print(True or 16)
print("" or 16)

# isso sobe ums exeção se o primeiro operando for false
print(6 or int("a"))

# pythonico
nome = input("informe o seu nome:") or "valor inválido"

print(nome)

"""
precedência

()
**
* / // &
+ -
> >=< <= == !=
not
and or
"""