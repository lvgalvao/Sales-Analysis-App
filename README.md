# Sales Analysis

Este é um aplicativo simples de análise de vendas desenvolvido com o Streamlit. Criei para apresentar as funcionalidades da biblioteca Streamlit e fornecer uma demonstração interativa de análise de dados.

O aplicativo final é esse: [App web](https://lvgalvao-sales-analysis-app-sales-analysis-kedjqa.streamlit.app/)

O dataset utilizado foi esse: [Planilha de Dados](https://docs.google.com/spreadsheets/d/1FThY31ZQV2a4d3eq4WtyL77kSsE-94NvX--XGzYRlZ4/edit?usp=sharing)

Você pode clonar o spreadsheets e inserir os seus próprios dados, necessário manter as mesmas colunas, ou baixar como .csv para fazer o upload na aplicação.

## Requisitos
----------------
<br>

- Python 3.9: Recomenda-se configurar um ambiente Python 3.9 antes de executar o aplicativo. Essa versão é necessária para colocar o app dentro do serviço da cloud do streamlit. Você pode usar o Pyenv para isso, executando o seguinte comando:

```shell
pyenv local 3.9
```

* Dependências: A única dependência direta para executar o aplicativo é o streamlit. Para instalá-la, execute o seguinte comando:
    
```shell
pip install streamlit
```
    
## Resumo do código
----------------

1. **Função `calcular_informacoes_vendas`:** Essa função é responsável por calcular as estatísticas das vendas e exibir as informações no aplicativo, incluindo a exibição dos gráficos interativos.

```python
def calcular_informacoes_vendas(df):
    ...
```
    
2. **Parte principal do aplicativo:** O código principal do aplicativo está dentro do bloco `if data_file is not None:`. Ele exibe o título do aplicativo, permite que o usuário carregue um arquivo CSV, mostra os dados carregados, chama a função `calcular_informacoes_vendas` para processar as informações e exibi-las somente após o usuário realizar o upload.

```python
if data_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(data_file)

    # Mostrar os dados carregados
    st.subheader('Dados Carregados')
    st.write(df)

    # Calcular e mostrar as informações das vendas
    st.header('Informações de Vendas')
    calcular_informacoes_vendas(df)
```
    
3. **Gráfico de Vendas Acumulado Mensal:** É exibido um gráfico de linha mostrando a evolução das vendas acumuladas ao longo do tempo, com base na coluna "Date" do conjunto de dados.

```python
    st.subheader('Gráfico de Vendas Acumulado Mensal')
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    vendas_acumuladas = df.groupby(pd.Grouper(key='Date', freq='M'))['Vendas'].sum().cumsum()
    st.line_chart(vendas_acumuladas)
```
    
4. **Selecionar Produtos Específicos:** Permite ao usuário selecionar produtos específicos por meio de uma caixa de seleção. Em seguida, é exibido um gráfico de barras mostrando as vendas por produto e por vendedor.

```python
    st.subheader('Selecionar Produtos')
    produtos = df['Produto'].unique()
    produtos_selecionados = st.multiselect('Selecione os produtos', produtos)
    if produtos_selecionados:
        df_filtrado = df[df['Produto'].isin(produtos_selecionados)]
        st.subheader('Gráfico de Vendas por Produto por Vendedor')
        vendas_por_produto_vendedor = df_filtrado.groupby(['Produto', 'Vendedor'])['Vendas'].sum().unstack()
        st.bar_chart(vendas_por_produto_vendedor)
```
    
5. **Carregamento de dados via arquivo CSV:** O aplicativo permite ao usuário carregar um arquivo CSV contendo os dados de vendas. O arquivo é carregado por meio do componente `file_uploader` do Streamlit.

```python
st.header('Carregar Dados')
data_file = st.file_uploader('Faça o upload do arquivo CSV', type=['csv'])
```    

Uso
---

Execute o arquivo `sales_analysis.py` com o seguinte comando:

```shell
streamlit run sales_analysis.py
```

O aplicativo será iniciado e você poderá interagir com ele por meio do navegador.