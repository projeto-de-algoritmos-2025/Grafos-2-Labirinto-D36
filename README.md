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
<a href="https://youtu.be/UFUj0rDUyyU"><img src="https://i.imgur.com/2LNlNYO.png" width="50%"></a>
</div>

Autores: [Danielle Soares](https://github.com/danielle-soaress) e [Leticia Arisa](https://github.com/Leticia-Arisa-K-Higa).

## 🎯 Objetivo

Desenvolver uma aplicação interativa que permita ao usuário **desenhar ou carregar mapas de labirinto** que contenha obstáculos e resolvê-los utilizando o algoritmo de Dijkstra.

O sistema deve:
- Encontrar o **caminho mais curto** entre dois pontos com **Dijkstra**.  
- Permitir obstáculos ou terrenos que influenciem o trajeto, como monstros ou áreas mais “difíceis”.

## 🔧 Tecnologias e Estruturas Utilizadas

- **Linguagem:** Python 3  
- **Bibliotecas:**  
  - `pygame` → interface gráfica, animações e interação com o usuário  
  - `numpy` → manipulação eficiente de matrizes do labirinto  
- **Estruturas de dados:**  
  - Matrizes (representação do labirinto)  
  - Listas ou dicionários (representação do grafo)  
  - Fila de prioridade (para Dijkstra)  

## 🧩 Modelagem do Grafo

- Cada **célula do labirinto** é um **nó do grafo**.  
- Cada **movimento possível** (cima, baixo, esquerda, direita) é uma **aresta**.  
- O **peso da aresta** pode ser:
  - `1` → movimento simples  
  - Valor maior → terreno mais difícil ou obstáculo (ex.: monstro, água, lama)  
- O nó de **início (E)** e o nó de **destino (S)** são os pontos usados pelo algoritmo de Dijkstra.  

---

## 🧠 Como funciona

1. **Entrada do mapa**  
   - Usuário pode desenhar manualmente o labirinto no Pygame ou carregar mapas prontos em `.txt`.  
   - Exemplo de mapa em `.txt`:
      ```python
      ##########
      #E #    ##
      ##   #  S#
      ##########
      ```
      - Onde: "E" = entrada e "S" = saída.

2. **Construção do grafo**  
   - Cada célula livre é convertida em nó.  
   - Conexões possíveis formam as arestas, com pesos de acordo com obstáculos ou terreno.

3. **Execução dos algoritmos**  
   - **Dijkstra:** encontra o menor caminho do início ao fim, considerando pesos.  
   - **Prim/Kruskal:** gera labirintos aleatórios ou conecta regiões isoladas.

4. **Saída e visualização**  
   - O labirinto e o caminho encontrado são exibidos no Pygame.  
   - Cada passo do algoritmo pode ser animado para mostrar a expansão das buscas.  
   - O usuário pode adicionar obstáculos e ver como eles alteram o caminho mais curto.

---

## 🚀 Como executar

1. **Clonar o repositório**

```bash
git clone https://github.com/projeto-de-algoritmos-2025/Grafos-2-Labirinto-D3
```

3. Entre na pasta do projeto

```bash
cd Projeto
```

4. Instalar dependências

```bash
pip install pygame numpy
```

5. Executar o programa

```bash
python main.py
```


##  💡 Observações

Sistema desenvolvido para o curso de Engenharia de Software da UnB-FCTE.


   

