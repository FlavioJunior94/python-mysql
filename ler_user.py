import mysql.connector
from mysql.connector import Error

vhost = '192.168.2.55'
vdatabase = 'formulario'
vuser = 'python'
vpassword = 'Python@321'

def ler_usuarios():
    try:
        # Estabelecendo a conexão com o banco de dados
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_select_query = "SELECT user, password, email FROM cadastro" #defini a query
            cursor.execute(sql_select_query) #roda a query na maquina
            registros = cursor.fetchall() #pega o resultado e poe na variavel
            print("Total de registros lidos: ", cursor.rowcount)

            print("\nImprimindo cada usuário:")
            for row in registros:
                print("User: ", row[0])
                print("Password: ", row[1])
                print("Email: ", row[2])
                print("\n")

    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada")
def ler_usuario_por_id(iduser):
    try:
        # Estabelecendo a conexão com o banco de dados
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            sql_select_query = "SELECT user, password, email FROM cadastro WHERE iduser = %s"
            cursor.execute(sql_select_query, (iduser,))
            registro = cursor.fetchone()

            if registro:
                print("\n\n Detalhes do usuário:\n")
                print("User: ", registro[0])
                print("Password: ", registro[1])
                print("Email: ", registro[2])
                print('\n---------fim--------------')
            else:
                print("Usuário não encontrado para o id usuario:", iduser)

    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada")

while True:
    opt=int(input('Ler todos ? 1-sim 2-nao'))
    if opt==1:
        ler_usuarios()
    else:
        pass
    print('='*60)

    x=int(input('id: '))
    ler_usuario_por_id(x)
    print('=' * 60)