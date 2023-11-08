import requests

r = requests.get("https://python.org")
print(r.status_code)

print(r)
print(b'Python is a programming language' in r.content)