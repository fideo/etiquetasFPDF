# Instalación
#
# 1- Montar la variable de entorno env de virtualenv
#
# 2- Correr pip install -r requirements.txt
# FIXMED: arreglar problema de acentos en Windows.

from fpdf import FPDF
from datetime import datetime

# Para mas información sobre FPDF ir a https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
class PDF(FPDF):
  pass # hace que no pase nada cuando se ejecuta

  # Defino la imagen de fondo para la etiqueta
  def imagen_fondo(self, name, x, y, w, h):
    self.image(name, x, y, w, h)

  # Función para setear el texto del producto a mostrar en la etiqueta
  def producto(self, txt):
    self.set_xy(10.0,30.0)
    self.set_text_color(0, 0, 0)
    self.set_font('Arial', 'B', 22)
    self.multi_cell(0, 10, txt, 0, "C")

  # Función para setear el texto de la cantidad a mostrar en la etiqueta
  def cantidad(self, txt):
    self.set_text_color(0, 0, 0)
    self.set_font('Arial', '',22)
    self.text(16, 73, txt)

# Defino la función que arma la etiqueta pasando lo variable necesarias para armarla
def armarPDF():
  now = datetime.now()
  pdf = PDF('P','mm',(100,80)) #objeto PDF
  ruta_archivo_productos = './assets/dataArgenchemical.txt'
  with open(ruta_archivo_productos, encoding='utf-8') as contenido:
    lineas = contenido.readlines()
    for linea in lineas:
      if linea != "\n":
        pdf.add_page()
        pdf.imagen_fondo('./assets/images/fondoArgenchemical.png',0,0,100,80)
        producto = (linea.split())
        pdf.producto(" ".join(producto[1:]).upper())
        if "POLVO" in str(producto[1:]).upper():
            pdf.cantidad(producto[0]+"K")
        else:
            pdf.cantidad(producto[0]+"L")
  pdf.set_title('Etiquetas para productos')
  pdf.set_subject('Este documento contiene las etiquetas generadas por Federico Mazzei')
  pdf.set_keywords('etiquetas')
  pdf.set_creator('Federico mazzei')
  pdf.set_author('Federico mazzei')
  pdf.output('etiquetas.pdf', 'F')
  # agrego un segundo archivo con la fecha y hora de cuando se ejecutó el script dentro del directorio pdfEjecutados
  pdf.output('./pdfEjecutados/etiquetas-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'-'+str(now.hour)+'hs'+str(now.minute)+'min' +
             str(now.second)+'seg'+'.pdf', 'F')

armarPDF()
