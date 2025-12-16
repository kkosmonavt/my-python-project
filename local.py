import requests

res = requests.get('http://127.0.0.1:3000/api/main')
# res = requests.get('http://127.0.0.1:3000/api/courses/1')
res = requests.delete('http://127.0.0.1:3000/api/courses/1')

print(res.json())