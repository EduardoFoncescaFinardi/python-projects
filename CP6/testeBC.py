'''
1. Oracle DB
2. Python lib (bibilioteca Python)
3. DB details
4. Driver - cx_oracle/ oracledb

PEP 249 - Python Database API Specification v2

Módulos
cx_Oracle | oracledb - Oracle Database
pyodbc - Microsoft SQL Server
pymysql - MySQL
psycopg2 - PostgreSQL

Passos:
1. Estabelecer uma conexão entre Python com Banco de dados:
    connection = cx_Oracle.connect(database connection String)

2. obter um Cursor (objeto para executar queries e obter resultados após a execução):
cursor = connection.cursor()

'''
from flask import Flask, render_template, request, redirect, url_for, jsonify
import cx_Oracle

	#create connection
conn = cx_Oracle.connect(
	    user= "RM98624",
	    password= "291002",
	    host= "oracle.fiap.com.br",
	    port= "1521",
	    service_name= "ORCL")
print(conn.version)
	
	#create cursor
cursor = conn.cursor()

#create table
sql_create = """
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER (3)
)
"""
#execute query
cursor.execute(sql_create )
print("Tabela Criada")
'''
1. Oracle DB
2. Python lib (bibilioteca Python)
3. DB details
4. Driver - cx_oracle/ oracledb

PEP 249 - Python Database API Specification v2

Módulos
cx_Oracle | oracledb - Oracle Database
pyodbc - Microsoft SQL Server
pymysql - MySQL
psycopg2 - PostgreSQL

Passos:
1. Estabelecer uma conexão entre Python com Banco de dados:
    connection = cx_Oracle.connect(database connection String)

2. obter um Cursor (objeto para executar queries e obter resultados após a execução):
cursor = connection.cursor()

'''

#create connection
conn = cx_Oracle.connect(
    user= "RM98207",
    password= "190804",
    host= "oracle.fiap.com.br",
    port= "1521",
    service_name= "ORCL")
print(conn.version)

#create cursor
cursor = conn.cursor()

#create table
sql_create = """
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER (3)
)
"""
#execute query
cursor.execute(sql_create )
print("Tabela Criada")

#select
select_data = "select * from CEO_DETAILS"
cursor.execute(select_data)

'''
ResultSet rs = new ResultSet()...
while(rs.next()){
}
'''
for result in cursor:
    print(result) #result[2]

conn.close()#fechando a conexão
cursor.close()#fechando o cursor