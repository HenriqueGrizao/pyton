#Crie uma lista contendo 10 valores inteiros aleatórios, entre 1 e 20. Imprima:
# O maior valor, o menor valor, a soma e a média dos valores na lista
# Ordene a lista, e em seguida, a imprima em ordem crescente
# Imprima a lista em ordem decrescente
# Solicite ao usuário que informe um valor e imprima a quantidade de ocorrências do valor na lista. Imprima uma mensagem, caso o valor não se encontre na lista

import random

lista = random.sample(range(1, 21), 10)

print("Lista original:", lista)
maior_valor = max(lista)
print("Maior valor:", maior_valor)
menor_valor = min(lista)
print("Menor valor:", menor_valor)
soma_valores = sum(lista)
print("Soma dos valores:", soma_valores)
media_valores = soma_valores / len(lista)
print("Média dos valores:", media_valores)
lista_ordenada = sorted(lista)
print("Lista em ordem crescente:", lista_ordenada)
lista_decrescente = sorted(lista, reverse=True)
print("Lista em ordem decrescente:", lista_decrescente)
valor = int(input("Informe um valor: "))
ocorrencias = lista.count(valor)
if ocorrencias > 0:
    print(f"O valor {valor} ocorre {ocorrencias} vez(es) na lista.")
else:
    print("O valor não está presente na lista.")

# Crie duas listas com 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma que contenha a soma dos elementos de mesma posição das duas listas originais, e outra que contenha a multiplicação dos valores de mesma posição. Imprima em seguida as 3 listas.

import random

lista1 = random.sample(range(1, 101), 10)
lista2 = random.sample(range(1, 101), 10)

soma_lista = []
multiplicacao_lista = []

for i in range(len(lista1)):
    soma = lista1[i] + lista2[i]
    multiplicacao = lista1[i] * lista2[i]
    soma_lista.append(soma)
    multiplicacao_lista.append(multiplicacao)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Soma dos valores de mesma posição:", soma_lista)
print("Multiplicação dos valores de mesma posição:", multiplicacao_lista)

#Considere a seguinte lista: [10, 20, 30, 30, 30, 40, 10, 20]
	# Faça um programa que exclua todas as ocorrências do número 30 da lista

lista = [10, 20, 30, 30, 30, 40, 10, 20]

while 30 in lista:
    lista.remove(30)

print(lista)

# Crie uma lista contendo 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma para armazenar os valores pares da primeira lista, e outra para armazenar os valores ímpares. Imprima em seguida as 3 listas.]

import random

lista = random.sample(range(1, 101), 10)

pares = []
impares = []

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Lista original:", lista)
print("Valores pares:", pares)
print("Valores ímpares:", impares)

# Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
# 27/05/2023 – 27 de maio de 2023
# (dica: crie uma lista contendo o nome de cada mês do ano)


meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

data = input("Digite uma data no formato DD/MM/AAAA: ")

dia, mes, ano = data.split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)

data_extenso = f"{dia} de {meses[mes - 1]} de {ano}"
print("Data por extenso:", data_extenso)

# Faça um programa que gere uma lista contendo 6 números aleatórios, de 1 a 60, que serão jogados na Mega-Sena. Em seguida, solicite ao usuário os 6 números sorteados. Imprima a lista contendo os números jogados, e a quantidade de números acertados no sorteio.

import random

numeros_jogados = random.sample(range(1, 61), 6)

numeros_sorteados = []
for i in range(6):
    numero = int(input(f"Digite o número sorteado {i+1}/6: "))
    numeros_sorteados.append(numero)

print("Números jogados:", numeros_jogados)
print("Números sorteados:", numeros_sorteados)

acertos = 0
for numero in numeros_sorteados:
    if numero in numeros_jogados:
        acertos += 1

print("Quantidade de números acertados:", acertos)

#----- FUNÇÃO -----
# Faça um programa contendo funções que recebam:
# Um número inteiro e que retorne o dobro deste número
# Dois números inteiros e que retorne o maior entre eles
# Um número inteiro e que retorne o valor do fatorial deste número
# Um número inteiro e positivo, que retorne a soma dos elementos inteiros existentes entre 1 e o número (inclusive)
# Um número inteiro e que retorne True se o número for par, e False caso contrário

def dobrar_numero(numero):
    return numero * 2

def maior_entre_dois_numeros(num1, num2):
    return max(num1, num2)

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def somar_elementos_ate(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

def verificar_par(numero):
    return numero % 2 == 0