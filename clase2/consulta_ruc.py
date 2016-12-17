import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract


raiz = 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/'
sesion = requests.session()
sesion.get(raiz + 'jcrS00Alias')
pantalla_principal = sesion.get(raiz + 'frameCriterioBusqueda.jsp')

# Suprimir warning: usar el parser incluido
soup = BeautifulSoup(pantalla_principal.content, 'html.parser')

ruta_captcha = raiz + soup.find('img').attrs['src']
imagen = sesion.get(ruta_captcha)
with open('imagen.jpg', 'wb') as captcha:
    captcha.write(imagen.content)

# tessdata
captcha = pytesseract.image_to_string(Image.open('imagen.jpg'))

ruc = input('ingrese RUC: ')

formdata = {
        'accion': 'consPorRuc',
        'razSoc': '',
        'nroRuc': ruc,
        'nrodoc': '',
        'contexto': 'ti - it',
        'search1': ruc,
        'codigo': captcha,
        'tQuery': 'on',
        'tipdoc': '1',
        'search2': '',
        'coddpto': '',
        'codprov': '',
        'coddist': '',
        'search3': '',
    }

resultado = sesion.post(raiz + 'jcrS00Alias', data=formdata)
resultado = BeautifulSoup(resultado.content, 'html.parser')
resultado = [td.text.strip() for td in
             resultado.find('table', attrs={'cellpadding': 2}).find_all('td')]

for posicion, celda in enumerate(resultado):
    print(celda.strip(), '\n' if (posicion + 1) % 2 == 0 else '',)