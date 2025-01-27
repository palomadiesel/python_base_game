import pgzrun
import random
from pygame import Rect
from pgzero.builtins import sounds, clock, keyboard, keys
from Player import Player
from Enemy import Enemy
from Platform import Platform
from Collectable import Collectable

# Configurações do fundo e da tela
WIDTH = 1000  # Largura da tela
HEIGHT = 600  # Altura da tela
GROUND_COLOR = (156, 115, 174)  # Cor do chão
game_over = False  # Variável para verificar se o jogo acabou
menu_active = True  # Indica se o menu principal está ativo
sound_on = True  # Controle de som do jogo

# Personagens
alien = Player('alien_idle', (500, 250))  # Jogador (alien)
thief = Enemy('thief', (random.randint(20, 780), 0), 4)  # Inimigo: ladrão
bomb = Enemy('bomb', (random.randint(20, 780), 0), 4)  # Inimigo: bomba

# Colecionáveis
coin_x = [950, 50, 850, 150, 750, 250, 650, 350, 500]  # Posições X das moedas
coin_y = [70, 70, 170, 170, 270, 270, 370, 370, 470]  # Posições Y das moedas
coin = Collectable('coin', coin_x, coin_y)  # Objeto coin que é colecionável

# Plataformas (representadas por retângulos)
floor = Rect((0, 580), (1000, 20))  # Chão
platform1 = Rect((450, 500), (100, 10))  # Plataforma 1
platform2 = Rect((300, 400), (100, 10))  # Plataforma 2
platform3 = Rect((600, 400), (100, 10))  # Plataforma 3
platform4 = Rect((400, 300), (100, 10))  # Plataforma 4
platform5 = Rect((700, 300), (100, 10))  # Plataforma 5
platform6 = Rect((100, 200), (100, 10))  # Plataforma 6
platform61 = Platform(200, 200)  # Plataforma móvel 1
platform62 = Platform(500, 200)  # Plataforma móvel 2
platform7 = Rect((800, 200), (100, 10))  # Plataforma 7
platform8 = Rect((0, 100), (100, 10))  # Plataforma 8
platform9 = Rect((900, 100), (100, 10))  # Plataforma 9

# Lista de todas as plataformas
platforms = [
    floor, platform1, platform2, platform3, platform4, platform5,
    platform6, platform7, platform8, platform9, platform61, platform62
]

# Toca a música de fundo se o som estiver ativado
if sound_on:
    sounds.space_level.play(-1)

# Funções de desenho

def draw():
    if menu_active:
        draw_menu()  # Exibe o menu inicial
    elif bomb.is_game_over:
        draw_game_over()  # Exibe a tela de game over
    else:
        draw_game()  # Exibe o jogo em andamento

def draw_menu():
    # Desenha o menu inicial com opções de controle
    screen.fill((0, 0, 0))
    screen.draw.text("SPACE QUEST", center=(WIDTH // 2, 100), fontsize=50, color="white")
    screen.draw.text("Tecla 1. Iniciar Jogo", center=(WIDTH // 2, 200), fontsize=40, color="white")
    screen.draw.text("Tecla 2. Ativar/Desativar Som", center=(WIDTH // 2, 300), fontsize=40, color="white")
    screen.draw.text("Tecla 3. Sair", center=(WIDTH // 2, 400), fontsize=40, color="white")
    screen.draw.text(
        "Pegue o máximo de moedas que puder.",
        center=(WIDTH // 2, 500),
        fontsize=30,
        color="yellow",
        shadow=(1, 1)
    )
    screen.draw.text(
        "Evite as bombas e os aliens amarelos, os aliens vão roubar suas moedas!",
        center=(WIDTH // 2, 540),
        fontsize=30,
        color="yellow",
        shadow=(1, 1)
    )

def draw_game_over():
    # Exibe a tela de game over com a pontuação final
    screen.fill((50, 50, 50))
    screen.draw.text('GAME OVER', center=(WIDTH // 2, 200), color=(255, 255, 255), fontsize=50)
    screen.draw.text(f'FINAL LOOT: {alien.points}', center=(WIDTH // 2, 300), color=(255, 255, 255), fontsize=30)
    screen.draw.text("Tecla 1. Iniciar Novo Jogo", center=(WIDTH // 2, 400), fontsize=30, color="white")
    screen.draw.text("Tecla 2. Sair", center=(WIDTH // 2, 450), fontsize=30, color="white")
    sounds.space_level.stop()

def draw_game():
    # Desenha o fundo, as plataformas, os personagens e os itens
    screen.blit('space_background', (0, 0))
    screen.blit('space_station', (0, 0))

    screen.draw.text(
        f"Loot: {alien.points}",
        (15, 10),
        fontname="publicpixel",
        fontsize=20,
        shadow=(1, 1),
        color=(255, 255, 255),
        scolor="#202020"
    )
    screen.draw.text(
        f"Lives: {alien.lives}",
        (800, 10),
        fontname="publicpixel",
        fontsize=20,
        shadow=(1, 1),
        color=(255, 255, 255),
        scolor="#202020"
    )

    platforms[10] = platform61.actor
    platforms[11] = platform62.actor

    for platform in platforms:
        screen.draw.filled_rect(platform, GROUND_COLOR)

    # Desenha os personagens e itens no jogo
    alien.actor.draw()
    thief.actor.draw()
    bomb.actor.draw()
    coin.actor.draw()

# Atualização do jogo
def update():
    global menu_active, sound_on

    if menu_active or bomb.is_game_over:
        return  # Não atualiza o jogo se estiver no menu ou game over

    platform61.move(player=alien)  # Move a plataforma móvel 1
    platform62.move(player=alien)  # Move a plataforma móvel 2

    alien.move(
        keyboard=keyboard,
        platforms=platforms,
        sounds=sounds,
        clock=clock,
        coin=coin
    )  # Atualiza o movimento do jogador

    thief.move(player=alien, sounds=sounds)  # Move o ladrão
    bomb.move(player=alien, sounds=sounds)  # Move a bomba

# Entradas do teclado
def on_key_down(key):
    global menu_active, sound_on

    if menu_active:
        if key == keys.K_1:
            menu_active = False  # Inicia o jogo
        elif key == keys.K_2:
            sound_on = not sound_on  # Alterna o som
            if sound_on:
                sounds.space_level.play(-1)
            else:
                sounds.space_level.stop()
        elif key == keys.K_3:
            quit()  # Encerra o jogo
    elif bomb.is_game_over:
        if key == keys.K_1:
            reset_game()  # Reseta o jogo após game over
        elif key == keys.K_2:
            quit()  # Encerra o jogo após game over

def reset_game():
    # Reseta o jogo para o estado inicial
    global menu_active, game_over
    menu_active = True
    game_over = False
    alien.reset()
    bomb.reset()
    thief.reset()

    if sound_on:
        sounds.space_level.stop()
        sounds.space_level.play(-1)  # Reproduz a música de fundo novamente

# Inicia o loop do jogo
pgzrun.go()