import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="FinTrack AI",
    layout="centered"
)

# Título
st.title("FinTrack AI")
st.subheader("Controle inteligente dos seus gastos")

# Carregar dados
try:
    transacoes = pd.read_csv("data/transacoes.csv")
except:
    st.error("Erro ao carregar os dados. Verifique o caminho do arquivo.")
    st.stop()

RENDA_ESTIMADA = 3500

# =========================
# Funções principais
# =========================

def analisar_gastos():
    total = transacoes["valor"].sum()
    percentual = (total / RENDA_ESTIMADA) * 100

    gastos_categoria = transacoes.groupby("categoria")["valor"].sum()
    maior_categoria = gastos_categoria.idxmax()

    return f"""
Você gastou R$ {total:.2f} no mês.

Isso representa aproximadamente {percentual:.0f}% da sua renda estimada.

A categoria com maior gasto foi: {maior_categoria}.
"""


def sugestao_economia():
    return """
Com base nos seus gastos, você pode reduzir despesas recorrentes.

Uma estratégia simples é diminuir gastos com alimentação fora ou compras não essenciais.

Uma redução de 10% já pode gerar uma economia mensal relevante.
"""


def simulacao():
    valor = 300
    meses = 12
    total = valor * meses

    return f"""
Se você guardar R$ {valor} por mês durante {meses} meses,
terá aproximadamente R$ {total}.
"""


def responder(pergunta):
    pergunta = pergunta.lower()

    if "gastei" in pergunta:
        return analisar_gastos()

    elif "economizar" in pergunta:
        return sugestao_economia()

    elif "guardar" in pergunta or "juntar" in pergunta:
        return simulacao()

    elif "investimento" in pergunta:
        return "Para um perfil conservador, opções como CDB e Tesouro Selic são mais seguras."

    else:
        return "Não encontrei dados suficientes para responder com segurança."

# =========================
# Interface
# =========================

st.write("---")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    resposta = responder(pergunta)
    st.write(resposta)

st.write("---")

st.caption("Projeto desenvolvido para fins educacionais com foco em IA e análise financeira.")