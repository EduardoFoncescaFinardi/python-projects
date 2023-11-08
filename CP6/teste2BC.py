from flask import Flask, render_template, request, redirect, url_for, jsonify
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")

def getConnection():
    try:
        connection = cx_Oracle.connect("RM98624", "291002", "oracle.fiap.com.br/ORCL")
        #  connection = cx_Oracle.connect(user="RM98621", password="260104", host="oracle.fiap.com.br", port="1521", service="ORCL") """
        print("conexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')

def createTableEndereco():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_endereco = """
    CREATE TABLE t_cycleSurvey_endereco(
        CEP VARCHAR(9) NOT NULL,
        CIDADE VARCHAR(50) NOT NULL,
        LOGRADOURO VARCHAR(100) NOT NULL,
        NUM_LOGRADOURO VARCHAR(8) NOT NULL,
        ESTADO CHAR(2) NOT NULL,
        COMPLEMENTO VARCHAR(15),
        CONSTRAINT pk_t_cycleSurvey_endereco PRIMARY KEY (cep)
    )"""

    try:
        cursor.execute(sql_endereco)
        print("Tabela t_cycleSurvey_endereco criada")

    except Exception as e:
        print(f'Erro ao criar a tabela t_cycleSurvey_endereco: {e}')
    
    finally:
        cursor.close
        conn.close

def droptableEndereco():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_enderecodrop = """
    DROP TABLE t_cycleSurvey_endereco
"""
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela t_cycleSurvey_endereco dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela t_cycleSurvey_endereco: {e}')

    finally:
        cursor.close
        conn.close


createTableEndereco()
a = int(input("a:"))
if a == 1:
    droptableEndereco()
elif a != 1:
    print("cu")
    