import requests

end_point = 'http://localhost:8000/api/v1/products/'

response = requests.get(end_point)
print(response.json())

