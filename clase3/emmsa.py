import requests
import bs4

data = {
    'vid_tipo': 1,
    'vprod': '',
    'vvari': '',
    'vfecha': '15/12/2016'
}

url = 'http://www.emmsa.com.pe/emmsa_spv/app/reportes/ajax/rpt07_gettable.php'
tabla = requests.post(url, data=data)
soup = bs4.BeautifulSoup(tabla.content, 'html.parser')

for fila in soup.find('tbody').find_all('tr'):
    producto, variedad, p_min, p_max, p_promedio = fila.find_all('td')
    print('Producto:', producto.text)
    print('Variedad:', variedad.text)
    print('Precio minimo:', p_min.text)
    print('Precio maximo:', p_max.text)
    print('Precio promedio:', p_promedio.text)
    print('---')
