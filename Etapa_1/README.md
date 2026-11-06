# Etapa 1 - Modelagem Matemática e Computacional

## A) Definição das variáveis

Para representar a distribuição dos ônibus entre as quatro regiões da cidade, foram definidas as seguintes variáveis:

- **N:** quantidade de ônibus destinados à região Norte.
- **S:** quantidade de ônibus destinados à região Sul.
- **L:** quantidade de ônibus destinados à região Leste.
- **O:** quantidade de ônibus destinados à região Oeste.

Todas as variáveis representam quantidades inteiras e não negativas de ônibus.

## B) Construção do modelo matemático

Com base nas relações operacionais apresentadas no enunciado, foram construídas quatro equações:

1. Norte + Oeste + dobro do Sul = 76

   `N + O + 2S = 76`

2. Sul + dobro do Leste = 52

   `S + 2L = 52`

3. Norte + Leste + dobro do Oeste = 76

   `N + L + 2O = 76`

4. Quantidade total de ônibus = 72

   `N + S + L + O = 72`

### Resolução algébrica do sistema

Para encontrar os valores das quatro variáveis, foram realizadas manipulações algébricas no sistema de equações.

**1. Subtraindo a primeira equação da terceira:**

`(N + L + 2O) - (N + O + 2S) = 76 - 76`

Simplificando:

`L + O - 2S = 0`

Isolando L:

`L = 2S - O`

**2. Substituindo o valor de L na segunda equação:**

`S + 2(2S - O) = 52`

`S + 4S - 2O = 52`

`5S - 2O = 52`

Isolando S:

`S = (52 + 2O) / 5`

**3. Utilizando a equação da frota total:**

`N + S + L + O = 72`

Substituindo L por `2S - O`:

`N + S + (2S - O) + O = 72`

Simplificando:

`N + 3S = 72`

**4. Subtraindo essa última equação da primeira:**

`(N + O + 2S) - (N + 3S) = 76 - 72`

Simplificando:

`O - S = 4`

Isolando O:

`O = S + 4`

**5. Substituindo O na expressão de S:**

`S = (52 + 2(S + 4)) / 5`

`S = (52 + 2S + 8) / 5`

`S = (60 + 2S) / 5`

Multiplicando os dois lados por 5:

`5S = 60 + 2S`

`3S = 60`

`S = 20`

**6. Encontrando as demais variáveis:**

Como `O = S + 4`:

`O = 20 + 4`

`O = 24`

Como `L = 2S - O`:

`L = 2(20) - 24`

`L = 16`

Utilizando `N + 3S = 72`:

`N + 3(20) = 72`

`N = 72 - 60`

`N = 12`

**Resultado encontrado:**

- Norte (N): 12 ônibus.
- Sul (S): 20 ônibus.
- Leste (L): 16 ônibus.
- Oeste (O): 24 ônibus.

Total: 12 + 20 + 16 + 24 = 72 ônibus.

## C) Representação matricial do sistema

Para representar o sistema na forma matricial, foi utilizada a seguinte organização das variáveis: N, S, L e O.

**Matriz dos coeficientes (A):**

```text
| 1  2  0  1 |
| 0  1  2  0 |
| 1  0  1  2 |
| 1  1  1  1 |
```

**Vetor das variáveis (X):**

```text
| N |
| S |
| L |
| O |
```

**Vetor dos resultados (B):**

```text
| 76 |
| 52 |
| 76 |
| 72 |
```

Dessa forma, o sistema pode ser representado pela expressão:

`A · X = B`

Cada linha da matriz A corresponde a uma das quatro equações do modelo matemático, enquanto suas colunas representam as variáveis N, S, L e O, nessa ordem.

## D) Investigação da unicidade da solução

Para investigar se o sistema possui uma única solução, utilizamos o conceito de determinante de uma matriz quadrada.

O determinante permite verificar se a matriz dos coeficientes é invertível. Quando o determinante é diferente de zero, o sistema possui uma única solução.

A matriz utilizada nesta análise é:

```text
| 1  2  0  1 |
| 0  1  2  0 |
| 1  0  1  2 |
| 1  1  1  1 |
```

Calculando o determinante, podemos realizar as seguintes operações nas linhas:

- Subtrair a primeira linha da terceira linha.
- Subtrair a primeira linha da quarta linha.

Essas operações não alteram o valor do determinante.

A matriz fica:

```text
| 1   2  0  1 |
| 0   1  2  0 |
| 0  -2  1  1 |
| 0  -1  1  0 |
```

Expandindo o determinante pela primeira coluna, obtemos:

```text
|  1  2  0 |
| -2  1  1 |
| -1  1  0 |
```

Calculando o determinante dessa matriz 3x3:

`1 × (1 × 0 - 1 × 1) - 2 × (-2 × 0 - 1 × -1)`

`= -1 - 2`

`= -3`

Portanto:

`det(A) = -3`

Como o determinante é diferente de zero, concluímos que a matriz é invertível e que o sistema possui uma única solução.

Isso significa que existe apenas uma combinação de quantidades de ônibus que satisfaz simultaneamente as quatro equações do modelo.

## E) Implementação em Python

Para implementar o modelo matemático, foi utilizada a biblioteca NumPy, que permite trabalhar com matrizes e realizar operações de Álgebra Linear.

No arquivo `resolucao.py`, a matriz dos coeficientes e o vetor dos resultados são representados por arrays do NumPy.

A função `numpy.linalg.solve()` é utilizada para resolver o sistema linear e encontrar os valores das variáveis.

Também foi utilizada a função `numpy.linalg.det()` para calcular o determinante da matriz e verificar a condição de unicidade da solução.

A implementação completa está disponível no arquivo `resolucao.py`, localizado nesta mesma pasta.

## F) Verificação das equações

Após encontrar os valores das variáveis, foi realizada a substituição dos resultados nas quatro equações originais.

**Primeira equação:**

`N + O + 2S = 76`

`12 + 24 + 2(20) = 76`

`76 = 76`

**Segunda equação:**

`S + 2L = 52`

`20 + 2(16) = 52`

`52 = 52`

**Terceira equação:**

`N + L + 2O = 76`

`12 + 16 + 2(24) = 76`

`76 = 76`

**Quarta equação:**

`N + S + L + O = 72`

`12 + 20 + 16 + 24 = 72`

`72 = 72`

Portanto, os valores encontrados satisfazem todas as equações do sistema e respeitam a quantidade total de 72 ônibus.

A implementação em Python também realiza essas verificações automaticamente, comparando os resultados calculados com os valores esperados.