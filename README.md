# Labirinto

**Número da Lista**: 36
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  

---

## 👩‍💻 Alunos

<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/danielle-soaress"><img style="border-radius: 50%;" src="https://github.com/danielle-soaress.png" width="190;" alt=""/><br /><sub><b>Danielle Soares</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/Leticia-Arisa-K-Higa"><img style="border-radius: 50%;" src="https://github.com/Leticia-Arisa-K-Higa.png" width="190px;" alt=""/><br /><sub><b>Leticia Arisa</b></sub></a><br />
  </tr>
</table>

| Matrícula   | Aluno                          |
| ----------- | ------------------------------ |
| 23/1012058  | Danielle Soares da Silva       |
| 23/1012272  | Leticia Arisa Kobayashi Higa   |
</div>

---

## 🎬 Apresentação do Projeto

<div align="center">
<a href="https://youtu.be/UFUj0rDUyyU"><img src="https://i.imgur.com/2LNlNYO.png" width="50%"></a>
</div>

<font size="3"><p style="text-align: center">Autor: [Danielle Soares](https://github.com/danielle-soaress) e [Leticia Arisa](https://github.com/Leticia-Arisa-K-Higa).</p></font>

---

## 🎯 Objetivo

Desenvolver uma aplicação interativa que permita ao usuário **desenhar ou carregar mapas de labirinto** e resolvê-los utilizando algoritmos clássicos de grafos. O sistema deve encontrar o **caminho mais curto** entre dois pontos através do **Dijkstra** e, opcionalmente, **gerar ou otimizar mapas** usando algoritmos de **árvore geradora mínima (Prim e Kruskal)**.

---

## 🔧 Tecnologias e Estruturas Utilizadas

* **Linguagem C** (implementação dos algoritmos de grafos).
* **Estruturas de dados:**

  * Matrizes (representação do labirinto).
  * Listas de adjacência ou vetores dinâmicos (representação do grafo).
  * Fila de prioridade (para Dijkstra).
  * Estruturas de conjuntos disjuntos (Union-Find) para Kruskal.
* **Interface: **
  * `ncurses` → para visualização em terminal com cores.
  * `SDL2` → para visualização gráfica com janelas e animação.

---

## 🧩 Modelagem do Grafo

* Cada **célula livre do labirinto** é um **nó do grafo**.
* Cada **movimento possível** (cima, baixo, esquerda, direita) é uma **aresta**.
* O **peso da aresta** pode ser:

  * `1` (movimento simples),
  * ou valores diferentes (ex.: terreno difícil, água, areia).
* O nó de **início (S)** e o nó de **destino (E)** são os pontos usados no Dijkstra.
* Para geração de labirintos com Prim/Kruskal, a grade de células é tratada como um grafo conexo onde o MST define os caminhos abertos.

---

## 🧠 Como funciona

1. **Entrada do mapa**
   * Usuário pode desenhar manualmente em arquivo `.txt` ou escolher entre mapas prontos.

2. **Construção do grafo**
   * O mapa é convertido para um grafo com base nas células livres e suas conexões.

3. **Execução dos algoritmos**
   * **Dijkstra:** encontra o menor caminho de `S` a `E`.
   * **Prim/Kruskal:** usados para gerar labirintos aleatórios ou conectar regiões isoladas.

4. **Saída**
   * Exibir o labirinto com o caminho encontrado destacado.
   * Se em modo gráfico, mostrar animação da expansão dos algoritmos.

---

## 🚀 Como executar

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/seuusuario/labirinto-grafos.git
   cd labirinto-grafos
   ```

2. **Compilar (modo console simples)**

   ```bash
   gcc main.c -o labirinto
   ./labirinto mapa.txt
   ```

3. **Compilar com ncurses (visualização no terminal)**

   ```bash
   gcc main.c -o labirinto -lncurses
   ./labirinto mapa.txt
   ```

4. **Compilar com SDL2 (visualização gráfica)**

   ```bash
   gcc main.c -o labirinto -lSDL2
   ./labirinto mapa.txt
   ```

5. **Resultado esperado**

   * Caminho mais curto desenhado no mapa.
   * Possibilidade de gerar labirintos novos ou resolver os prontos.

---

## 💡 Observações

- Sistema desenvolvido para o **curso de Engenharia de Software** da UnB-FCTE.
