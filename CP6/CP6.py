import requests
from pprint import pprint

from flask import Flask, render_template, request, redirect, url_for, jsonify
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")

def ConsumoAPI_publica_endpoint_1():
  print('GitHub users')
  username= input('Username: ')
  url = f'https://api.github.com/users/{username}'

  response = requests.get(url)
  data = response.json()

  if response.status_code == 200:
      print(f'id: {data["id"]}')
      print(f'Nome Completo: {data["name"]}')
      print(f'Bio: {data["bio"]}')
      print(f'Localização: {data["location"]}')
  
  else:
      print('Usuário não encontrado!')

def ConsumoAPI_publica_endpoint_2():  
  print("""
As Routes possíveis são "/users" e "/posts".
A partir dessas routes você conseguirá acessar alguns dados!
        """)
  route = input("Route:")
  url = f'https://jsonplaceholder.typicode.com/{route}'
  
  response = requests.get(url)
  data = response.json()

  if response.status_code == 200 and route == "/users":
    print("-------------------------")
    for item in data:
      print(f"id: {item['id']}, Nome: {item['name']}, Cidade: {item['address']['city']}")

  elif response.status_code == 200 and route == "/posts":
    print("-------------------------")
    for item in data:
       print(f'id: {item["id"]}, title: {item["title"]}')
  else:
      print("Route incorreta!")
  
  return route

def getConnection():
    try:
        connection = cx_Oracle.connect("RM98624", "291002", "oracle.fiap.com.br/ORCL")
        # connection = cx_Oracle.connect(user="a", password="b", host="c", port="1521", service="ORCL") 
        print("conexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')

def CREATE_TABLE_DADOS_GITHUB():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_GitHub = """
    CREATE TABLE DADOS_GITHUB(
      ID_GITHUB INT NOT NULL,
      NOME_COMPLETO VARCHAR (60) NOT NULL,
      BIOGRAFIA VARCHAR(1000),
      LOCALIZACAO VARCHAR(100),
      CONSTRAINT pk_ID_GITHUB PRIMARY KEY (ID_GITHUB)
    )"""

    try:
        cursor.execute(sql_GitHub)
        print("Tabela DADOS_GITHUB criada")

    except Exception as e:
        print(f'Erro ao criar a tabela DADOS_GITHUB: {e}')
    
    finally:
        cursor.close
        conn.close

def DROP_TABLE_DADOS_GITHUB():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_enderecodrop = """
    DROP TABLE DADOS_GITHUB
"""
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela DADOS_GITHUB dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela DADOS_GITHUB: {e}')

    finally:
        cursor.close
        conn.close

def CREATE_TABLE_DADOS_JSONPLACEHOLDER_USERS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_JSONPLACEHOLDER = """
    CREATE TABLE DADOS_JSONPLACEHOLDER_USERS(
      ID_JSONPLACEHOLDER_USERS INT NOT NULL,
      COMPLETE_NAME VARCHAR (60) NOT NULL,
      CIDADE VARCHAR(60),
      CONSTRAINT pk_ID_JSONPLACEHOLDER_USERS PRIMARY KEY (ID_JSONPLACEHOLDER_USERS)
    )"""

    try:
        cursor.execute(sql_JSONPLACEHOLDER)
        print("Tabela DADOS_JSONPLACEHOLDER_USERS criada")

    except Exception as e:
        print(f'Erro ao criar a tabela DADOS_JSONPLACEHOLDER_USERS: {e}')
    
    finally:
        cursor.close
        conn.close

def DROP_TABLE_DADOS_JSONPLACEHOLDER_USERS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_DADOS_JSONPLACEHOLDER_USERS_DROP = """
    DROP TABLE DADOS_JSONPLACEHOLDER_USERS
"""
    try:
        cursor.execute(sql_DADOS_JSONPLACEHOLDER_USERS_DROP)
        print("Tabela DADOS_JSONPLACEHOLDER_USERS dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela DADOS_JSONPLACEHOLDER_USERS_USERS: {e}')

    finally:
        cursor.close
        conn.close

def CREATE_TABLE_DADOS_JSONPLACEHOLDER_POSTS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_JSONPLACEHOLDER = """
    CREATE TABLE DADOS_JSONPLACEHOLDER_POSTS(
      ID_JSONPLACEHOLDER_POSTS INT NOT NULL,
      TITLE VARCHAR (600) NOT NULL,
      CONSTRAINT pk_ID_JSONPLACEHOLDER_POSTS PRIMARY KEY (ID_JSONPLACEHOLDER_POSTS)
    )"""

    try:
      cursor.execute(sql_JSONPLACEHOLDER)
      print("Tabela DADOS_JSONPLACEHOLDER_POSTS criada")

    except Exception as e:
      print(f'Erro ao criar a tabela DADOS_JSONPLACEHOLDER_POSTS: {e}')
    
    finally:
      cursor.close
      conn.close

def DROP_TABLE_DADOS_JSONPLACEHOLDER_POSTS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_DADOS_JSONPALCEHOLDER_POSTS_DROP = """
    DROP TABLE DADOS_JSONPLACEHOLDER_POSTS
"""
    try:
        cursor.execute(sql_DADOS_JSONPALCEHOLDER_POSTS_DROP)
        print("Tabela DADOS_JSONPLACEHOLDER_POSTS dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela DADOS_JSONPLACEHOLDER_POSTS: {e}')

    finally:
        cursor.close
        conn.close

def INSERT_DADOS_GITHUB_PASSO_1():
  lista_de_dados_GitHub = []
  print("gostaria de inserir algum dos valores provenientes da API dentro da tabela?")
  question_1 = int(input("Se sim, digite 1:"))
  if question_1 == 1:
    id = input("id:")
    lista_de_dados_GitHub.append(id)

    Nome_completo = input("Nome completo:")
    lista_de_dados_GitHub.append(Nome_completo)

    Biografia = input("Biografia:")
    lista_de_dados_GitHub.append(Biografia)

    Localizacao = input("Localização:")
    lista_de_dados_GitHub.append(Localizacao)

  return lista_de_dados_GitHub

def INSERT_DADOS_GITHUB_PASSO_2(lista_de_dados_GitHub):
  conn = getConnection()
  cursor = conn.cursor()
  sql_query = "INSERT INTO DADOS_GITHUB (ID_GITHUB, NOME_COMPLETO, BIOGRAFIA, LOCALIZACAO) VALUES (:0, :1, :2, :3)"
  try:
      cursor.execute(sql_query, (lista_de_dados_GitHub[0], lista_de_dados_GitHub[1], lista_de_dados_GitHub[2], lista_de_dados_GitHub[3]))
      conn.commit()
      print("Registro de cliente inserido com sucesso.")
  except Exception as e:
      print(f'Erro ao inserir o registro de cliente: {e}')
  finally:
      cursor.close()
      conn.close()

def INSERIR_DADOS_JSONPLACEHOLDER_USERS_PASSO_1():
  lista_de_dados_JSONPLACEHOLDER_USERS = []
  print("gostaria de inserir algum dos valores provenientes da API dentro da tabela?")
  question_1 = int(input("Se sim, digite 1:"))
  if question_1 == 1:
    id = input("id:")
    lista_de_dados_JSONPLACEHOLDER_USERS.append(id)

    Nome_completo = input("Nome completo:")
    lista_de_dados_JSONPLACEHOLDER_USERS.append(Nome_completo)

    Localizacao = input("Cidade:")
    lista_de_dados_JSONPLACEHOLDER_USERS.append(Localizacao)

  return lista_de_dados_JSONPLACEHOLDER_USERS

def INSERIR_DADOS_JSONPLACEHOLDER_USERS_PASSO_2(lista_de_dados_JSONPLACEHOLDER_USERS):
  conn = getConnection()
  cursor = conn.cursor()
  sql_query = "INSERT INTO DADOS_JSONPLACEHOLDER_USERS (ID_JSONPLACEHOLDER_USERS, COMPLETE_NAME, CIDADE) VALUES (:0, :1, :2)"
  try:
      cursor.execute(sql_query, (lista_de_dados_JSONPLACEHOLDER_USERS[0], lista_de_dados_JSONPLACEHOLDER_USERS[1], lista_de_dados_JSONPLACEHOLDER_USERS[2]))
      conn.commit()
      print("Registro de cliente inserido com sucesso.")
  except Exception as e:
      print(f'Erro ao inserir o registro de cliente: {e}')
  finally:
      cursor.close()
      conn.close()

def INSERIR_DADOS_JSONPLACEHOLDER_POSTS_PASSO_1():
  lista_de_dados_JSONPLACEHOLDER_POSTS = []
  print("gostaria de inserir algum dos valores provenientes da API dentro da tabela?")
  question_1 = int(input("Se sim, digite 1:"))
  if question_1 == 1:
    id = input("id:")
    lista_de_dados_JSONPLACEHOLDER_POSTS.append(id)

    Nome_completo = input("Title:")
    lista_de_dados_JSONPLACEHOLDER_POSTS.append(Nome_completo)

  return lista_de_dados_JSONPLACEHOLDER_POSTS 

def INSERIR_DADOS_JSONPLACEHOLDER_POSTS_PASSO_2(lista_de_dados_JSONPLACEHOLDER_POSTS):
  conn = getConnection()
  cursor = conn.cursor()
  sql_query = "INSERT INTO DADOS_JSONPLACEHOLDER_POSTS (ID_JSONPLACEHOLDER_POSTS, TITLE) VALUES (:0, :1)"
  try:
      cursor.execute(sql_query, (lista_de_dados_JSONPLACEHOLDER_POSTS[0], lista_de_dados_JSONPLACEHOLDER_POSTS[1]))
      conn.commit()
      print("Registro de cliente inserido com sucesso.")
  except Exception as e:
      print(f'Erro ao inserir o registro de cliente: {e}')
  finally:
      cursor.close()
      conn.close()

def main():
  print("Escolher funcionalidade do menu")
  selecionar_menu = int(input("""
1 - Consultar dados de usuário do GitHub.
2 - Consultar dados de users e posts do JSONplaceholder.                   
Selecione:"""))
  
  match selecionar_menu:
    case 1:   
      ConsumoAPI_publica_endpoint_1()
      CREATE_TABLE_DADOS_GITHUB()
      lista_de_dados_GitHub = INSERT_DADOS_GITHUB_PASSO_1()
      INSERT_DADOS_GITHUB_PASSO_2(lista_de_dados_GitHub)
      print("Desejar dropar a tabela? Se sim, digite 1")
      drop_table = int(input("Resposta:"))
      if drop_table == 1:
        DROP_TABLE_DADOS_GITHUB()
      elif drop_table != 1:
        print("fim!")
    
    case 2:
      route = ConsumoAPI_publica_endpoint_2()
      if route  == "/users":
        CREATE_TABLE_DADOS_JSONPLACEHOLDER_USERS()
        lista_de_dados_JSONPLACEHOLDER_USERS = INSERIR_DADOS_JSONPLACEHOLDER_USERS_PASSO_1()
        INSERIR_DADOS_JSONPLACEHOLDER_USERS_PASSO_2(lista_de_dados_JSONPLACEHOLDER_USERS)
        print("Desejar dropar a tabela? Se sim, digite 1!")
        drop_table = int(input("Resposta:"))
        
        if drop_table == 1:
          DROP_TABLE_DADOS_JSONPLACEHOLDER_USERS()
        
        elif drop_table != 1:
          print("fim!")
      
      elif route == "/posts": 
        CREATE_TABLE_DADOS_JSONPLACEHOLDER_POSTS()
        lista_de_dados_JSONPLACEHOLDER_POSTS = INSERIR_DADOS_JSONPLACEHOLDER_POSTS_PASSO_1()
        INSERIR_DADOS_JSONPLACEHOLDER_POSTS_PASSO_2(lista_de_dados_JSONPLACEHOLDER_POSTS)
        print("Desejar dropar a tabela? Se sim, digite 1!")
        drop_table = int(input("Resposta:"))
        
        if drop_table == 1:
          DROP_TABLE_DADOS_JSONPLACEHOLDER_POSTS()
        
        elif drop_table != 1:
          print("fim!")

main()