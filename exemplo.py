import mysql.connector
from mysql.connector import Error

# Define uma função para inserir um usuário no banco de dados
def inserir_usuario(user, password, email):
    try:
        # Tenta estabelecer a conexão com o banco de dados MySQL
        conexao = mysql.connector.connect(
            host='localhost',  # Endereço do servidor MySQL
            database='nome_do_banco_de_dados',  # Nome do banco de dados
            user='seu_usuario',  # Usuário MySQL
            password='sua_senha'  # Senha do usuário MySQL
        )

        # Verifica se a conexão foi bem-sucedida
        if conexao.is_connected():
            # Cria um cursor para executar comandos SQL
            cursor = conexao.cursor()
            # SQL query para inserir um novo registro na tabela 'usuário'
            sql_insert_query = """ INSERT INTO usuário (user, password, email)
                                   VALUES (%s, %s, %s)"""
            # Valores a serem inseridos no SQL query
            record = (user, password, email)
            # Executa o comando SQL com os valores fornecidos
            cursor.execute(sql_insert_query, record)
            # Confirma a transação para salvar as alterações no banco de dados
            conexao.commit()
            # Imprime mensagem de sucesso
            print("Registro inserido com sucesso na tabela usuário")

    # Captura e imprime qualquer erro que ocorrer durante a conexão ou execução do SQL
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    # Bloco de finalização que será executado independentemente de ocorrer um erro ou não
    finally:
        # Verifica se a conexão ainda está ativa
        if (conexao.is_connected()):
            # Fecha o cursor
            cursor.close()
            # Fecha a conexão com o banco de dados
            conexao.close()
            # Imprime mensagem indicando que a conexão foi encerrada
            print("Conexão ao MySQL encerrada")

# Exemplo de uso da função: insere um novo usuário com nome de usuário, senha e email fornecidos
inserir_usuario('usuario_teste', 'senha123', 'teste@exemplo.com')
