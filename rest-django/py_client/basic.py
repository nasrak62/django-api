import requests

end_point = 'http://localhost:8000/api/v1/'

response = requests.get(end_point, params={'abc': 123})
print(response.json())


body = {
    'title': 'hi',
    'content': 'hi content',
    'price': 1
}

response = requests.post(end_point, json = body)

print(response.json())