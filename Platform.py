from pygame import Rect

# Classe que representa uma plataforma móvel no jogo
class Platform:
    def __init__(self, position, movement_range):
        # Cria a plataforma com a posição inicial e um tamanho fixo
        self.actor = Rect((position, 200), (100, 10))
        
        # Define o intervalo de movimento da plataforma (mínimo e máximo)
        self.x_min = position
        self.x_max = position + movement_range
        
        # Controla a direção do movimento da plataforma (inicia movendo para a esquerda)
        self.direction_left = True

    def move(self, player):
        # Move a plataforma para a direita ou para a esquerda dependendo da direção
        if self.direction_left:
            self.actor.x += 2

            # Se a plataforma atingiu o limite direito, muda a direção
            if self.actor.x == self.x_max:
                self.direction_left = False

            # Se a plataforma colide com o jogador, move o jogador junto
            if player.actor.colliderect(self.actor):
                player.actor.x += 2
        else:
            self.actor.x -= 2

            # Se a plataforma atingiu o limite esquerdo, muda a direção
            if self.actor.x == self.x_min:
                self.direction_left = True

            # Se a plataforma colide com o jogador, move o jogador junto
            if player.actor.colliderect(self.actor):
                player.actor.x -= 2