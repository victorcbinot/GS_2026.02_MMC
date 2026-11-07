# Etapa 2 - Redistribuição da Frota

## A) Análise da demanda de passageiros

De acordo com o Relatório II, cada ônibus possui capacidade para transportar 40 passageiros durante o período analisado.

Para descobrir a quantidade de ônibus necessária em cada região, dividimos a demanda de passageiros pela capacidade de cada veículo.

- **Norte:** 560 / 40 = 14 ônibus.
- **Sul:** 760 / 40 = 19 ônibus.
- **Leste:** 720 / 40 = 18 ônibus.
- **Oeste:** 840 / 40 = 21 ônibus.

Portanto, a quantidade total necessária é de 72 ônibus.

## B) Identificação dos desequilíbrios

Comparando a distribuição original, obtida na Etapa 1, com a quantidade necessária para atender à demanda, identificamos os seguintes desequilíbrios:

| Região | Ônibus atuais | Ônibus necessários | Diferença |
|---|---:|---:|---:|
| Norte | 12 | 14 | -2 |
| Sul | 20 | 19 | +1 |
| Leste | 16 | 18 | -2 |
| Oeste | 24 | 21 | +3 |
| **Total** | **72** | **72** | **0** |

Os valores negativos representam regiões com falta de ônibus, enquanto os positivos representam regiões com veículos excedentes.

Assim, identificamos que Norte e Leste precisam receber ônibus, enquanto Sul e Oeste possuem veículos disponíveis para transferência.

## C) Proposta de política de redistribuição

Propomos uma política de redistribuição baseada na transferência dos ônibus excedentes para as regiões que apresentam déficit.

As transferências estabelecidas são:

- A região Sul transfere 1 ônibus para o Norte.
- A região Oeste transfere 1 ônibus para o Norte.
- A região Oeste transfere 2 ônibus para o Leste.

Essa política foi escolhida para que todas as regiões alcancem exatamente a quantidade de ônibus necessária para atender à demanda estimada, sem aumentar a frota total.

Após a redistribuição, obtemos:

| Região | Antes | Depois |
|---|---:|---:|
| Norte | 12 | 14 |
| Sul | 20 | 19 |
| Leste | 16 | 18 |
| Oeste | 24 | 21 |
| **Total** | **72** | **72** |

## D) Representação da política como transformação linear

Para representar matematicamente a redistribuição, utilizamos a transformação linear:

**T(X) = M · X**

O vetor da distribuição original é:

```text
X = [12, 20, 16, 24]ᵀ
```

A matriz M representa a política de redistribuição, considerando as regiões de origem nas colunas e as regiões de destino nas linhas.

A matriz foi construída com base nas proporções de ônibus transferidos e mantidos em cada região.

## E) Matriz associada e explicação dos coeficientes

A matriz de redistribuição é:

```text
M = [
    [1, 1/20, 0, 1/24],
    [0, 19/20, 0, 0],
    [0, 0, 1, 2/24],
    [0, 0, 0, 21/24]
]
```

Os coeficientes representam as proporções de ônibus destinadas a cada região:

- **1:** todos os ônibus permanecem na região de origem.
- **1/20:** 1 dos 20 ônibus do Sul é transferido para o Norte.
- **19/20:** 19 dos 20 ônibus do Sul permanecem no Sul.
- **1/24:** 1 dos 24 ônibus do Oeste é transferido para o Norte.
- **2/24:** 2 dos 24 ônibus do Oeste são transferidos para o Leste.
- **21/24:** 21 dos 24 ônibus do Oeste permanecem no Oeste.
- **0:** nenhum ônibus é destinado àquela região.

Aplicando a transformação ao vetor original:

```text
X' = M · X

X' = [14, 19, 18, 21]ᵀ
```

Dessa forma, a transformação produz a distribuição planejada na política de redistribuição.

## F) Demonstração da preservação do total e da não negatividade

**Preservação da quantidade total de ônibus**

Para garantir que a transformação preserve a quantidade total de ônibus, a soma dos coeficientes de cada coluna da matriz deve ser igual a 1.

Verificando cada coluna:

- Norte: 1 = 1.
- Sul: 1/20 + 19/20 = 1.
- Leste: 1 = 1.
- Oeste: 1/24 + 2/24 + 21/24 = 1.

Portanto, todos os ônibus são redistribuídos sem que haja criação ou eliminação de veículos.

Isso também pode ser confirmado pela distribuição final:

14 + 19 + 18 + 21 = 72 ônibus.

**Garantia de alocações não negativas**

Todos os coeficientes da matriz são maiores ou iguais a zero. Além disso, a distribuição inicial possui apenas valores não negativos.

Como cada resultado da transformação é uma soma de produtos entre valores não negativos, nenhuma região receberá uma quantidade negativa de ônibus.

No cenário analisado, a distribuição final é composta por 14 ônibus no Norte, 19 no Sul, 18 no Leste e 21 no Oeste.

Portanto, a política preserva a frota total e não produz alocações negativas, atendendo às condições matemáticas estabelecidas para o problema.

**Verificação da integralidade das alocações**

Para a distribuição inicial utilizada neste problema, a transformação também resulta em quantidades inteiras de ônibus, conforme demonstrado nos cálculos e na implementação em Python. Entretanto, como a matriz utiliza proporções, essa garantia de integralidade é válida para a distribuição específica analisada, não necessariamente para qualquer outra distribuição inicial.