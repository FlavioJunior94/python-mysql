import mysql.connector
from mysql.connector import Error

vhost = '192.168.2.55'
vdatabase = 'livro'
vuser = 'python'
vpassword = 'Python@321'

def pagina_banco(x):
    try:
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_select_query = "UPDATE got SET pagina_lida = %s WHERE livro_lido = 'dragao';"
            dado=(x,)
            cursor.execute(sql_select_query,dado)
            conexao.commit()
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()

def pagina_atual():
    try:
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_select_query = "SELECT pagina_lida FROM got where livro_lido = 'dragao'"
            cursor.execute(sql_select_query)
            total= cursor.fetchone()

            return  total[0]


    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()




print(pagina_atual())

xx=(100*pagina_atual())/987
print(f"{xx}% lido")
x=int(input('quantas paginas foram lidas ?  '))
pagina_banco(x)


"""
create database livro;
use livro;
create table got(

livro_lido varchar(100),
pagina_lida int(100)

);


insert into variaveis values('dragao',10);

UPDATE got SET valor = %s WHERE livro_lido = 'dragao';






"""