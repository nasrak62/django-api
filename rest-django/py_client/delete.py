import requests

end_point = 'http://localhost:8000/api/v1/products/1/delete/'

response = requests.delete(end_point)
print(response.json())

