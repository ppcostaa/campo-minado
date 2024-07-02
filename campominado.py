import random

def definicaoDeDificuldade():
    print("******* Campo Minado *******")
    print("Bem-vindo! Escolha a dificuldade:")
    print("(1)Fácil (2)Médio (3)Difícil")
    dificuldade = int(input())
    if dificuldade == 1:
        print("No seguro, hein? Boa sorte! (^◡^ )")
        return 5, 5, random.randint(7, 14)
    elif dificuldade == 2:
        print("Hehe, boa sorte! (^◡^ )")
        return 7, 7, random.randint(20, 30)
    elif dificuldade == 3:
        print("Uau, que pessoa corajosa! Boa sorte (^◡^ )")
        return 10, 10, random.randint(30, 60)
    else:
        print("Opção inválida. Escolha novamente. (^◡^ )")
        return definicaoDeDificuldade()

def criarMatriz(linhas, colunas):
    return [['.' for _ in range(colunas)] for _ in range(linhas)]

def criarTabuleiroVisivel(colunas, linhas):
    campo = criarMatriz(linhas, colunas)
    for linha in campo:
        print(' '.join(linha))
    return campo

def jogo():
    colunas, linhas, minas = definicaoDeDificuldade()
    tabuleiroVisivel = criarTabuleiroVisivel(colunas, linhas)
    tabuleiroReal = criarMatriz(colunas, linhas)
    infoMinas(tabuleiroReal, colunas, linhas, minas)
    jogando(tabuleiroVisivel, tabuleiroReal, colunas, linhas)

def infoMinas(tabuleiroReal, colunas, linhas, minas):
    localMinas = random.sample(range(colunas * linhas), minas)
    for local in localMinas:
        x = local // colunas
        y = local % colunas
        tabuleiroReal[x][y] = '*'

def obterCoordenadas():
    coordenadas = input("Digite as coordenadas (x, y): ").strip()
    if ',' not in coordenadas:
        print("Formato de coordenadas inválido. Use 'x, y'. Tente novamente! (^◡^ )")
        return obterCoordenadas()

    x, y = coordenadas.split(',')
    try:
        x = int(x.strip()) - 1
        y = int(y.strip()) - 1
        return x, y
    except ValueError:
        print("Coordenadas inválidas. Certifique-se de inserir números inteiros. Tente novamente! (^◡^ )")
        return obterCoordenadas()

def obterAcao():
    print("O que você gostaria de fazer?")
    print("(M) Marcar mina (T) Tirar marcação (R) Revelar espaço")
    decisao = input().strip().upper()

    if decisao.startswith(('M', 'T', 'R')) and len(decisao) >= 1:
        return decisao[0]
    else:
        print("Desculpa, ação inválida. Tente novamente! (╥﹏╥)")
        return obterAcao()

def marcacoes():
    acao = obterAcao()
    coordenadas = obterCoordenadas()
    return acao, coordenadas

def mostrarTabuleiro(tabuleiroVisivel):
    for linha in tabuleiroVisivel:
        print(' '.join(linha))

def contarMinas(tabuleiroReal, linha, coluna):
    linhas = len(tabuleiroReal)
    colunas = len(tabuleiroReal[0])
    minasAoRedor = 0
    for x in range(max(0, linha - 1), min(linhas, linha + 2)):
        for y in range(max(0, coluna - 1), min(colunas, coluna + 2)):
            if (x, y) != (linha, coluna) and tabuleiroReal[x][y] == '*':
                minasAoRedor += 1
    return minasAoRedor

def atualizarTabuleiro(tabuleiroReal, tabuleiroVisivel, linha, coluna):
    if tabuleiroReal[linha][coluna] == '*':
        print("Você explodiu! (╥﹏╥)")
        return False
    else:
        minasAoRedor = contarMinas(tabuleiroReal, linha, coluna)
        tabuleiroVisivel[linha][coluna] = str(minasAoRedor)
        return True

def verificarVitoria(tabuleiroReal, tabuleiroVisivel):
    linhas = len(tabuleiroReal)
    colunas = len(tabuleiroReal[0])
    for x in range(linhas):
        for y in range(colunas):
            if tabuleiroReal[x][y] != '*' and tabuleiroReal[x][y] != tabuleiroVisivel[x][y]:
                return False
    return True

def jogando(tabuleiroVisivel, tabuleiroReal, colunas, linhas):
    mostrarTabuleiro(tabuleiroVisivel)
    while True:
        acao, (x, y) = marcacoes()

        if x < 0 or y < 0 or x >= linhas or y >= colunas:
            print("Desculpa, mas a coordenada escolhida foi inválida. Tente novamente! (^◡^ )")
            continue

        if acao == 'M':
            if tabuleiroVisivel[x][y] == '.':
                tabuleiroVisivel[x][y] = 'M'
            else:
                print("Esta posição já está marcada! (>‿◠)✌")
                continue
        elif acao == 'T':
            if tabuleiroVisivel[x][y] == 'M':
                tabuleiroVisivel[x][y] = '.'
            else:
                print("Esta posição não está marcada! (>‿◠)✌")
                continue
        elif acao == 'R':
            if not atualizarTabuleiro(tabuleiroReal, tabuleiroVisivel, x, y):
                print("Sinto muito, você perdeu (╥﹏╥)")
                break
        else:
            print("Sinto muito, ação inválida. (╥﹏╥)")
            continue
        mostrarTabuleiro(tabuleiroVisivel)
        if verificarVitoria(tabuleiroReal, tabuleiroVisivel):
            print('Parabéns! Você venceu ᕙ(`▿´)ᕗ')
            break
    
jogo()