#1. Solicite ao usuário que digite uma frase. Imprima:
	# - o tamanho (em caracteres) da frase
	# - a frase toda em maiúscula
	# - a frase toda em minúscula
	# - a frase na vertical(letra por letra)
	# - solicite ao usuário que informe uma posição inicial e final na frase, e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	# - a frase em ordem inversa
	# - solicite ao usuário que informe duas palavras. Substitua, na frase informada, a primeira palavra informada pelo usuário, pela segunda palavra informada. Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.

frase = input("Digite uma frase: ");
print(len(frase));
print(frase.lower());
print(frase.upper());
for c in frase:
  print(c);
inicio = int(input("Digite o inicio"));
final = int(input("Digite o final"));
print(frase[inicio:final]);
print(frase[::-1]);

plavra1 = input("Digite o que vai ser substituido");
palavra2 = input("Digite pelo que vai ser supstituido");

fraseNova = frase.replace(plavra1, palavra2);

#2. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que digite uma palavra. Imprima uma mensagem informando a quantidade de vezes em que a palavra se encontra na frase (considere que a palavra pode estar em maiúscula ou minúscula na frase).

frase = input("Digite uma frase: ");
palavra = input("Digite uma palavra: ");

fraseM = frase.lower()  
palavraM = palavra.lower() 

print (fraseM.count(palavraM))

#3. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que informe um caractere de maneira que a frase seja dividida em partes de acordo com o caractere informado. Imprima na tela a frase dividida.

frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

partes = frase.split(caractere)

for parte in partes:
    print(parte)

# 4. Solicite ao usuário que digite uma palavra. Em seguida, solicite ao mesmo que informe um caractere separador, de maneira que o separador seja incluído na palavra, separando cada letra da palavra digitada. 

palavra = input("Digite uma palavra: ")
caractere = input("Digite um caractere: ")

palavra_separada = caractere.join(palavra)

print(palavra_separada)

# 5. Solicite ao usuário que digite uma palavra e imprima uma mensagem informando se a palavra é ou não um palíndromo (uma palavra que se lê da mesma maneira nos dois sentidos. Por exemplo: OVO, RADAR, OSSO etc.)

palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")