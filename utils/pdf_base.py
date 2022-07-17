from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, titulo):
        super().__init__()
        self.titulo = titulo
        self.imagem = 'staticfiles/65709.png'

    def header(self):
        self.image(self.imagem, 10, 10, 12)
        self.set_font('courier', 'BIU', 16)
        self.set_text_color(220, 50, 50)
        self.cell(0, 15, self.titulo, border=False, ln=True, align='R')
        self.set_font('courier', 'IU', 15)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def footer(self):
        self.set_y(280)
        self.set_font('courier', 'I', 10)
        self.cell(0, 10, f'Página {self.page_no()}/{{nb}}', align='C')
