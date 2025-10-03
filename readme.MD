# Teste Analytics - Alan Borges dos Reis

## Estrutura do projeto
- **data/**: CSVs gerados
  - `data_raw.csv`
  - `data_clean.csv`
- **images/**: Imagens ilustrativas
- **relatorios/**: relatórios de insights
  - `relatorio_insights.md`
- **scripts/**: códigos em Python
  - `gerar_dataset.py` - cria dataset simulado
  - `limpeza_dataset.py` - limpa dataset
  - `analise_vendas.py` - cálculos e análises
  - `criar_db.py` - criação de banco de dados
  - `consulta_sqlite.py` - execução e Visualização das Consultas SQL
- **sql/**: consultas SQL
  - `consultas_sql.sql`
- **requirements.txt**: dependências Python

---

## Como executar

 **Criar e ativar ambiente virtual**:

```bash
python -m venv venv # Ativar o ambiente
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

 **Installe as dependências**:

```bash
pip install -r requirements.txt
```

## Limpeza e Análise de Dados de Vendas
**Executar os scripts na ordem:**
```bash
python scripts/gerar_dataset.py        # cria dataset aleatorio/data_raw.csv
python scripts/limpeza_dataset.py      # faz a limpeza no dataset/data_clean.csv
python scripts/analise_vendas.py       # cálculos de vendas e produto mais vendido
```

## Análise Exploratória de Dados de Vendas
**Grafico linha feito em Power BI onde mostra a tendencias de vendas ao longo do tempo, analisando dados mensalmente.**

## Padrões e insights em : [Insights](relatorios/relatorio_insights.md)


![grafico - power bi](/images/grafico-powerbi.jpg)


# SQL
Nesta etapa, as consultas foram elaboradas com base no arquivo data_clean.csv.

## Observação sobre o Dataset:
Para atender ao requisito de identificar vendas de junho de 2024, o script gerar_dataset.py foi ajustado para simular dados de 01/01/2023 a 31/12/2025.
Consequentemente, o script limpeza_dataset.py sobrescreveu o data_clean.csv com o dataset completo.

## Validação das Consultas
As consultas SQL foram salvas em sql/consultas_sql.sql. Para executá-las no banco de dados local:
Criação do Banco de Dados: Carregar os dados limpos em uma base SQLite.
```bash
python scripts/criar_db.py 
```
Execução e Visualização das Consultas SQL: Executar o script que lê o consultas_sql.sql e exibe os resultados no terminal, validando a Parte 2.
```bash
python scripts/executar_consultas_sql.py
```

![grafico - power bi](/images/image.png)

# Interpretação de Resultados

 Relatório e principais insights em [Relatório](relatorios/relatorio_insights.md)

# Apresentação em Vídeo
 A gravação explicando o projeto pode ser acessada pelo [Youtube](https://youtu.be/ujBTeluvPyA)