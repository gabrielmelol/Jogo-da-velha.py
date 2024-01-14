import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Configurações da tela
largura_tela = 300
altura_tela = 300
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Velha do Iniciante")

# Tamanho do quadrado do tabuleiro
tamanho_quadrado = 100

# Inicialização do tabuleiro
tabuleiro = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    tela.fill(PRETO)
    for linha in range(1, 3):
        pygame.draw.line(tela, VERDE, (0, linha * tamanho_quadrado), (largura_tela, linha * tamanho_quadrado), 2)
        pygame.draw.line(tela, VERDE, (linha * tamanho_quadrado, 0), (linha * tamanho_quadrado, altura_tela), 2)

# Função para desenhar as jogadas
def desenhar_jogadas():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 'X':
                pygame.draw.line(tela, VERDE, (coluna * tamanho_quadrado + 20, linha * tamanho_quadrado + 20),
                                 ((coluna + 1) * tamanho_quadrado - 20, (linha + 1) * tamanho_quadrado - 20), 2)
                pygame.draw.line(tela, VERDE, ((coluna + 1) * tamanho_quadrado - 20, linha * tamanho_quadrado + 20),
                                 (coluna * tamanho_quadrado + 20, (linha + 1) * tamanho_quadrado - 20), 2)
            elif tabuleiro[linha][coluna] == 'O':
                pygame.draw.circle(tela, VERDE, (coluna * tamanho_quadrado + tamanho_quadrado // 2,
                                                linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 20, 2)

# Função para verificar o vencedor
def verificar_vencedor(jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
           tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para verificar se há empate
def verificar_empate():
    return all(tabuleiro[i][j] != '' for i in range(3) for j in range(3))

# Função para reiniciar o jogo
def reiniciar_jogo():
    global tabuleiro
    tabuleiro = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]

# Função principal do jogo
def jogo_da_velha():
    jogador_atual = 'X'

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                coluna = mouseX // tamanho_quadrado
                linha = mouseY // tamanho_quadrado

                if tabuleiro[linha][coluna] == '':
                    tabuleiro[linha][coluna] = jogador_atual

                    if verificar_vencedor(jogador_atual):
                        print(f"Jogador {jogador_atual} venceu!")
                        pygame.time.delay(2000)
                        reiniciar_jogo()  # Reinicia o jogo
                    elif verificar_empate():
                        print("Deu velha!")
                        pygame.time.delay(2000)
                        reiniciar_jogo()  # Reinicia o jogo
                    else:
                        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        desenhar_tabuleiro()
        desenhar_jogadas()
        pygame.display.flip()
        pygame.display.update()

# Inicia o jogo da velha
jogo_da_velha()
