import requests
import pandas as pd

def fetch_data(url, output_filename, period_column, additional_columns):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('value', [])
        
        if data:
            df = pd.DataFrame(data)
            
            if period_column in df.columns:
                df['ano'] = df[period_column].str[:4]
                
                if period_column == 'datatrimestre':
                    df['trimestre'] = df[period_column].str[-2:]
                    columns_order = [period_column, 'ano', 'trimestre'] + additional_columns
                else:
                    columns_order = [period_column, 'ano'] + additional_columns
                
                df = df[columns_order]
                df.to_csv(output_filename, index=False)
                print(f"Arquivo CSV gerado com os dados: {output_filename}")
            else:
                print(f"A coluna '{period_column}' não está disponível nos dados retornados.")
        else:
            print("Nenhum dado disponível para os parâmetros selecionados.")
    else:
        print(f"Erro na requisição: {response.status_code}")
        print(response.text)

urls = {
    "dados_trimestrais": (
        "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/"
        "MeiosdePagamentosTrimestralDA(trimestre='20151')?$top=999&$format=json&"
        "$select=datatrimestre,valorCartaoCredito,valorCartaoDebito,valorDebitoDireto,valorTransIntrabancaria,"
        "valorCartaoPrePago,valorConvenios,valorSaques,quantidadeCartaoCredito,quantidadeCartaoDebito,"
        "quantidadeDebitoDireto,quantidadeTransIntrabancaria,quantidadeCartaoPrePago,quantidadeConvenios,"
        "quantidadeSaques,valorPix,valorTED,valorCheque,valorBoleto,valorDOC,"
        "quantidadePix,quantidadeTED,quantidadeCheque,quantidadeBoleto,quantidadeDOC"
    )
}

columns = {
    "dados_trimestrais": [
        'valorCartaoCredito', 'valorCartaoDebito', 'valorDebitoDireto', 'valorTransIntrabancaria',
        'valorCartaoPrePago', 'valorConvenios', 'valorSaques', 'quantidadeCartaoCredito', 'quantidadeCartaoDebito',
        'quantidadeDebitoDireto', 'quantidadeTransIntrabancaria', 'quantidadeCartaoPrePago',
        'quantidadeConvenios', 'quantidadeSaques','valorPix', 'valorTED', 'valorCheque', 'valorBoleto', 'valorDOC',
        'quantidadePix', 'quantidadeTED', 'quantidadeCheque', 'quantidadeBoleto', 'quantidadeDOC'
    ]
}

fetch_data(urls['dados_trimestrais'], 'dados_trimestrais.csv', 'datatrimestre', columns['dados_trimestrais'])
