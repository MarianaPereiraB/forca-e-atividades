palavra = "espaço"
letras_usuario = [] #letras_usuario é uma lista que guarda todas as letras que o jogador já tentou.
chances = 5
ganhou = False

while True:
    print("\n" + "-" * 20 + "\n") #pesquisei no google para pode fazer, significa criar uma string com 20 "-" e quebra de linha no começo e no final
#letra.lower() significa o valor va variárel "letra" para minúscula
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nVocê tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ").lower()
#.isalpha() verifica se a string colocada é letra do alfabeto(anula numero, espaço e símbolos)
    if not tentativa.isalpha() or len(tentativa) != 1:
        print("Digite apenas uma letra válida!")
        continue
#descobri também que "continue" é usada dentro dos laços de repetição para pular o restante do código daquela iteração
# e ir para a próxima repetição. ex: quando i == 2, o continue faz o loop ignorar o print(i) e seguir para o próximo número
    if tentativa in letras_usuario:
        print("Você já tentou essa letra.")
        continue

    letras_usuario.append(tentativa)
    #.append() é um método de lista do Python que insere um novo item no final da lista
    #Adiciona a letra digitada pelo jogador (armazenada na variável tentativa) à lista letras_usuario

    if tentativa not in palavra.lower():
        chances -= 1

    ganhou = all(letra in letras_usuario for letra in palavra.lower())

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"\nParabéns, você ganhou. A palavra era: {palavra}")
else:
    print(f"\nVocê perdeu! A palavra era: {palavra}")