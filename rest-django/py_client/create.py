import requests

end_point = 'http://localhost:8000/api/v1/products/'

data = {
    'title': 'create post',
    'content': 'create post content',
    'price': 12.12
}

response = requests.post(end_point, json=data)
print(response.json())

