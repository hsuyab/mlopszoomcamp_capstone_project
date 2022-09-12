import requests

diamond = {
    'Carat Weight': 1.10,
    'Cut': 'Ideal',
    'Color': 'H',
    'Polish': 'VG',
    'Symmetry': 'EX',
    'Report':'GIA'
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
print(response.json())