import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Matriz que representa a política de redistribuição
M = np.array([
    [1, 1/20, 0, 1/24],
    [0, 19/20, 0, 0],
    [0, 0, 1, 2/24],
    [0, 0, 0, 21/24]
], dtype=float)

# Distribuição original obtida na Etapa 1: Norte, Sul, Leste e Oeste
distribuicao_original = np.array([12, 20, 16, 24])

# Dados do Relatório II
passageiros = np.array([560, 760, 720, 840])
capacidade_por_onibus = 40

# Demanda estimada de ônibus por região
demanda = np.ceil(passageiros / capacidade_por_onibus).astype(int)

# Análise da demanda e dos desequilíbrios
regioes = ["Norte", "Sul", "Leste", "Oeste"]
diferencas = distribuicao_original - demanda

print("ANÁLISE DA DEMANDA E DOS DESEQUILÍBRIOS\n")
print(f"{'Região':<8}{'Atuais':>8}{'Necessários':>13}{'Diferença':>11}")

for i, regiao in enumerate(regioes):
    print(f"{regiao:<8}{distribuicao_original[i]:>8}{demanda[i]:>13}{diferencas[i]:>+11}")

# Aplicação da transformação linear
nova_distribuicao = M @ distribuicao_original

# Exibição dos resultados
print("\nDISTRIBUIÇÃO APÓS A REDISTRIBUIÇÃO\n")

for i, regiao in enumerate(regioes):
    print(f"{regiao}: {nova_distribuicao[i]:.0f} ônibus")

# Verificações matemáticas
print("\nVERIFICAÇÕES")

# Verifica se o total de ônibus foi preservado
total_original = np.sum(distribuicao_original)
total_final = np.sum(nova_distribuicao)

print(f"Total original: {total_original:.0f}")
print(f"Total final: {total_final:.0f}")
print(f"Total preservado: {total_original == total_final}")

# Verifica se os coeficientes são não negativos
print(f"Coeficientes não negativos: {np.all(M >= 0)}")

# Verifica se cada coluna soma 1
print(f"Colunas somam 1: {np.allclose(np.sum(M, axis=0), 1)}")

# Verifica se as quantidades finais são não negativas
print(f"Alocações não negativas: {np.all(nova_distribuicao >= 0)}")

# Verifica se as quantidades finais são inteiras
print(f"Alocações inteiras: {np.allclose(nova_distribuicao, np.round(nova_distribuicao))}")

# Verifica se a distribuição atende à demanda
print(f"Demanda atendida: {np.allclose(nova_distribuicao, demanda)}")
