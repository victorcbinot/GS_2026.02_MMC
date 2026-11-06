import numpy as np

# Matriz dos coeficientes
A = np.array([
    [1, 2, 0, 1],
    [0, 1, 2, 0],
    [1, 0, 1, 2],
    [1, 1, 1, 1]
], dtype=float)

# Vetor dos resultados
B = np.array([76, 52, 76, 72], dtype=float)


# D) Investigação da unicidade da solução

determinante = np.linalg.det(A)

print("DETERMINANTE DA MATRIZ")
print(f"Determinante: {determinante:.2f}")

if not np.isclose(determinante, 0):
    print("A matriz é invertível.")
    print("O sistema possui uma única solução.")
else:
    print("A matriz não é invertível.")
    print("É necessário investigar a existência de soluções.")


# E) Resolução do sistema em Python

solucao = np.linalg.solve(A, B)

N, S, L, O = solucao

print("\nSOLUÇÃO DO SISTEMA")
print(f"Norte: {N:.0f} ônibus")
print(f"Sul: {S:.0f} ônibus")
print(f"Leste: {L:.0f} ônibus")
print(f"Oeste: {O:.0f} ônibus")


# F) Verificação das equações

resultados = A @ solucao

print("\nVERIFICAÇÃO DAS EQUAÇÕES")

for i, resultado in enumerate(resultados):
    esperado = B[i]

    print(
        f"Equação {i + 1}: "
        f"{resultado:.2f} = {esperado:.2f} "
        f"-> {'Correta' if np.isclose(resultado, esperado) else 'Incorreta'}"
    )


# Verificação das condições do problema

total_onibus = sum(solucao)

quantidades_validas = (
    np.all(solucao >= 0)
    and np.allclose(solucao, np.round(solucao))
)

total_valido = np.isclose(total_onibus, 72)

print("\nVERIFICAÇÃO DAS CONDIÇÕES")
print(f"Total de ônibus: {total_onibus:.0f}")
print(f"Quantidades inteiras e não negativas: {quantidades_validas}")
print(f"Total de 72 ônibus respeitado: {total_valido}")

if quantidades_validas and total_valido and np.allclose(resultados, B):
    print("\nTodas as verificações foram aprovadas!")
else:
    print("\nAlguma verificação apresentou problemas.")