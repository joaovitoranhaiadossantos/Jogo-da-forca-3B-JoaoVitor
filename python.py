import random

#MISSÃO DOS ALUNOS CONCLUÍDA: 
#Adicionar mais palavras
#Palavras separadas por temas usando Dicionário
palavras_por_tema = {
    "tecnologia": ["python", "programacao", "sistema", "algoritmo", "teclado", "internet", "computador", "hardware", "software", "monitor"],
    "escola": ["professor", "aluno", "caderno", "caneta", "biblioteca", "aula", "prova"],
    "jogos": ["controle", "console", "aventura", "plataforma", "estrategia", "ranking"],
    "filmes": ["cinema", "diretor", "roteiro", "comedia", "drama", "animacao"]
}

def escolher_palavra():
    """Escolhe um tema e uma palavra aleatória dentro desse tema."""
    # Sorteia um tema do dicionário
    tema = random.choice(list(palavras_por_tema.keys()))
    # Sorteia uma palavra dentro do tema escolhido
    palavra = random.choice(palavras_por_tema[tema])
    return palavra, tema

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com as letras já acertadas."""
    resultado = ""
    for letra in palavra:
        if letra in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar():
    # Agora a função retorna a palavra E o tema sorteado
    palavra_secreta, tema_da_rodada = escolher_palavra()
    letras_acertadas = []
    letras_tentadas = []
    vidas = 6
    pontos = 0

    print("=" * 40)
    print("JOGO DA FORCA - PYTHON")
    print("=" * 40)
    print(f"DICA: O tema da palavra é -> {tema_da_rodada.upper()}")
    print("Você tem", vidas, "vidas.")
    print()

    while vidas > 0:
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras já tentadas:", letras_tentadas)
        print("Vidas:", vidas)
        print("Pontos:", pontos)
        print("-" * 40)

        letra = input("Digite uma letra: ").lower()

        # Validação da entrada
        if len(letra) != 1:
            print("Digite apenas UMA letra.")
            print()
            continue

        if not letra.isalpha():
            print("Digite apenas letras.")
            print()
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            print()
            continue

        letras_tentadas.append(letra)

        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra.")
            letras_acertadas.append(letra)
            pontos += 10
        else:
            print("Ops! Essa letra não está na palavra.")
            vidas -= 1
            pontos -= 2

        print()

        # Verifica se o jogador venceu
        venceu = True
        for letra_da_palavra in palavra_secreta:
            if letra_da_palavra not in letras_acertadas:
                venceu = False

        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break

    if vidas == 0:
        print("=" * 40)
        print("FIM DE JOGO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

# Início do programa
jogar()