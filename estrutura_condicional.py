# 1. Faça um programa que receba dois números e mostre o maior e o menor. Emita uma mensagem, caso os dois sejam iguais.
a= int(input("1° Numero - "));
b= int(input("2° Numero - "));

if(a > b):
  print(str(a) + " é o maior valor");
elif(b > a):
  print(str(b) + " é o maior valor");
else:
  print("são iguai");

# 2. Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
# >= 7 -> Aprovado
# < 7 -> Reprovado

a= float(input("1° Nota - "));
b= float(input("2° Nota - "));

media = (a+b)/2;

if(media >= 7):
  print(f"aprovado com {media}")
else:
  print(f"reprovado com {media}")

# 3. Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
a= float(input("1° Nota - "));
b= float(input("2° Nota - "));
c= float(input("3° Nota - "));

media = (a+b+c)/3;

if(media >= 7):
  print(f"aprovado com {media}")
elif(media >= 3):
  print(f"Exame com {media}")
else:
  print(f"Reprovado {media}")

# 4. Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.

a= float(input("1° valor - "));
b= float(input("2° valor - "));
c= float(input("3° valor - "));

if(a<b+c and b<a+c and c<b+a):
  print("é um triangulo")
else:
  print("Não é um triangulo")

# 5. Faça um programa que leia o sexo e a altura (H - em metros) de uma pessoa, calcule e apresente seu peso ideal utilizando as seguintes fórmulas: 
# Peso ideal (homens) = (72,7 * H) – 58. 
# Peso ideal (mulheres) = (62,1 * H) – 44,7
# Sugestão: para identificar o sexo da pessoa, solicite ao usuário que informe 1 para homens, e 2 para mulheres

altura= float(input("Digite a sua altura: "));

sexo = input("Você é home ou mulher (h/m)")
if(sexo == "h"):
  print(f"Seu pesso ideal é: {(72.7*altura)-58}");
elif(sexo == 'm'):
  print(f"Seu pesso ideal é: {(62.1*altura)-44.7}");
else:
    print("opção invalida");

# 6. Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado d

pesso= float(input("Digite o seu pesso em - KG "));
altura= float(input("Digite a seua altura em - M "));

imc = pesso/(altura*altura);

if(imc > 40):
  print(f"Obesso mórbido - {imc}");
elif(imc > 30):
  print(f"Obesso - {imc}");
elif(imc > 25):
  print(f"sobrepesso - {imc}");
elif(imc > 20):
  print(f"Normal - {imc}");
else:
  print(f"Abaixo do pesso - {imc}");

# 7. Uma empresa decide dar aumento de 30% aos funcionários com salários inferiores a R$1000,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustad

salario= float(input("Digite o salário "));

if(salario < 1000): 
  print(f"O novo sálario é de {salario * 1.3}")
else:
  print("Você não tem direito");

#  8. Faça um programa que receba a idade de um nadador e mostre a sua categoria

idade = int(input("Digite a sua idade "));

if(idade < 7):
  print('INFANTIL');
elif(idade < 10):
  print("JUVENIL");
elif(idade < 15):
  print("ADOLESCENTE");
elif(idade > 30):
  print("ADULTO");
else:
  print("SENIOR");

# 9. Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
# - não eleitor (abaixo de 16 anos); 
# - eleitor obrigatório (entre a faixa de 18 e menor de 65 anos); 
# - eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)

idade = int(input("Digite a sua idade "));

if(idade < 16):
  print('não eleitor');
elif(idade < 18):
  print("facutativo");
elif(idade < 65):
  print("obrigatorio");
else:
  print("facutativo");

# 10. Faça um programa que leia um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número.

a = int(input("Digite um número de 1 à 7 "));

if(a == 2):
  print('segunda');
elif(a == 3):
  print("terça");
elif(a == 4):
  print("quarta");
elif(a == 5):
  print("quinta");
elif(a == 6):
  print("sexta");
elif(a == 7):
  print("sabado");
elif(a == 1):
  print("domingo");
else:
  print("valor invalido");

# 11. Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

a = int(input("Digite um número de 1 à 12 "));
if(a ==1):
  print("janeiro")
elif(a == 2):
  print('fevereiro');
elif(a == 3):
  print("maço");
elif(a == 4):
  print("abril");
elif(a == 5):
  print("maio");
elif(a == 6):
  print("junho");
elif(a == 7):
  print("julho");
elif(a == 8):
  print("agosto");
elif(a == 9):
  print("setembro");
elif(a == 10):
  print("outubro");
elif(a == 11):
  print("novembro");
elif(a == 12):
  print("desenbro");
else:
  print("valor invalido");

# 12. Faça um programa que solicite ao usuário que informe dois números e que exiba o seguinte menu:
# 1 – Somar
# 2 – Subtrair 
# 3 – Multiplicar
# 4 – Dividir
# 5 – Sair
# Em seguida, leia a opção escolhida e exiba o resultado de acordo com a opção.


a = float(input("Digite um número: "));
b = float(input("Digite outro número: "));

print("1 – Somar | 2 – Subtrair | 3 – Multiplicar |  4 – Dividir | 5 – Sair");
c = int(input("SELECIONE UMA OPÇÃO"));

if(c == 1):
  print(f"soma {a+b}");
elif(c == 2):
  print(f"Subtrair {a-b}");
elif(c == 3):
  print(f"Multiplicar {a*b}");
elif(c == 4):
  print(f"Dividir {a/b}");
elif(c == 5):
  print("Sair");
else:
  print("opção invalida");

import math;
a= int(input("Coeficiente A => "));
b= int(input("Coeficiente B => "));
c= int(input("Coeficiente C => "));

#13. faça um programa que resolva a equações de segundo grau
delta = b**2 - 4*a*c;

if(delta < 0):
  print("Não existe raiz real");
elif(delta == 0):
  print(f"Existe somente uma raiz real { ((-b) / (2*a)):.2f}")
elif(delta > 0):
  print(f"Existem duas raizes reais: { ((-b + math.sqrt(delta)) / (2*a)):.2f},{((-b - math.sqrt(delta)) / (2*a)):.2f}")