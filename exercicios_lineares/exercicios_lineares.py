from utils.pdf_base import PDF
from utils.gerador_numeros import gerando_numeros
from datetime import datetime

titulo = 'GCM - Gerador de Calcúlos Matematicos'
LINE_LENGTH = 8
COLUMN_LENGTH = 100
MAX_LINE_LENGTH = 260


class LinearExercises:
    def __init__(self, operador, gerador, intervalo1, intervalo2, ordem='n'):
        pdf = PDF(titulo=titulo)
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('courier', '', 14)
        self.operador = operador
        self.gerador = gerador
        self.pdf = pdf
        self.linha = 27
        self.linha2 = 35
        self.coluna = 10
        self.tamanho_altura = 8
        self.tamanho_largura = 80
        self.x1 = 60
        self.x = 1
        self.fator1 = None
        self.fator2 = None
        self.ordem = ordem
        self.intervalo1 = intervalo1
        self.intervalo2 = intervalo2

    def questions(self):
        if self.ordem == 'n':
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador(intervalo1=self.intervalo1, intervalo2=self.intervalo2)
                if self.linha < MAX_LINE_LENGTH and self.coluna == 10:
                    self.linha = self.write_question(fator1=self.fator1,
                                                     fator2=self.fator2,
                                                     linha=self.linha,
                                                     coluna=self.coluna)
                else:
                    self.coluna = COLUMN_LENGTH
                    self.linha2 = self.write_question(fator1=self.fator1,
                                                      fator2=self.fator2,
                                                      linha=self.linha2,
                                                      coluna=self.coluna)
                self.x += 1
        else:
            while self.x <= self.x1:
                self.fator1, self.fator2 = self.gerador(intervalo1=self.intervalo1, intervalo2=self.intervalo2)
                if self.fator1 > self.fator2:
                    if self.linha < MAX_LINE_LENGTH and self.coluna == 10:
                        self.linha = self.write_question(fator1=self.fator1,
                                                         fator2=self.fator2,
                                                         linha=self.linha,
                                                         coluna=self.coluna)
                    else:
                        self.coluna = COLUMN_LENGTH
                        self.linha2 = self.write_question(fator1=self.fator1,
                                                          fator2=self.fator2,
                                                          linha=self.linha2,
                                                          coluna=self.coluna)
                else:
                    if self.linha < MAX_LINE_LENGTH and self.coluna == 10:
                        self.linha = self.write_question(fator1=self.fator2,
                                                         fator2=self.fator1,
                                                         linha=self.linha,
                                                         coluna=self.coluna)
                    else:
                        self.coluna = COLUMN_LENGTH
                        self.linha2 = self.write_question(fator1=self.fator2,
                                                          fator2=self.fator1,
                                                          linha=self.linha2,
                                                          coluna=self.coluna)
                self.x += 1
        date = datetime.now()
        date_format = date.strftime("%m_%d_%Y_%H_%M_%S")
        self.pdf.output(f'files_pdf/exercicios_{date_format}.pdf')
        file_path = f'files_pdf/exercicios_{date_format}.pdf'
        return file_path

    def write_question(self, fator1, fator2, linha, coluna):
        self.pdf.multi_cell(self.tamanho_largura, self.tamanho_altura,
                            f'{self.x}) {fator1} {self.operador} {fator2} =', border=True)
        self.pdf.set_xy(coluna, linha + LINE_LENGTH)
        linha += LINE_LENGTH
        return linha


if __name__ == '__main__':
    print('Gerador de Calculos Matematicos')
    print('Você precisa escolher o intervalo que deseja utilizar para montar os calculos!')
    intervalo1 = int(input('Digite o primeiro numero do intervalo: '))
    intervalo2 = int(input('Digite o ultimo numero do intervalo: '))
    ordem = input('Deseja organizar com o maior fator primeiro? [s]im ou [n]ão: ')
    operador = input('Digite o Operador:(Divisão = ÷ / Multiplicação = x / Soma = + / Subtração = - ) ')
    exercises = LinearExercises(operador=operador,
                                gerador=gerando_numeros,
                                ordem=ordem,
                                intervalo1=intervalo1,
                                intervalo2=intervalo2).questions()
