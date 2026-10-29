import os
import sys

# Garante que o yfinance está instalado e atualizado no ambiente do IDLE
print("Verificando e instalando dependências necessárias...")
os.system(f'"{sys.executable}" -m pip install --upgrade yfinance pandas matplotlib requests')

import yfinance as yf
import matplotlib.pyplot as plt

# Definir o ativo: USDBRL=X traz o histórico do dólar comercial em relação ao Real
ticker = "USDBRL=X"

print("\nBuscando dados de cotação reais no Yahoo Finance...")

try:
    # Busca o histórico dos últimos 2 anos com intervalo diário
    dados = yf.download(ticker, period="2y", interval="1d")
    
    if dados.empty:
        raise Exception("Nenhum dado foi retornado pela API. Verifique sua conexão com a internet.")
        
    # Seleciona a coluna de fechamento (Close)
    precos_fechamento = dados['Close']
    
    # Montar a Análise Visual
    plt.figure(figsize=(10, 5))
    plt.plot(precos_fechamento.index, precos_fechamento.values, color='#2ca02c', linewidth=2)
    
    # Customização visual limpa e profissional para Portfólio
    plt.title('Evolução da Cotação do Dólar (USDBRL) - Últimos 2 Anos', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Data', fontsize=11)
    plt.ylabel('Preço em Reais (R$)', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    print("Sucesso! Abrindo gráfico na tela...")
    plt.show()

except Exception as e:
    print(f"\nErro ao processar os dados: {e}")
