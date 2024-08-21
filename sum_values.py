import mysql.connector
from mysql.connector import Error

vhost = '192.168.2.55'
vdatabase = 'soma'
vuser = 'python'
vpassword = 'Python@321'

def numeros_banco():
    try:
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_select_query = "SELECT x,y FROM variaveis"
            cursor.execute(sql_select_query)
            numeros= cursor.fetchall()

            for row in numeros:
                numero1=row[0]
                numero2=row[1]

                return numero1,numero2



    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada")

n1,n2=numeros_banco()[0]
n2=numeros_banco()[1]
print(n1+n2)

"""
create database soma;
use soma;
create table variaveis(

chave char(2),
valor int (10)

);

insert into variaveis values('1',10);
insert into variaveis values('2',5);

UPDATE got SET valor = 12 WHERE chave = 1;


"""