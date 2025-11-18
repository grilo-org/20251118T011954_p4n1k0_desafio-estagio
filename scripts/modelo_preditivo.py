# importações necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# 1. Carregamento dos Dados
# OBS: O caminho do arquivo ('scripts/leads.csv') deve ser ajustado
# se você rodar o script de um diretório diferente.
try:
    df = pd.read_csv('scripts/leads.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'scripts/leads.csv' não foi encontrado. Verifique o caminho.")
    exit()

# Visualização inicial
print("--- DataFrame Inicial ---")
print(df.head())

# 2. Preparação e Pré-processamento
# Remover a coluna de identificação, que não tem poder preditivo
df = df.drop('id_visitante', axis=1)

# Converter a variável alvo (Target) de texto para binário (0/1)
# 'sim' -> 1 (Converteu), 'não' -> 0 (Não Converteu)
df['converteu_em_cliente'] = df['converteu_em_cliente'].map({'sim': 1, 'não': 0})

# Aplicar One-Hot Encoding nas variáveis categóricas
# 'cidade_lead' e 'setor_empresa' são transformadas em colunas numéricas binárias.
df_encoded = pd.get_dummies(df, columns=['cidade_lead', 'setor_empresa'], drop_first=True)

# 3. Definição de Variáveis
X = df_encoded.drop('converteu_em_cliente', axis=1) # Features (Tudo exceto o Target)
y = df_encoded['converteu_em_cliente'] # Target

# 4. Divisão dos dados (Treino e Teste)
# Usando 'stratify=y' para garantir que a proporção de conversão seja igual em Treino e Teste.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 5. Treinamento do Modelo (Regressão Logística)
model = LogisticRegression(solver='liblinear', random_state=42)
model.fit(X_train, y_train)

# 6. Avaliação
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1] # Probabilidade de conversão para o AUC-ROC

print("\n--- Resultados do Protótipo de Lead Scoring ---")
print(f"Acurácia (Geral): {accuracy_score(y_test, y_pred):.3f}")
print(f"AUC-ROC (Poder Preditivo): {roc_auc_score(y_test, y_proba):.3f}")
print("\nRelatório de Classificação (Detalhado):\n", classification_report(y_test, y_pred, zero_division=0))
