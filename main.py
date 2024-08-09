import requests
import pandas as pd

# URL da API com parâmetros ajustados para dados mensais
url = (
    "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/"
    "MeiosdePagamentosMensalDA(AnoMes='201501')?$top=999&$format=json&"
    "$select=AnoMes,valorPix,valorTED,valorCheque,valorBoleto,valorDOC,"
    "quantidadePix,quantidadeTED,quantidadeCheque,quantidadeBoleto,quantidadeDOC"
)

# Fazer a requisição à API
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrair os dados do JSON
    data = response.json().get('value', [])
    
    # Verificar se há dados
    if data:
        # Transformar os dados em um DataFrame do pandas
        df = pd.DataFrame(data)
        
        # Verificar se a coluna 'AnoMes' existe e extrair os dados necessários
        if 'AnoMes' in df.columns:
            # Adicionar colunas de ano, mês e semestre
            df['ano'] = df['AnoMes'].str[:4]
            df['mes'] = df['AnoMes'].str[4:]
            df['semestre'] = df['mes'].apply(lambda x: 'Semestre 1' if int(x) <= 6 else 'Semestre 2')
            
            # Reordenar as colunas para incluir 'ano', 'semestre', e 'AnoMes' no início
            columns_order = [
                'AnoMes', 'ano', 'mes', 'semestre',
                'valorPix', 'valorTED', 'valorCheque', 'valorBoleto', 'valorDOC',
                'quantidadePix', 'quantidadeTED', 'quantidadeCheque', 'quantidadeBoleto', 'quantidadeDOC'
            ]
            df = df[columns_order]
            
            # Exportar todos os dados para um único arquivo CSV
            df.to_csv('dados_mensais.csv', index=False)
            print("Arquivo CSV gerado com todos os dados.")
        else:
            print("A coluna 'AnoMes' não está disponível nos dados retornados.")
    else:
        print("Nenhum dado disponível para os parâmetros selecionados.")
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
