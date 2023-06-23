# leitor_guias_fesp
 
Projeto para automatização da leitura de códigos de barra e valores das Guias emitidas pelo SDA (Sistema da Dívida Ativa), da Procuradoria Geral do Estado de São Paulo.

O script utiliza as seguintes bibliotecas:
  **PDFQUERY** para leitura do PDF e localização das coordenadas BBOX referentes ao código de barras e valor total a ser pago.
  **PANDAS** para criação dos DataFrames e exportação para Excel.
  **TKINTER** para seleção do arquivo para tratamento e posterior escolha do local de salvamento.

Após a seleção do arquivo PDF contendo as guias para pagamento, o script transforma o PDF em arquivo XML, permitindo, assim, a leitura e aplicação.
Uma vez transformado em XML, o arquivo é vasculhado, procurando pelas **COORDENADAS BBOX** correspondentes, que são inseridas em um data frame.
No caso de arquivos com várias páginas, um **FOR LOOP** vasculha tudo e, ao final, é gerado um último DATA FRAME e exportado para o excel.
