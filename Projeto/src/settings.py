import pygame
import os

# peso do grafo
TERRAIN_WEIGHTS = {
    "grass": 1,
    "sand": 3,
    "water": 5,
    "rock": 7,
}

# cor para pintar quando o vértice é visitado
FALLBACK_COLORS = {
    "grass": (255, 255, 255),
    "sand": (244, 164, 96),
    "rock": (139, 137, 137),
    "water": (30, 144, 255),
    "wall": (0, 0, 0)
}

# cores
WHITE = (255, 255, 255)
WHITE_GRAY = (100, 100, 100) # é um branco não muito branco
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0,255,0)

# ajustes de tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Laby"

# ajustes do mapa (grid)
ROWS = 20
CELL_SIZE = 30

# ajustes da barra de tarelas
ICON_SIZE = 50
SPACING = 10
MARGIN = 10
TOOL_PANEL_WIDTH = 80
ICON_SIZE = 50
SPACING = 10
MARGIN = 10

#texto de instrução para o início do jogo.
instructions_text = [
    "Bem-vindo ao Laby!",
    "",
    "O seu desafio é construir um labirinto com obstáculos e encontrar o melhor caminho até a saída!",
    "",
    "Use o menu lateral para selecionar os elementos e o mouse para desenhar na grade:",
    "- Parede: Crie limites para o labirinto.",
    "- Borracha: Apague elementos da grade.",
    "",
    "Para marcar os pontos de partida e chegada, use as bandeiras. ",
    "Lembre-se: esses elementos são obrigatórios para sabermos o resultado. ",
    "",
    "Adicione desafios que alteram o percurso:",
    "- Água: Um trecho que exige natação.",
    "- Areia: Terreno onde a areia pode entrar nos olhos e dificultar a passagem.",
    "- Rochas: Pedras que machucam os pés.",
    "",
    "Para traçar o caminho mais curto, aperte a barra de espaço.",
    "Para limpar o caminho encontrado, aperte a tecla C."
]
