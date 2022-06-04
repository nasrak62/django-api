import requests

end_point = 'http://localhost:8000/api/v1/products/1/update/'

data = {
    'title': 'updated title',
    'content': 'updated content'
}

response = requests.put(end_point, json=data)
print(response.json())

