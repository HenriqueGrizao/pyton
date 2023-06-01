#----- WHILE -----
# 1. Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa. 
matricula = int(input("Digite a matricula ou um número negativo para encerar :"))
while(matricula > 0):
  

  a= float(input("1° Nota - "));
  b= float(input("2° Nota - "));
  c= float(input("3° Nota - "));

  media = (a+b+c)/3;

  if(media >= 70):
    print(f"aprovado com {media}")
  elif(media >= 60):
    print(f"Exame com {media}")
  else:
    print(f"Reprovado {media}")
    
  
  matricula = int(input("Digite a matricula ou um número negativo para encerar :"));

# 2. Leia a idade de um número indeterminado de pessoas. Imprima:
# - Quantas pessoas possuem idade acima de 50 anos
# - A média de idade das pessoas
# - O percentual de pessoas com idade abaixo de 40 anos
# A leitura será encerrada quando o usuário informar uma idade negativa.

idade = int(input("Digite a idade ou um número negativo para encerar :"));
contador = 0;
idadeCinquenta = 0;
idadequarenta = 0;
idadeTotal = 0;
while(idade > 0):
  contador = contador + 1;
  idadeTotal += idade

  if(idade >= 50):
    idadeCinquenta = idadeCinquenta + 1
  elif(idade <= 40):
    idadequarenta = idadequarenta + 1

  idade = int(input("Digite a idade ou um número negativo para encerar :"));
print(idadeCinquenta);
print(idadeTotal/contador);
print((idadequarenta*idadeTotal)/100);

# 3. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber: 
# a ) A média do salário da população; 
# b ) A média do número de filhos. 
# O final da leitura de dados dar-se-á com a entrada de salários negativos. 

salarios = 0
filhos = 0
salario = int(input("Digite o salário ou um número negativo para encerar :"));
contador = 0;
while(salario > 0):
  salarios += salario
  filho = int(input("Digite o numero de filhos"));
  filhos += filho
  contador = contador + 1;
  salario = int(input("Digite o salário ou um número negativo para encerar :"));
print(salarios/contador);
print(filhos/contador);

#----- FOR -----

# 1. Faça um programa que faça a leitura de 5 valores, e para cada valor, mostre o seu dobro na tela. 

for i in range(1,6):
  print( 2* int(input("Digite o valor: ")))

# 2. Faça um programa que leia um número e que imprima os números ímpares de 1 até o número informado. 

a = int(input("Digite um numero "));
for i in range(1,a,2):
  print(i);

# 3. Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:

a = int(input("Digite um numero "));
for i in range(1,11):
  print(f"{a} * {i} = {a * i}");

# 4. Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados.

a = int(input("Digite um numero "));
b = int(input("Digite um numero "));
for i in range(a,b):
  print(i);

# 5. Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado

a = int(input("Digite um numero "));
b = 0;
for i in range(1,a+1):
  b += i;
print(b);

# 6. Faça um programa que leia um número e que calcule o fatorial deste número

a = int(input("Digite um numero "));
b = 1;
for i in range(1,a+1):
  b = b*i;
print(b);

# 7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos.

soma_pesos = 0

for i in range(1, 11):
  peso = float(input(f"Digite o peso da pessoa {i} (em kg): "))
  soma_pesos += peso

media_pesos = soma_pesos / 10

print(f"A média dos pesos das 10 pessoas é: {media_pesos:.2f} kg")

# 10. Faça um programa que leia um número e que imprima na tela se o número é primo ou não.

a = int(input("Digite um numero "));
for i in range(2,a):
  if (a % i == 0):
    print("não é primo")
    break
  print('é primo');