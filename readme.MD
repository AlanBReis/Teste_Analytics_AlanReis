![Teste Analytics - Alan Borges dos Reis](/images/titulo.png)

# Estrutura do projeto
- **data/**: CSVs gerados
  - `data_raw.csv`
  - `data_clean.csv`
- **scripts/**: códigos em Python
  - `gerar_dataset.py` - cria dataset simulado
  - `limpeza_dataset.py` - limpa dataset
  - `analise_vendas.py` - cálculos e análises
- **sql/**: consultas SQL
  - `consultas_sql.sql`
- **relatorios/**: relatórios de insights
  - `relatorio_insights.md`
- **README.md**: este arquivo
- **requirements.txt**: dependências Python

---

## Como executar

1. **Criar e ativar ambiente virtual**:

```bash
python -m venv venv # Ativar o ambiente
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

1. **Installe as dependências**:

```bash
pip install -r requirements.txt
```

## 1. Limpeza e Análise de Dados de Vendas
1. **Executar os scripts na ordem:**
```bash
python scripts/gerar_dataset.py        # cria dataset aleatorio/data_raw.csv
python scripts/limpeza_dataset.py      # faz a limpeza no dataset/data_clean.csv
python scripts/analise_vendas.py       # cálculos de vendas e produto mais vendido
```

## 2. Análise Exploratória de Dados de Vendas
**Grafico linha feito em Power BI onde mostra a tendencias de vendas ao longo do tempo, analisando dados mensalmente.**

## Padrões e insights em : [Insights](relatorios/relatorio_insights.md)


![grafico - power bi](/images/grafico-powerbi.jpg)