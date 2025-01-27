# Space Quest

**Space Quest** é um jogo de plataforma 2D onde o jogador assume o papel de um alienígena tentando coletar o máximo de moedas possível enquanto evita bombas e inimigos. O jogo é feito com **Pygame Zero** e oferece um menu interativo, mecânicas de salto, movimento e colisões com plataformas.

## Funcionalidades

- **Personagem Jogável (Alien)**: Controle do personagem que pode se mover e pular pelas plataformas.
- **Inimigos**: Ladrões que roubam moedas e bombas que causam dano.
- **Colecionáveis**: Moedas que o jogador deve pegar para ganhar pontos.
- **Plataformas**: Estáticas e móveis que o jogador pode usar para navegar pelo cenário.
- **Som e Música**: Música de fundo e efeitos sonoros para ações como pular e pegar moedas.
- **Menu Inicial**: Opções para iniciar o jogo, alternar o som ou sair.
- **Tela de Game Over**: Exibe a pontuação final e opções para reiniciar ou sair.

## Como Jogar

1. **Iniciar Jogo**: Pressione a tecla `1` no menu.
2. **Som**: Pressione a tecla `2` para ativar/desativar o som.
3. **Sair**: Pressione a tecla `3` para sair.
4. **Movimentos**:
   - **Esquerda**: Tecla `←`
   - **Direita**: Tecla `→`
   - **Pular**: Tecla `↑`
5. **Objetivo**: Pegue o máximo de moedas que puder, evite bombas e ladrões!

## Requisitos

- Python 3.x
- Pygame Zero

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/space-quest.git
   ```

2. Instale as dependências:
    ```bash
   pip install pgzero
   pip install pygame
   ```

3. Execute o jogo:
    ```bash
   pgzrun space_quest.py
   ```
