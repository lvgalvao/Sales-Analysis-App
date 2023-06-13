# Sales Analysis

Este é um aplicativo simples de análise de vendas desenvolvido com o Streamlit. Criei com o objetivo de apresentar as funcionalidades da biblioteca Streamlit e fornecer uma demonstração interativa de análise de dados.

## Requisitos
----------------
<br>

- Python 3.9: Recomenda-se configurar um ambiente Python 3.9 antes de executar o aplicativo. Essa versão é necessária para colocar o app dentro do serviço da cloud do streamlit. Você pode usar o Pyenv para isso, executando o seguinte comando:
<br>
<br>
```shell
pyenv local 3.9
```

* Dependências: A única dependências direta para executar o aplicativo é o streamlit. Para instalá-la, execute o seguinte comando:
    
```shell
pip install streamlit
```
    

## Resumo do código
----------------


O arquivo `sales_analysis.py` contém as seguintes partes principais:

1. **Função `calcular_informacoes_vendas`:** Essa função é responsável por calcular as estatísticas das vendas e exibir as informações no aplicativo, incluindo a exibição dos gráficos interativos.
    
2. **Parte principal do aplicativo:** O código principal do aplicativo está dentro do bloco `if __name__ == '__main__'`. Ele exibe o título do aplicativo, permite que o usuário carregue um arquivo CSV, mostra os dados carregados, chama a função `calcular_informacoes_vendas` para processar as informações e exibi-las.
    
3. **Gráfico de Vendas Acumulado Mensal:** É exibido um gráfico de linha mostrando a evolução das vendas acumuladas ao longo do tempo, com base na coluna "Date" do conjunto de dados.
    
4. **Selecionar Produtos Específicos:** Permite ao usuário selecionar produtos específicos por meio de uma caixa de seleção. Em seguida, é exibido um gráfico de barras mostrando as vendas por produto e por vendedor.
    
5. **Carregamento de dados via arquivo CSV:** O aplicativo permite ao usuário carregar um arquivo CSV contendo os dados de vendas. O arquivo é carregado por meio do componente `file_uploader` do Streamlit.
    

Uso
---

Execute o arquivo `sales_analysis.py` com o seguinte comando:

```shell
streamlit run sales_analysis.py
```

O aplicativo será iniciado e você poderá interagir com ele por meio do navegador.

Contribuição
------------

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
-------

Este projeto está licenciado sob a [MIT License](LICENSE).

```javascript

Certifique-se de substituir o conteúdo do arquivo `LICENSE` pelo texto adequado da licença que você deseja utilizar.
```