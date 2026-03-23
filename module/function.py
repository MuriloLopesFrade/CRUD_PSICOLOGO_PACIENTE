from bando_de_dados.DataBase import conector

def create_paciente(primeiro_nome,ultimo_nome,email,senha):
    conexao = conector()
    cursor = conexao.cursor()

    sql = f'INSERT INTO paciente (primeiro_nome, ultimo_nome, email, senha) VALUES (%s,%s,%s,%s)'
    values = (primeiro_nome, ultimo_nome,email,senha)

    cursor.execute(sql,values)
    conexao.commit()# usamos esse comando quando editamos o banco de dados

    print('')
    print('Paciente cadastrdo com sucesso')

    cursor.close()
    conexao.close()

def create_psicologo(primeiro_nome,ultimo_nome,email,senha):
    conexao = conector()
    cursor = conexao.cursor()

    sql = "INSERT INTO psicologo (primeiro_nome, ultimo_nome, email, senha) VALUES (%s,%s,%s,%s)"
    values = (primeiro_nome, ultimo_nome, email, senha)

    cursor.execute(sql,values)
    conexao.commit()# usamos esse comando quando editamos o banco de dados

    print('')
    print('Psicologo cadastrdo com sucesso')

    cursor.close()
    conexao.close()

def listagem(tabela):
    conexao = conector()
    cursor = conexao.cursor()

    sql = f'SELECT * FROM {tabela}'

    cursor.execute(sql)
    resultado = cursor.fetchall() # Usando esse comando para ler o banco de dados (pegando o resultado doque foi executado no comando acima)

    print(' ')
    print(f'Listagem de {tabela}')
    for i, paciente in enumerate(resultado):
        print(f'{i+1}- {paciente[1]} {paciente[2]}')
    print(' ')

    cursor.close()
    conexao.close()

def atualizacao(tabela,id, primeiro_nome,ultimo_nome,email,senha):
    conexao = conector()
    cursor = conexao.cursor()

    sql = f'UPDATE {tabela} set primeiro_nome=%s,ultimo_nome=%s,email=%s,senha=%s WHERE id=%s'
    values = (primeiro_nome,ultimo_nome,email,senha,id)
    cursor.execute(sql,values)
    conexao.commit() # usamos esse comando quando editamos o banco de dados

    print('')
    print('Autualização realizada com sucesso!')

    cursor.close()
    conexao.close()

def exclucao(tabela,id):
    conexao = conector()
    cursor = conexao.cursor()

    sql = f'DELETE FROM {tabela} WHERE id = %s'
    values = (id,)

    print('')
    print('Exclusão realizada com sucesso!')

    cursor.execute(sql,values)
    conexao.commit() # usamos esse comando quando editamos o banco de dados

    cursor.close()
    conexao.close()