# ======================================================================
# Análise de Resenhas
# ======================================================================

import pandas as pd
from pathlib import Path
from groq_Connect import gerar_texto_groq
import json

# ------------------------------------------------------------------------------------------------------------
# Etapa 1: Carregar o arquivo .txt e criar uma lista de resenhas
# ------------------------------------------------------------------------------------------------------------
# Definindo o caminho do arquivo
arquivo = Path("resenhas_app_gpt.txt")

# Verificando se o arquivo existe
if not arquivo.exists():
    print(f"Arquivo {arquivo} não encontrado. Certifique-se de que está no diretório correto.")
    exit()

# Lendo o arquivo e criando a lista de resenhas
with arquivo.open("r", encoding="utf-8") as f:
    lista_resenhas = [linha.strip() for linha in f if linha.strip()]

# Criando um DataFrame a partir da lista de resenhas
df = pd.DataFrame(lista_resenhas, columns=["resenha"])

# Exibindo a lista de resenhas carregada
print("Lista de resenhas carregada com sucesso.")
print(df)

# ------------------------------------------------------------------------------------------------------------
# Etapa 2: Enviar lista ao modelo para extração em formato JSON
# ------------------------------------------------------------------------------------------------------------
prompt = (
    "Você é um analista de dados. "
    "Vou te fornecer uma lista de resenhas de usuários. "
    "Sua única tarefa é responder com **apenas JSON válido**. "
    "Formato: uma lista de dicionários. "
    "Cada dicionário deve ter as chaves: "
    '"usuario", "resenha original", "resenha_pt", "avaliacao". '
    "A avaliação deve ser 'Positiva', 'Negativa' ou 'Neutra'. "
    "Não inclua explicações, texto fora do JSON ou comentários. "
    "Responda apenas com JSON."
)

prompt += "\nResenhas:\n" + "\n".join(df["resenha"].tolist())
resposta = gerar_texto_groq(prompt=prompt)

print("\nResposta bruta do modelo:", flush=True)
print(resposta, flush=True)

# ------------------------------------------------------------------------------------------------------------
# Etapa 3: Transformar a resposta do modelo em uma lista de dicionários Python
# ------------------------------------------------------------------------------------------------------------
try:
    lista_dicionarios = json.loads(resposta)
    print("\nResposta convertida em lista de dicionários com sucesso.", flush=True)
except json.JSONDecodeError as e:
    print("Erro ao converter a resposta em JSON:", e, flush=True)
    exit()
except Exception as e:
    print("Erro inesperado:", e, flush=True)
    exit()

if not isinstance(lista_dicionarios, list) or not all(isinstance(item, dict) for item in lista_dicionarios):
    print("A resposta não está no formato esperado de lista de dicionários.", flush=True)
    exit()

print(f"\nNúmero de itens na lista de dicionários: {len(lista_dicionarios)}", flush=True)
print("Primeiros itens da lista de dicionários:", flush=True)
for item in lista_dicionarios[:3]:
    print(item, flush=True)

# ------------------------------------------------------------------------------------------------------------
# Etapa 4: Função para contar avaliações e unir itens em uma string
# ------------------------------------------------------------------------------------------------------------
def analisar_avaliacoes(lista):
    contagem = {"Positiva": 0, "Negativa": 0, "Neutra": 0}
    
    for item in lista:
        avaliacao = item.get("avaliacao")
        if avaliacao in contagem:
            contagem[avaliacao] += 1

    itens_unidos = " | ".join(
        f"Usuário: {item.get('usuario')}, Resenha: {item.get('resenha_pt')}, Avaliação: {item.get('avaliacao')}"
        for item in lista
    )
    
    return contagem, itens_unidos

contagem_avaliacoes, string_itens = analisar_avaliacoes(lista_dicionarios)

print("\nContagem de avaliações:", flush=True)
for chave, valor in contagem_avaliacoes.items():
    print(f" - {chave}: {valor}", flush=True)

print("\nItens unidos em uma string:", flush=True)
print(string_itens, flush=True)
