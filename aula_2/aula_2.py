# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + [markdown] id="D9e3FqhO1S3X"
# ## Aula 2 - Manipulando dados no Python

# + [markdown] id="n6o7C1Ze2cRe"
# ### Coleta e amostragem de dados

# + [markdown] id="sRneWag9PV5Q"
# #### Questão 1
# Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

# + id="dbX1fKqy2HnE"
nome = input("Digite seu nome: ")

print(f'Olá {nome}')

# + [markdown] id="BJ1SznEp70d5"
# #### Questão 2
# Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

# + id="jKz-0Sq8PFkp"
import datetime

nome = input("Digite seu nome: ")
ano = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.date.today()
ano_atual_ano = ano_atual.year
idade = ano_atual_ano - ano

print(f'Olá {nome}, você tem {idade} anos')

# + [markdown] id="2T0jNYZt70aa"
# #### Questão 3
# Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

# + id="pI4kHNzTPIXh"
import datetime

nome = input("Digite seu nome: ")
ano = int(input("Digite o ano de nascimento: "))
altura = float(input("Digite a sua altura: "))

ano_atual = datetime.date.today()
ano_atual_ano = ano_atual.year
idade = ano_atual_ano - ano

print(f'Olá {nome}, você tem {idade} anos e mede {altura}')



# + [markdown] id="mEBFwKkC70KP"
# ### Calculadora com operadores

# + [markdown] id="H-IV1oAPPSqK"
# #### Questão 1
#
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

# + id="Zb0W84sy8rnp"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))


def soma(var1, var2):
    valores = []

    valores.append(var1)
    valores.append(var2)

    resultado = sum(valores)
    print(resultado)


    
soma(var1, var2)


# + [markdown] id="LUoi2MOu70Em"
# #### Questão 2
# Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.

# + id="4FYjWyBS8rDm"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))
var3 = float(input("Valor 3: "))

def soma(var1, var2, var3):
    valores = []

    valores.append(var1)
    valores.append(var2)
    valores.append(var2)

    resultado = sum(valores)
    print(f'Você digitou os valores: {var1}, {var2}, {var3} e o resultado é {resultado}')


    
soma(var1, var2, var3)

# + [markdown] id="lezGctF07z8i"
# #### Questão 3
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

# + id="k0GE1z4w8p3J"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))


def sub(var1, var2):
    valores = []

    valores.append(var1)
    valores.append(var2)

    resultado = var1 - var2
    print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')


    
sub(var1, var2)

# + [markdown] id="wwMP-dPU7zxW"
# #### Questão 4
#
# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
#

# + id="GzFCVHfp8peZ"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))


def multiply(var1, var2):
    valores = []

    valores.append(var1)
    valores.append(var2)

    resultado = var1 * var2
    print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')


    
multiply(var1, var2)

# + [markdown] id="9kxyHxUo7zRD"
# #### Questão 5
#
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser `0`.
#

# + id="ytJ8l5KH8ozc"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))

def div(var1, var2):
    valores = []
    if var2 == 0:
        print('Valor inválido. O número deve ser maior do que 0')
    else:
        valores.append(var1)
        valores.append(var2)

        resultado = var1 / var2
        print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')

div(var1,var2)

# + [markdown] id="zkUSBTQq8Hxt"
# #### Questão 6
#
# Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
#

# + id="RPj36jq08oZp"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))


def expo(var1, var2):
    valores = []

    valores.append(var1)
    valores.append(var2)

    resultado = var1 ** var2
    print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')


    
expo(var1, var2)

# + [markdown] id="yiunIusZ8Huj"
# #### Questão 7
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser `0`.

# + id="UHK8xITf8oCg"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))

def div_int(var1, var2):
    valores = []
    if var2 == 0:
        print('Valor inválido. O número deve ser maior do que 0')
    else:
        valores.append(var1)
        valores.append(var2)

        resultado = var1 // var2
        print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')

div_int(var1,var2)

# + [markdown] id="z_D_JiLX8Hra"
# #### Questão 8
#
# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser `0`.

# + id="EWGJeukO8nqx"
var1 = float(input("Valor 1: "))
var2 = float(input("Valor 2: "))

def div_int(var1, var2):
    valores = []
    if var2 == 0:
        print('Valor inválido. O número deve ser maior do que 0')
    else:
        valores.append(var1)
        valores.append(var2)

        resultado = var1 % var2
        print(f'Você digitou os valores: {var1}, {var2} e o resultado é {resultado}')

div_int(var1,var2)

# + [markdown] id="RDRajNkU8N8N"
# #### Questão 9
#
# Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

# + id="H6F4Ojzt8nSR"
i = 0
notas = int(input("Quantas notas deseja inserir?: "))
valores = []

while i < notas:        
    nota= float(input("Digite o valor da nota: "))
    valores.append(nota)
    print(valores)
    i+= 1

media = round(sum(valores)/len(valores),2)
print(f'As notas inseridas foram {valores} e a média final é {media}')



# + [markdown] id="d7fjkne58N21"
# #### Questão 10
#
# Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

# + id="fwjoHlV48mkv"
numeros = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]

if len(numeros) != len(pesos):
    print("As listas de números e pesos devem ter o mesmo tamanho!")
else:
    soma_produtos = sum(n * p for n, p in zip(numeros, pesos))
    soma_pesos = sum(pesos)
    avg_w = soma_produtos / soma_pesos

    print(f'A média ponderada dos números é: {avg_w}')


# + [markdown] id="GNmbX1OU8N0V"
# ## Editando textos

# + [markdown] id="6wZ85mCsRCV0"
# #### Questão 1
#
# Crie uma variável chamada “`frase`” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

# + id="eRqr_gh-8mFy"
frase = 'Hello World'
print(frase)

# + [markdown] id="Aac17z-18Nwv"
# #### Questão 2
# Crie um código que solicite uma frase e depois imprima a frase na tela.

# + id="8zfE2hh98lb0"
frase = input("Digite uma frase: ")
print(frase)

# + [markdown] id="DXVzqpN58Ntr"
# #### Questão 3
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

# + id="d0VzoYP68k-I"
frase = input("Digite uma frase: ")
print(frase.upper())

# + [markdown] id="I12VeNPK8Nqb"
# #### Questão 4
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

# + id="KD8rNy2K8kox"
frase = input("Digite uma frase: ")
print(frase.lower())

# + [markdown] id="cRqngSE48Nog"
# #### Questão 5
#
# Crie uma variável chamada “`frase`” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

# + id="aSCpdF-o8kBs"
frase = "  Hello World  "
print(frase.strip())

# + [markdown] id="murIazpQ8Nkv"
# #### Questão 6
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

# + id="tHunjwuG8jNq"
frase = input("Digite uma frase: ")
print(frase.strip())

# + [markdown] id="eRxc2OeX8Nh2"
# #### Questão 7
#
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

# + id="DYm0_UwS8ih6"
frase = input("Digite uma frase: ")
print(frase.strip().lower())

# + [markdown] id="UKATLavs8NfI"
# #### Questão 8
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “`e`” trocadas pela letra “`f`”.

# + id="k64C5G5S8iLO"
frase = input("Digite uma frase: ")
print(frase.replace('e', 'f'))

# + [markdown] id="n_1SPchw8NdG"
# #### Questão 9
#
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “`a`” trocadas pela caractere  “`@`”.

# + id="msaDNm_p8h0D"
frase = input("Digite uma frase: ")
print(frase.replace('a', chr(64)))

# + [markdown] id="H3sTTjqI8Naa"
# #### Questão 10
#
#
# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “`s`” trocadas pelo caractere  “`$`”.

# + id="RPBIsWT68e-1"
frase = input("Digite uma frase: ")
print(frase.replace('s', chr(36)))
