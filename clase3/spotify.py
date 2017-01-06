import requests

tofind = input('ToFind: ')
resultado = requests.get('https://api.spotify.com/v1/search',
                         params={'q': tofind, 'type': 'track'})

start = resultado.json()

data = start['tracks']['items']

for track in data:
    print(track['name'])
