# Redes-Mesh-Sem-Fio-para-Sistemas-Autonomos-de-Armazenagem-e-Logistica
Este projeto investiga a aplicação do problema Minimum Vertex Cover na seleção de nós relay em uma rede WiFi Mesh.

# Seleção Adaptativa de Nós Relay Utilizando Vertex Cover para Redes WiFi Mesh

## Visão Geral

Este projeto investiga a aplicação do problema **Minimum Vertex Cover** na seleção de nós relay em uma rede WiFi Mesh.

O objetivo é determinar um subconjunto reduzido de dispositivos capaz de manter a conectividade da rede, minimizando a quantidade de nós ativos utilizados como retransmissores de comunicação.

A motivação principal está relacionada a sistemas autônomos de armazenagem e logística, nos quais robôs móveis, elevadores, sensores e dispositivos IoT precisam manter comunicação contínua enquanto reduzem o consumo de energia.

O projeto compara algoritmos exatos e heurísticos para o problema Vertex Cover e avalia seu desempenho em topologias de redes sem fio geradas automaticamente.

---

# Motivação

Em sistemas autônomos de grande escala, manter todos os dispositivos atuando como nós relay pode resultar em:

* Maior consumo de energia;
* Maior tráfego de comunicação;
* Maior complexidade da rede;
* Redução da autonomia das baterias.

Este trabalho avalia se técnicas baseadas em Vertex Cover podem ser utilizadas para selecionar apenas um subconjunto dos dispositivos para atuar como relay nodes, preservando a conectividade da rede e reduzindo o número de dispositivos ativos.

As aplicações potenciais incluem:

* Robôs Móveis Autônomos (AMRs);
* Sistemas Automatizados de Armazenagem (AS/RS);
* Internet das Coisas Industrial (IIoT);
* Redes WiFi HaLow;
* Redes Mesh sem fio.

---

# Algoritmos Implementados

## Métodos Exatos

### Brute Force

Avalia todas as combinações possíveis de vértices e encontra a solução ótima.

**Características:**

* Solução ótima garantida;
* Complexidade exponencial;
* Utilizado como referência (ground truth).

---

### Backtracking

Explora o espaço de busca realizando podas em ramos que não podem produzir soluções melhores.

**Características:**

* Solução ótima garantida;
* Menor tempo de execução que o Brute Force;
* Complexidade exponencial no pior caso.

---

## Métodos Heurísticos

### Greedy Vertex Cover

Seleciona iterativamente o vértice com maior grau na rede.

**Características:**

* Execução rápida;
* Não garante solução ótima;
* Boa qualidade de solução em muitos cenários.

---

### Edge-Greedy Heuristic

Seleciona uma aresta não coberta e adiciona ambos os vértices à cobertura.

**Características:**

* Execução muito rápida;
* Aproximação clássica do problema Vertex Cover;
* Amplamente utilizada na literatura.

---

# Configuração Experimental

Os experimentos foram executados utilizando os seguintes parâmetros:

| Parâmetro                     | Valor       |
| ----------------------------- | ----------- |
| Número mínimo de dispositivos | 8           |
| Número máximo de dispositivos | 26          |
| Área de cobertura             | 10 m2 |
| Alcance WiFi                  | 8 m         |
| Distribuição superior         | 70%         |
| Distribuição inferior         | 30%         |

Os dispositivos são distribuídos aleatoriamente em uma área bidimensional.

Para representar cenários semelhantes a armazéns automatizados, os nós são concentrados principalmente nas regiões superior e inferior da área.

---

# Geração da Rede

Para cada cenário:

1. Os dispositivos são posicionados aleatoriamente.
2. Um grafo é criado.
3. Dois dispositivos são conectados caso a distância entre eles seja menor ou igual ao alcance WiFi definido.
4. Apenas grafos conectados são aceitos.
5. Todos os algoritmos são executados sobre exatamente o mesmo grafo para permitir comparação justa.

---

# Métricas Avaliadas

## Métricas da Rede

* Conectividade (%)
* Densidade do Grafo (Graph Density)
* Grau Médio dos Vértices (Average Degree)

---

## Métricas dos Algoritmos

* Tamanho do Vertex Cover
* Tempo de Execução (ms)
* Razão de Aproximação (Approximation Ratio)
* Erro Relativo (%)

---

## Métrica Energética

* Economia de Energia (%)

A economia de energia representa a redução do número de dispositivos que precisam permanecer ativos como nós relay quando comparado ao cenário onde todos os dispositivos participam da retransmissão.

---

# Resultados Gerados

## Imagens dos Grafos

Para cada cenário e algoritmo são geradas imagens individuais:

```text
graphs/

N8_run1_BruteForce.png
N8_run1_Backtracking.png
N8_run1_Greedy.png
N8_run1_EdgeGreedy.png

...

N30_runX_EdgeGreedy.png
```

---

## Arquivo CSV Detalhado

Contém:

* Número de dispositivos;
* Número da execução;
* Algoritmo utilizado;
* Tamanho do Vertex Cover;
* Tempo de execução;
* Densidade do grafo;
* Conectividade;
* Grau médio;
* Economia de energia;
* Erro relativo;
* Approximation Ratio;
* Caminho da imagem correspondente ao grafo.

---

## Arquivo CSV Resumido

Contém estatísticas agregadas para cada algoritmo:

* Média;
* Desvio padrão;
* Melhor resultado obtido;
* Tempo médio;
* Economia média de energia.

---

## Gráficos Comparativos

O sistema gera automaticamente gráficos comparativos contendo os quatro algoritmos:

* Comparação de Tempo de Execução;
* Comparação do Tamanho do Vertex Cover;
* Comparação do Erro Relativo;
* Comparação da Razão de Aproximação;
* Comparação da Economia de Energia.

---

# Estrutura do Projeto

```text
project/

├── algorithms/
│   ├── brute_force.py
│   ├── backtracking.py
│   ├── greedy.py
│   └── edge_greedy.py
│
├── graph_generation/
│   └── graph_generator.py
│
├── metrics/
│   └── metrics.py
│
├── reports/
│   ├── csv_writer.py
│   └── plot_generator.py
│
├── visualizations/
│   └── graph_visualizer.py
│
├── graphs/
├── plots/
│
├── vertex_cover_detailed.csv
├── vertex_cover_summary.csv
│
└── main.py
```

---

# Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
```

Instale as dependências:

```bash
pip install networkx matplotlib
```

Execute:

```bash
python main.py
```

O programa solicitará:

```text
Número mínimo de dispositivos
Número máximo de dispositivos
Número de repetições
Tamanho da área
Alcance WiFi
```

---

# Trabalhos Futuros

Possíveis extensões deste projeto:

* Modelagem de propagação WiFi HaLow;
* Mobilidade dinâmica dos dispositivos;
* Seleção de relays baseada em bateria;
* Branch and Bound;
* Algoritmos Genéticos;
* Simulated Annealing;
* Reconfiguração dinâmica da rede Mesh;
* Otimização de roteamento multi-hop;
* Integração com simuladores de armazéns automatizados;
* Integração com CoppeliaSim.

---

# Autor

**Carlos Erlan Olival Lima**

Projeto de Pesquisa de Doutorado

**Redes Mesh Sem Fio para Sistemas Autônomos de Armazenagem e Logística**
