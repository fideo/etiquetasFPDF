# Instalación
# 
# 1- Montar la variable de entorno env de virtualenv
#
# 2- Correr pip install -r requirements.txt

from calendar import c
from re import L
from fpdf import FPDF

class PDF(FPDF):
  pass # hace que no pase nada cuando se ejecuta

  def imagen_fondo(self, name, x, y, w, h):
    self.image(name, x, y, w, h)

  def texts(self, name):
    with open(name,'rb') as xy:
      txt=xy.read().decode('UTF-8')
    self.set_xy(10.0,30.0)
    self.set_text_color(0, 0, 0)
    self.set_font('Arial', 'B', 22)
    self.multi_cell(0, 10, txt, 0, "C")
  

pdf = PDF('P','mm',(100,80)) #objeto PDF
pdf.add_page()
pdf.imagen_fondo('fondo.png',0,0,100,80)
pdf.texts('data.txt')
pdf.set_author('Federico mazzei')
pdf.output('test.pdf', 'F')