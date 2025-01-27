import random
from pgzero.builtins import Actor

# Classe que representa um objeto colecionável no jogo
class Collectable:
    def __init__(self, image, collectable_x_positions, collectable_y_positions):
        # Inicializa a posição do colecionável com base nas listas de posições fornecidas
        self.collectable_x_positions = collectable_x_positions
        self.collectable_y_positions = collectable_y_positions
        
        # Escolhe uma posição aleatória para o colecionável
        self.collectable_index = random.randint(0, len(collectable_x_positions) - 1)

        # Cria o ator do colecionável (imagem e posição)
        self.actor = Actor(
            image,
            (
                collectable_x_positions[self.collectable_index],
                collectable_y_positions[self.collectable_index]
            )
        )

    def reset_position(self):
        # Armazena o índice da posição atual
        old_coin_index = self.collectable_index
        positions_num = len(self.collectable_x_positions)

        # Garante que o novo índice de posição seja diferente do antigo
        while old_coin_index == self.collectable_index:
            self.collectable_index = random.randint(0, positions_num - 1)

        # Atualiza a posição do ator para a nova posição aleatória
        self.actor.x = self.collectable_x_positions[self.collectable_index]
        self.actor.y = self.collectable_y_positions[self.collectable_index]