import json

def cargar_datos(archivo):
  with open(archivo) as contenido:
    productos = json.load(contenido) #esto devuelve un objeto
    for producto in productos:
      print(producto.get('producto'))

if __name__ == '__main__':
  ruta = 'data.json'
  cargar_datos(ruta)