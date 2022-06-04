import requests

end_point = 'http://localhost:8000/api/v1/products/1'

response = requests.get(end_point)
print(response.json())

