# Análise de Dados de Meios de Pagamento - Banco Central do Brasil

Este repositório contém um script Python que extrai e analisa dados mensais de meios de pagamento fornecidos pelo Banco Central do Brasil.

## Funcionalidades

- **Requisição de Dados**: Obtém dados sobre transações de diferentes tipos (Pix, TED, Cheque, Boleto, DOC) usando a API do Banco Central.
- **Processamento de Dados**: Converte os dados JSON em um DataFrame do pandas, adiciona colunas para ano, mês e semestre, e organiza as colunas.
- **Exportação para CSV**: Gera um arquivo CSV contendo todos os dados processados.

## Como Usar

1. **Instale as dependências**:
   ```bash
   pip install requests pandas
   ```

2. **Execute o script**:
   ```bash
   python nome_do_script.py
   ```

3. **Resultado**: Um arquivo `dados_mensais.csv` será criado com os dados processados.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Sinta-se livre para ajustar conforme necessário!
