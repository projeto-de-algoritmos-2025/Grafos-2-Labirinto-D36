# Labirinto

**Número da Lista**: 36  
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  

## 👩‍💻 Alunos

<div align="center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/danielle-soaress"><img style="border-radius: 50%;" src="https://github.com/danielle-soaress.png" width="190;" alt=""/><br /><sub><b>Danielle Soares</b></sub></a></td>
    <td align="center"><a href="https://github.com/Leticia-Arisa-K-Higa"><img style="border-radius: 50%;" src="https://github.com/Leticia-Arisa-K-Higa.png" width="190px;" alt=""/><br /><sub><b>Leticia Arisa</b></sub></a></td>
  </tr>
</table>

| Matrícula   | Aluno                          |
| ----------- | ------------------------------ |
| 23/1012058  | Danielle Soares da Silva       |
| 23/1012272  | Leticia Arisa Kobayashi Higa   |
</div>

## 🎬 Apresentação do Projeto

<div align="center">

<a href="https://youtu.be/dY56_IJ9qys"><img src="https://i.imgur.com/kzR0glG.png" width="50%"></a>
</div>

Autores: [Danielle Soares](https://github.com/danielle-soaress) e [Leticia Arisa](https://github.com/Leticia-Arisa-K-Higa).

## 🎯 Objetivo

Desenvolver uma aplicação interativa que permita ao usuário **desenhar ou carregar mapas de labirinto** que contenha obstáculos e resolvê-los utilizando o algoritmo de Dijkstra.

O sistema deve:
- Encontrar o **caminho mais curto** entre dois pontos com **Dijkstra**.  
- Permitir obstáculos ou terrenos que influenciem o trajeto, como paredes, água e rochas.

## 🔧 Tecnologias e Estruturas Utilizadas

- **Linguagem:** Python 3  
- **Bibliotecas:**  
  - `pygame` → interface gráfica, animações e interação com o usuário  
  - `os` → manipulação de caminhos de arquivos de forma segura e cross-plataforma
- **Estruturas de dados:**  
  - Matrizes (para representar a grade do labirinto)
  - Dicionários (para representar os nós e seus atributos, como o tipo de terreno e o sprite)
  - Fila de prioridade (para o algoritmo de Dijkstra)

## 🧩 Modelagem do Grafo

- Cada **célula do labirinto** é um **nó do grafo**.  
- Cada **movimento possível** (cima, baixo, esquerda, direita) é uma **aresta**.  
- O **peso da aresta** pode ser:
  - `1` → movimento simples
  - `3` → movimento sob um terreno de areia
  - `5` → movimento sob um trecho de natação
  - `7` → movimento sob um trecho rochoso
- O nó de **início** e o nó de **destino** são os pontos usados pelo algoritmo de Dijkstra.  

---

## 🧠 Como funciona

1. **Desenho do labirinto**  
   - O usuário desenha o labirinto e adiciona obstáculos diretamente na grade usando as ferramentas do menu lateral.
   - O ponto de início e de chegada são definidos pelo usuário com as bandeiras.

2. **Execução do algoritmo**  
   - Quando o usuário aperta a **barra de espaço**, o algoritmo de Dijkstra é executado para encontrar o caminho de menor custo.
   - O caminho encontrado e os nós visitados são visualizados com uma animação.

3. **Visualização**  
   - A grade, os obstáculos e o caminho são exibidos no Pygame.
   - O usuário pode limpar o caminho a qualquer momento apertando a **tecla C**.

---

## 🚀 Como executar

1. **Clonar o repositório**

```bash
git clone https://github.com/projeto-de-algoritmos-2025/Grafos-2-Labirinto-D3
```

3. Entre na pasta do projeto

```bash
cd Projeto/src
```

4. Instalar dependências

```bash
pip install pygame
```

5. Executar o programa

```bash
python main.py
```

##  💡 Observações

Sistema desenvolvido para o curso de Engenharia de Software da UnB-FCTE.