import mysql.connector
from mysql.connector import Error

vhost = '192.168.2.55'
vdatabase = 'formulario'
vuser = 'python'
vpassword = 'Python@321'


def inserir_usuario(user, password, email):
    try:
        # Estabelecendo a conexão com o banco de dados
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)

        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_insert_query = """ INSERT INTO cadastro (user, password, email)
                                   VALUES (%s, %s, %s)"""
            record = (user, password, email)
            cursor.execute(sql_insert_query, record)
            conexao.commit()
            print("Usuario cadastrado com sucesso \n")

    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerradan\n\n")

# Exemplo de uso da função

while True:
    print("Formulario de Cadastro")
    usuario=input('Insira o Usuario: ')
    senha=input('Insira a senha: ')
    email=input('Insira o email: ')
    print('===========Fim============= ')
    inserir_usuario(usuario, senha, email)
