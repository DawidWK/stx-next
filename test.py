import requests

r = requests.get("http://localhost:8000/api/books/")

print(r.json())
