import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Banner Animado")

# Cores
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Lista de cores (vermelho, verde, azul)
cor_atual = 0  # Índice da cor atual

# Fonte
fonte = pygame.font.Font(None, 36)

# Texto
texto = fonte.render("Joshe", True, cores[cor_atual])

# Posição inicial do texto
pos_x = largura // 2 - texto.get_width() // 2
pos_y = altura // 2 - texto.get_height() // 2

# Velocidade de movimento
velocidade_x = 5

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill((255, 255, 255))
    tela.blit(texto, (pos_x, pos_y))
    pygame.display.flip()

    pos_x += velocidade_x

    # Inverter direção quando atinge a borda direita
    if pos_x + texto.get_width() > largura or pos_x < 0:
        velocidade_x *= -1

    # Mudar de cor a cada X frames
    if pygame.time.get_ticks() % 200 == 0:  # Muda a cor a cada 200 milissegundos
        cor_atual = (cor_atual + 1) % len(cores)
        texto = fonte.render("JosheBrK21", True, cores[cor_atual])

    pygame.time.delay(30)

