"""
Análise de Dados com Python [T1]
Mini-Projeto Avaliativo - Módulo 1 - Semana 07
Aluno: Telmo Rangel
Turma: T1

COMMIT 01: Carregamento Estruturado e Diagnóstico Inicial
"""

import warnings
import pandas as pd

# Configurações de otimização de visualização do terminal
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)

# =====================================================================
# CARREGAMENTO E MANIPULAÇÃO ESTRUTURADA
# =====================================================================
print("=" * 70)
print("CARREGAMENTO E DIAGNÓSTICO DA BASE")
print("=" * 70)

# Leitura estruturada do arquivo CSV
df_varejo = pd.read_csv(r"Base Varejo.csv", encoding="latin-1", sep=";")
print(df_varejo.head())

# Verificar valores nulos por coluna
print("\n--- VALORES NULOS POR COLUNA ---")
print(df_varejo.isnull().sum())

# As colunas Unnamed: 10, Unnamed: 11, Unnamed: 12, Unnamed: 13 possuem todos os seus dados nulos
# Elimina apenas as colunas onde TODOS os valores são nulos
df_varejo = df_varejo.dropna(axis=1, how="all")

print("\n--- BASE APÓS REMOÇÃO DE COLUNAS VAZIAS ---")
print(df_varejo.head())
print(df_varejo.isnull().sum())
print()

df_varejo.info()
print(f"Tamanho: {df_varejo.shape[0]} linhas e {df_varejo.shape[1]} colunas")

# Listar linhas duplicadas do data frame
print(f"Linhas 100% duplicadas: {df_varejo.duplicated().sum()}")
print("=" * 70)
