import time
from pgzero.builtins import Actor
from Platform import Platform

# Classe que representa o jogador no jogo
class Player:
    def __init__(self, image, position):
        # Inicializa o ator do jogador com a imagem e posição fornecidas
        self.actor = Actor(image, position)
        # Define variáveis para controle de movimento e física
        self.x_velocity = 0  # Velocidade horizontal
        self.y_velocity = 0  # Velocidade vertical
        self.gravity = 1  # Gravidade aplicada ao jogador
        self.jumping = False  # Indica se o jogador está pulando
        self.jumped = False  # Impede que o jogador pule repetidamente
        self.allow_x = True  # Permite ou não o movimento horizontal
        self.timer = []  # Lista para controlar o tempo do pulo e queda
        self.points = 0  # Pontuação do jogador
        self.lives = 3  # Vidas do jogador
        self.initial_position = position  # Posição inicial para o reset

    def collide_check(self, platforms):
        # Verifica se o jogador colidiu com alguma plataforma
        for plat in platforms:
            if isinstance(plat, Platform):
                return True
            if self.actor.colliderect(plat):
                return True
        return False

    def lose_life(self):
        # Decrementa uma vida do jogador
        self.lives -= 1

    def lose_point(self):
        # Decrementa um ponto do jogador
        self.points -= 1

    def reset_jump(self):
        # Reseta o estado de pulo do jogador
        self.jumped = False

    def add_point(self):
        # Incrementa um ponto para o jogador
        self.points += 1

    def move(self, keyboard, platforms, sounds, clock, coin):
        # Controle de animação e movimento do jogador
        if self.x_velocity == 0 and not self.jumped:
            self.actor.image = 'alien_idle'  # Jogador parado

        # Se o jogador colidiu com uma plataforma, ajusta a gravidade e posição
        if self.collide_check(platforms):
            self.gravity = 1
            self.actor.y -= 1
            self.allow_x = True
            self.timer = []
        else:
            self.actor.y += self.gravity  # Aplica gravidade

            if self.gravity <= 20:
                self.gravity += 0.5  # Aumenta a gravidade com o tempo

            self.timer.append(time.perf_counter())  # Registra o tempo do salto/queda

            # Ajusta o movimento no eixo X se o jogador não estiver pulando
            if len(self.timer) > 5 and not self.jumped:
                self.allow_x = False
                self.actor.image = 'alien_jump'

                if len(self.timer) > 20:
                    self.actor.image = 'alien_fall1'

                    if len(self.timer) > 30:
                        self.actor.image = 'alien_fall2'

        # Movimento para a esquerda
        if keyboard.left and self.allow_x:
            if self.actor.x > 40 and self.x_velocity > -8:
                self.x_velocity -= 2
                self.actor.image = 'alien_left'

            if self.jumped:
                self.actor.image = 'alien_upper_left'

        # Movimento para a direita
        if keyboard.right and self.allow_x:
            if self.actor.x < 960 and self.x_velocity < 8:
                self.x_velocity += 2
                self.actor.image = 'alien_right'

            if self.jumped:
                self.actor.image = 'alien_upper_right'

        # Aplica o movimento gradual do jogador no eixo X
        self.actor.x += self.x_velocity

        # Reduz a velocidade de movimento horizontal gradualmente
        if self.x_velocity > 0:
            self.x_velocity -= 1

        if self.x_velocity < 0:
            self.x_velocity += 1

        # Impede que o jogador ultrapasse as bordas da tela
        if self.actor.x < 50 or self.actor.x > 950:
            self.x_velocity = 0

        # Pulo do jogador: verificação de teclas e colisão com plataformas
        if keyboard.up and self.collide_check(platforms) and not self.jumped:
            sounds.jump.play()  # Toca som de pulo
            self.jumping = True
            self.jumped = True
            clock.schedule_unique(self.reset_jump, 0.4)
            self.actor.image = 'alien_jump'
            self.y_velocity = 95  # Altura do pulo

        # Controle da física do pulo (queda gradual)
        if self.jumping and self.y_velocity > 25:
            self.y_velocity -= ((100 - self.y_velocity) / 2)
            self.actor.y -= self.y_velocity / 3  # Ajusta a altura do pulo
        else:
            self.y_velocity = 0
            self.jumping = False  # Fim do pulo

        # Se o jogador pegar uma moeda, adiciona um ponto
        if self.actor.colliderect(coin.actor):
            self.add_point()
            sounds.coin.play()  # Toca som de coleta de moeda
            coin.reset_position()  # Reseta a posição da moeda

    def reset(self):
        """Restaura o jogador ao estado inicial."""
        self.actor.pos = self.initial_position  # Reseta a posição inicial
        self.x_velocity = 0  # Reseta a velocidade horizontal
        self.y_velocity = 0  # Reseta a velocidade vertical
        self.gravity = 1  # Reseta a gravidade
        self.jumping = False  # Reseta o estado de pulo
        self.jumped = False  # Impede pulo repetido
        self.allow_x = True  # Permite movimento horizontal
        self.timer = []  # Limpa o temporizador
        self.points = 0  # Reseta a pontuação
        self.lives = 3  # Reseta as vidas