#Importações
import pandas as pd
import pdfquery
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Interface gráfica
janela_padrao = Tk().withdraw()
arquivo = askopenfilename(filetypes=(('Arquivos PDF', '*.pdf'),))

#Lendo o PDF
pdf = pdfquery.PDFQuery(arquivo)
pdf.load()

#transformando o PDF em arquivo estrutura XML
pdf.tree.write('pdfXML.txt', pretty_print = True)

#localizando código de barras e valor segundo as coordenadas BBOX
def raspa_pdf(pdf):
    barcode = pdf.pq('LTTextLineHorizontal:in_bbox("127.56, 430.55, 424.44, 440.55")').text()
    vlr_total = pdf.pq('LTTextLineHorizontal:overlaps_bbox("384.93, 310.844, 416.066, 318.844")').text()
    barcode2 = pdf.pq('LTTextLineHorizontal:in_bbox("24.693, 258.711, 323.536, 266.71")').text()
    vlr_total2 = pdf.pq('LTTextLineHorizontal:overlaps_bbox("515.229, 132.675, 570.592, 144.674")').text()

    #Combinando as informacoes em um Data Frame utilizando PANDAS
    page = pd.DataFrame({
        'cod_barras principal':barcode, 
        'valor principal': vlr_total,
        'cod_barras custas': barcode2,
        'valor custas': vlr_total2,
    }, index=[0])

    return(page)

#Contando a quantidade de páginas para o laço FOR
page_count = pdf.doc.catalog['Pages'].resolve()['Count']

excel = pd.DataFrame() #novo DataFrame que terá informação de todos os códigos de barra e valores
for p in range(page_count):
    pdf.load(p)
    page = raspa_pdf(pdf)
    excel = excel.append(page, ignore_index=True)

#Caixa de diálogo que permite escolher o nome e local do arquivo para salvamento
arquivo = asksaveasfilename(defaultextension='.xlsx')
excel.to_excel(arquivo, index=False) #exportação para excel