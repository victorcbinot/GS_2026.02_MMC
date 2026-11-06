# Global Solution - Modelagem Matemática e Computacional

## Sobre o projeto

Este projeto foi desenvolvido como parte da Global Solution da disciplina de Modelagem Matemática e Computacional (MMC), da FIAP.

O objetivo é utilizar conceitos de Matemática, Álgebra Linear e programação em Python para desenvolver uma solução relacionada à mobilidade urbana inteligente, considerando a distribuição e a redistribuição de ônibus entre quatro regiões de uma cidade: Norte, Sul, Leste e Oeste.

O projeto está dividido em duas etapas, contemplando a modelagem matemática do problema e o desenvolvimento de uma proposta de redistribuição da frota.

## Estrutura do projeto

```text
Global-Solution-MMC/
│
├── README.md
├── requirements.txt
│
├── etapa_1/
│   ├── README.md
│   └── resolucao.py
│
└── etapa_2/
    ├── README.md
    └── redistribuicao.py
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `README.md` | Documentação geral do projeto. |
| `requirements.txt` | Bibliotecas necessárias para executar o projeto. |
| `etapa_1/README.md` | Documentação da modelagem matemática e dos itens A até F. |
| `etapa_1/resolucao.py` | Implementação e resolução do sistema de equações. |
| `etapa_2/README.md` | Documentação da proposta de redistribuição dos ônibus. |
| `etapa_2/redistribuicao.py` | Implementação da política de redistribuição. |

## Tecnologias utilizadas

- **Python:** linguagem utilizada para implementar os modelos matemáticos.
- **NumPy:** biblioteca utilizada para operações com matrizes e resolução de sistemas lineares.

## Requisitos

Para executar o projeto, é necessário ter:

- Python 3 instalado.
- pip (gerenciador de pacotes do Python).

## Instalação das dependências

Com o terminal aberto na pasta raiz do projeto, execute:

```bash
pip install -r requirements.txt
```

Esse comando instala as bibliotecas necessárias para executar os códigos.

## Como executar o projeto

Os códigos das duas etapas podem ser executados separadamente, utilizando o terminal na pasta raiz do projeto.

### Etapa 1 - Modelagem Matemática

Para executar a implementação da primeira etapa, utilize:

```bash
python etapa_1/resolucao.py
```

O programa resolve o sistema de equações, calcula o determinante da matriz e verifica os resultados encontrados.

### Etapa 2 - Redistribuição dos ônibus

Para executar a implementação da segunda etapa, utilize:

```bash
python etapa_2/redistribuicao.py
```

O programa será responsável por executar a política de redistribuição desenvolvida pela equipe, considerando as condições e restrições estabelecidas no problema.

## Organização do desenvolvimento

- **Etapa 1:** definição das variáveis, construção do modelo matemático, representação matricial, investigação da unicidade da solução, implementação em Python e verificação das equações.
- **Etapa 2:** análise da demanda por região, identificação dos desequilíbrios, desenvolvimento de uma política de redistribuição, representação por transformação linear e verificação das condições do problema.
