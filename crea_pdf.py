# Instalación
# 
# 1- Montar la variable de entorno env de virtualenv
#
# 2- Correr pip install -r requirements.txt

from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
  pass # hace que no pase nada cuando se ejecuta

  def imagen_fondo(self, name, x, y, w, h):
    self.image(name, x, y, w, h)

  def texts(self, txt):    
    self.set_xy(10.0,30.0)
    self.set_text_color(0, 0, 0)
    self.set_font('Arial', 'B', 22)
    self.multi_cell(0, 10, txt, 0, "C")
  

def armarPDF():
  now = datetime.now()
  pdf = PDF('P','mm',(100,80)) #objeto PDF
  ruta_archivo_productos = ruta_archivo_productos = './data.txt'
  fichero = open(ruta_archivo_productos)
  lineas = fichero.readlines()
  for linea in lineas:
    if linea != "\n":
      pdf.add_page()
      pdf.imagen_fondo('fondo.png',0,0,100,80)
      pdf.texts(linea.strip())
  fichero.close()
  pdf.set_title('Etiquetas para productos')
  pdf.set_subject('Este documento contiene las etiquetas generadas por Federico Mazzei')
  pdf.set_keywords('etiquetas')
  pdf.set_creator('Federico mazzei')
  pdf.set_author('Federico mazzei')
  pdf.output('etiquetas.pdf', 'F')
  pdf.output('./pdfEjecutados/etiquetas-'+str(now)+'.pdf', 'F')

armarPDF()

