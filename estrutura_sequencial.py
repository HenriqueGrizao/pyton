# 1-Leia três números inteiros e imprima a média aritmética entre esses números.

a= int(input("1° Numero - "));
b= int(input("2° Numero - "));
c= int(input("3° Numero - "));

print((a+b+c)/3);

# 2-Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
# A idade da pessoa no ano atual
# A idade que a pessoa terá em 2050


anoNascimento = int(input("Digite o ano do seu nascimento - "));
ano = int(input("Digite o ano atual - "));

print(f"A sua idade é {ano - anoNascimento}, e em 2050 você vai ter {2050 - anoNascimento}");

# 3-Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação).
import math;
a= int(input("Coeficiente A => "));
b= int(input("Coeficiente B => "));
c= int(input("Coeficiente C => "));

delta = b**2 - 4*a*c;


print(f"O valor de X é : { ((-b + math.sqrt(delta)) / (2*a)):.2f},{((-b - math.sqrt(delta)) / (2*a)):.2f}")

# 4-Leia um número e imprima a tabuada de multiplicar deste número.
for i in range(1,11):
  print(str(5*i));

# 5- Receba um número positivo, calcule e mostre:
# O número digitado ao quadrado
# O número digitado ao cubo
# A raiz quadrada do número digitado
# A raiz cúbica do número digitado.

import math;
a= int(input("Digite um numero positivo: "));

print(f"{a}² = {a**2}");
print(f"{a}³ = {a**3}");
print(f"√{a} = {(math.sqrt(a)):.3f}");
print(f"√³{a} = {(a**(1/3)):.3f}");

# 6-Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom. Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta.

valor = float(input("Digite o valor da conta: "));

print(f"Valor gasto = {valor}");
print(f"gorgeta = {valor*0.1}");
print(f"Valor total = {valor*1.1}");

# 7. Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado. 

a= int(input("Digite um numero positivo: "));

print(f"Antecessor = {a-1}");
print(f"Sucessor = {a+2}");
print(f"Dobro = {a*2}");
print(f"Metade = {a/2}");

# 8. Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
# Peso ideal (P) = (72,7 * H) – 58. 


altura= float(input("Digite a sua altura(Homes): "));

print(f"Seu pesso ideal é: {(72.7*altura)-58}");

# 9. Faça o mesmo programa do item anterior, utilizando a fórmula para o cálculo do peso ideal para mulheres:
# Peso ideal (P) = (62,1 * H) – 44,7

altura= float(input("Digite a sua altura(Mulheres): "));

print(f"Seu pesso ideal é: {(62.1*altura)-44.7}");

# 10. Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
a= input("Digite o valor da variavel A: ");
b= input("Digite o valor da variavel B: ");

a, b = b, a;

print("Invertendo os valores..");
print(f"A={a} e b={b}");

# 11. Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato. Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.
votosA= int(input("Digite a quantidade de votos que o candidato A teve: "));
votosB= int(input("Digite a quantidade de votos que o candidato B teve: "));
totalVotos= int(input("Digite a quantidade total de votos: "));

print(f"O candidatos A teve: {(votosA*100)/totalVotos}% dos votos");
print(f"O candidatos B teve: {(votosB*100)/totalVotos}% dos votos");
print(f"O porcentual de votos nulos é: {((totalVotos-(votosA+votosB))*100)/totalVotos}%");