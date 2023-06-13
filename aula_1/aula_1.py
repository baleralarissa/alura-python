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

# + [markdown] id="_kwAaQ36gLQ1"
# # Sobre o notebook
#
# A "hora da prática" é uma atividade do curso de Python para Data Science da Alura que contém diversos desafios envolvendo os aprendizados de cada aula.
#
# O notebook "hora da pratica" é um notebook construído com espaço para as células dos desafios propostos no curso, com ele você tem espaço para construir e executar suas soluções

# + [markdown] id="Mc-KN0dA0Z83"
# ## Aula 1 - Introdução ao Python

# + [markdown] id="l5eLWf0W0ikn"
# ### Questão 1
#
# Imprima a frase `Escola de Dados da Alura!`

# + id="5pllxJ0h0-yA"
print("Escola de Dados da Alura")

# + [markdown] id="tQdX90Ue03c7"
# ### Questão 2
# Imprima na tela seu nome e seu sobrenome seguindo a estrutura abaixo:
# ```
# Nome: [seu nome]
# Sobrenome: [seu sobrenome]
# ```
#

# + id="RVw5iKn20_Ps"
print("Nome: Larissa")
print("Sobrenome: Balera")

# + [markdown] id="gfg-aiip03vC"
# ### Questão 3
# Imprima o seu primeiro nome letra a letra. Por exemplo, nome é Mirla, então eu obtenho a seguinte saída:
# ```
# M
# I
# R
# L
# A
# ```
#

# + id="v5bkrgf60_qx"
nome = "Larissa"
letras = list(nome)

for l in letras:
    print(l)

# + [markdown] id="oadrJbl704MM"
# ### Questão 4
# Imprima o dia do seu nascimento em formato `dia mês ano`. Os valores de dia e ano não podem estar entre aspas. O formato deve estar como no exemplo, supondo uma data de aniversário dia 28 de fevereiro de 2003:
# ```
# 28 fevereiro 2003
# ```

# + id="cx0KSsrq1ALD"
print(8, "fevereiro", 1997)

# + [markdown] id="3RgyMaan04TD"
# ### Questão 5
# Imprima em um único print o atual ano que você está fazendo esse curso, o valor do ano deve ser um dado numérico. A saída do print deve ser a seguinte:
# ```
# Ano atual: [ano]
# ```
#

# + id="UN77EfQ2d36Y"
import datetime 

hoje = datetime.date.today()
ano = hoje.year

print("Ano atual:", ano)

