"""
query para pegar dados de um user:
select * from cadastro where user='flavio';

query para pegar user de um user:
select user from cadastro where user='flavio';

query para pegar senha de um user:
select password from cadastro where user='flavio';

"""
import mysql.connector
from mysql.connector import Error

vhost = '192.168.2.55'
vdatabase = 'formulario'
vuser = 'python'
vpassword = 'Python@321'

def verificar_user(var_user,var_senha):
    try:
        # Estabelecendo a conexão com o banco de dados
        conexao = mysql.connector.connect(host=vhost,database=vdatabase,user=vuser,password=vpassword)
        if conexao.is_connected():
            cursor = conexao.cursor()
            dados_query = f"select * from cadastro where user='{var_user}'" #defini a query
            cursor.execute(dados_query) #roda a query na maquina
            dados = cursor.fetchall() #pega o resultado e poe na variavel

            senha_query = f"select password from cadastro where user='{var_user}'"
            cursor.execute(senha_query)
            senha = cursor.fetchall()
            if senha:
                senha=senha[0][0]

            user_query = f"select user from cadastro where user='{var_user}'"
            cursor.execute(user_query)
            user = cursor.fetchall()
            if user:
                user=user[0][0]

            print(f"{dados}\n{user}\n{senha}")

            if senha == var_senha:
                return True
            else:
                return False


    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close()
            #print("Conexão ao MySQL encerrada")

user=input('user: ')
senha=input('Senha: ')
login=verificar_user(user,senha)

print(login)
if login == True:
    print('entrando no sistema: ')
else:
    print('dados invalidos!')