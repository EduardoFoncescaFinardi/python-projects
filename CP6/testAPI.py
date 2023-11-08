import requests
from pprint import pprint



def ConsumoAPI_publica_endpoint_2():  
  
  print("""
As Routes possíveis são "/users" e "/posts".
A partir dessas routes você conseguirá acessar alguns dados!
        """)
  route = input("Route:")
  url = f'https://jsonplaceholder.typicode.com/{route}'
  
  response = requests.get(url)
  data = response.json()

  if response.status_code == 200:
    pprint(data)

  else:
      print("Route incorreta!")

ConsumoAPI_publica_endpoint_2()