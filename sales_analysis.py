import streamlit as st
import pandas as pd

# Criamos uma função para calcular as informações
# O objetivo ao utilizar a função é 'chamar' os gráficos somente após o usuário carregar os dados no app

def calcular_informacoes_vendas(df):

    # Estatísticas básicas sobre as vendas
    total_vendas = df['Vendas'].sum()
    media_vendas = df['Vendas'].mean()
    max_vendas = df['Vendas'].max()
    min_vendas = df['Vendas'].min()


    # Mostrar as informações calculadas anteriormente
    col1, col2 = st.columns(2)
    col1.markdown(f"Total de Vendas: **`{total_vendas}`**")
    col2.markdown(f"Média de Vendas: **`{media_vendas}`**")

    col1.markdown(f"Maior Venda: **`{max_vendas}`**")
    col2.markdown(f"Menor Venda: **`{min_vendas}`**")



    # Gráfico de vendas acumulado mensal
    st.subheader('Gráfico de Vendas Acumulado Mensal')
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    vendas_acumuladas = df.groupby(pd.Grouper(key='Date', freq='M'))['Vendas'].sum().cumsum()
    st.line_chart(vendas_acumuladas)

    # Selecionar produtos específicos
    st.subheader('Selecionar Produtos')
    produtos = df['Produto'].unique()
    produtos_selecionados = st.multiselect('Selecione os produtos', produtos)
    if produtos_selecionados:
        df_filtrado = df[df['Produto'].isin(produtos_selecionados)]
        st.subheader('Gráfico de Vendas por Produto por Vendedor')
        vendas_por_produto_vendedor = df_filtrado.groupby(['Produto', 'Vendedor'])['Vendas'].sum().unstack()
        st.bar_chart(vendas_por_produto_vendedor)

# Parte principal do app
st.title('Análise de Vendas')

# Carregar os dados
st.header('Carregar Dados')
data_file = st.file_uploader('Faça o upload do arquivo CSV', type=['csv'])

if data_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(data_file)

    # Mostrar os dados carregados
    st.subheader('Dados Carregados')
    st.write(df)

    # Calcular e mostrar as informações das vendas
    st.header('Informações de Vendas')
    calcular_informacoes_vendas(df)
