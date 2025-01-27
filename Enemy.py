import random
from pgzero.builtins import Actor

# Classe que representa um inimigo no jogo
class Enemy:
    def __init__(self, image, position, speed):
        # Inicializa o ator do inimigo com a imagem e posição fornecidas
        self.actor = Actor(image, position)
        self.speed = speed  # Velocidade do inimigo
        self.is_game_over = False  # Flag de fim de jogo
        self.initial_position = position  # Posição inicial do inimigo

    def move(self, player, sounds):
        # Move o inimigo para baixo de acordo com sua velocidade
        self.actor.y += self.speed
        
        # Se o inimigo sai da tela, reposiciona ele no topo
        if self.actor.y > 560:
            self.reset_position()

        # Verifica colisão com o jogador
        if self.actor.colliderect(player.actor):
            if self.actor.image == 'thief':  # Se o inimigo for um ladrão
                sounds.hurt.play()  # Toca o som de dano
                if player.points > 0:
                    player.lose_point()  # O jogador perde um ponto
                self.reset_position()  # Reseta a posição do inimigo
            elif self.actor.image == 'bomb':  # Se o inimigo for uma bomba
                sounds.boom.play()  # Toca o som de explosão
                self.reset_position()  # Reseta a posição da bomba

                if player.lives > 0:
                    player.lives -= 1  # O jogador perde uma vida

                # Se o jogador ficar sem vidas, o jogo termina
                if player.lives == 0:
                    self.is_game_over = True
                    sounds.game_over.play()  # Toca o som de fim de jogo

    def reset_position(self):
        # Reseta a posição do inimigo para um novo local aleatório
        self.actor.x = random.randint(20, 780)
        self.actor.y = 0

    def reset(self):
        """Restaura o inimigo ao estado inicial."""
        self.actor.pos = self.initial_position  # Restaura a posição inicial
        self.is_game_over = False  # Reseta o estado de fim de jogo