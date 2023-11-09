import MySQLdb

def newVarejo(nome, numero):

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )
    
    cursor = connection.cursor()
    comando_sql = "INSERT INTO varejo (nome, numero) VALUES (%s, %s)"
    valores = (nome, numero)
    cursor.execute(comando_sql, valores)
    connection.commit()

    dados = listarVarejo()

    if len(dados) == 1:
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_varejo (id_varejo) VALUES (%s)"
            valores = (dados[0][0],)
            cursor.execute(comando_sql, valores)
            connection.commit()



    cursor.close()
    connection.close()

def deleteVarejo(nome):

    dados = listarVarejo()
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if len(dados) == 1:
        cursor = connection.cursor()
        comando_sql = "DELETE FROM varejo WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()
        sql = "DELETE FROM current_varejo"
        cursor.execute(sql)
        connection.commit()

    else:

        for i in range(len(dados)):
            if dados[i][1] == nome:
                id_encontrado = dados[i][0]
                if i == len(dados) - 1:
                    id_next = dados[0][0]
                else:
                    id_next = dados[i+1][0]

        cursor = connection.cursor()
        comando_sql = "DELETE FROM varejo WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()

        cursor = connection.cursor()
        consulta_sql = "SELECT id_varejo FROM current_varejo LIMIT 1"
        cursor.execute(consulta_sql)
        resultado = cursor.fetchone()

        if resultado[0] == id_encontrado:

            sql = "DELETE FROM current_varejo"
            cursor.execute(sql)
            connection.commit()
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_varejo (id_varejo) VALUES (%s)"
            valores = (id_next,)
            cursor.execute(comando_sql, valores)
            connection.commit()

    cursor.close()
    connection.close()

def newAtacado(nome, numero):

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )
    
    cursor = connection.cursor()
    comando_sql = "INSERT INTO atacado (nome, numero) VALUES (%s, %s)"
    valores = (nome, numero)
    cursor.execute(comando_sql, valores)
    connection.commit()
    cursor.close()
    connection.close()


    dados = listarAtacado()

    if len(dados) == 1:


            connection = MySQLdb.connect(
            host= "aws.connect.psdb.cloud",
            user="xv0oerf6bo5ct7fzs0ks",
            passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
            db= "chatbot",
            autocommit = True,
            ssl_mode = "VERIFY_IDENTITY"
            )
            cursor = connection.cursor()
            comando_sql = "INSERT INTO  current_atacado (id_atacado) VALUES (%s)"
            valores = (dados[0][0],)
            cursor.execute(comando_sql, valores)
            connection.commit()

            cursor.close()
            connection.close()

def deleteAtacado(nome):
    dados = listarAtacado()
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if len(dados) == 1:
        cursor = connection.cursor()
        comando_sql = "DELETE FROM atacado WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()
        sql = "DELETE FROM current_atacado"
        cursor.execute(sql)
        connection.commit()

    else:

        for i in range(len(dados)):
            if dados[i][1] == nome:
                id_encontrado = dados[i][0]
                if i == len(dados) - 1:
                    id_next = dados[0][0]
                else:
                    id_next = dados[i+1][0]

        cursor = connection.cursor()
        comando_sql = "DELETE FROM atacado WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()

        cursor = connection.cursor()
        consulta_sql = "SELECT id_atacado FROM current_atacado LIMIT 1"
        cursor.execute(consulta_sql)
        resultado = cursor.fetchone()

        if resultado[0] == id_encontrado:

            sql = "DELETE FROM current_atacado"
            cursor.execute(sql)
            connection.commit()
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_atacado (id_atacado) VALUES (%s)"
            valores = (id_next,)
            cursor.execute(comando_sql, valores)
            connection.commit()

    cursor.close()
    connection.close()

def newSetorDeCompras(nome, numero):
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )
    
    cursor = connection.cursor()
    comando_sql = "INSERT INTO setor_de_compras (nome, numero) VALUES (%s, %s)"
    valores = (nome, numero)
    cursor.execute(comando_sql, valores)
    connection.commit()
    cursor.close()
    connection.close()

    dados = listarSetorDeCompras()

    if len(dados) == 1:

        connection = MySQLdb.connect(
        host= "aws.connect.psdb.cloud",
        user="xv0oerf6bo5ct7fzs0ks",
        passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
        db= "chatbot",
        autocommit = True,
        ssl_mode = "VERIFY_IDENTITY"
        )
        cursor = connection.cursor()
        comando_sql = "INSERT INTO  current_setor_de_compras (id_setor_de_compras) VALUES (%s)"
        valores = (dados[0][0],)
        cursor.execute(comando_sql, valores)
        connection.commit()

        cursor.close()
        connection.close()

def deleteSetorDeCompras(nome):
    dados = listarSetorDeCompras()
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if len(dados) == 1:
        cursor = connection.cursor()
        comando_sql = "DELETE FROM setor_de_compras WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()
        sql = "DELETE FROM current_setor_de_compras"
        cursor.execute(sql)
        connection.commit()

    else:

        for i in range(len(dados)):
            if dados[i][1] == nome:
                id_encontrado = dados[i][0]
                if i == len(dados) - 1:
                    id_next = dados[0][0]
                else:
                    id_next = dados[i+1][0]

        cursor = connection.cursor()
        comando_sql = "DELETE FROM setor_de_compras WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()

        cursor = connection.cursor()
        consulta_sql = "SELECT id_setor_de_compras FROM current_setor_de_compras LIMIT 1"
        cursor.execute(consulta_sql)
        resultado = cursor.fetchone()

        if resultado[0] == id_encontrado:

            sql = "DELETE FROM current_setor_de_compras"
            cursor.execute(sql)
            connection.commit()
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_setor_de_compras (id_setor_de_compras) VALUES (%s)"
            valores = (id_next,)
            cursor.execute(comando_sql, valores)
            connection.commit()

    cursor.close()
    connection.close()

def newSac(nome, numero):
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )
    
    cursor = connection.cursor()
    comando_sql = "INSERT INTO sac (nome, numero) VALUES (%s, %s)"
    valores = (nome, numero)
    cursor.execute(comando_sql, valores)
    connection.commit()
    cursor.close()
    connection.close()

    dados = listarSac()

    if len(dados) == 1:
        connection = MySQLdb.connect(
        host= "aws.connect.psdb.cloud",
        user="xv0oerf6bo5ct7fzs0ks",
        passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
        db= "chatbot",
        autocommit = True,
        ssl_mode = "VERIFY_IDENTITY"
        )

        cursor = connection.cursor()

        comando_sql = "INSERT INTO  current_sac (id_sac) VALUES (%s)"
        valores = (dados[0][0],)
        cursor.execute(comando_sql, valores)
        connection.commit()
        cursor.close()
        connection.close()

def deleteSac(nome):
    dados = listarSac()
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if len(dados) == 1:
        cursor = connection.cursor()
        comando_sql = "DELETE FROM sac WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()
        sql = "DELETE FROM current_sac"
        cursor.execute(sql)
        connection.commit()

    else:

        for i in range(len(dados)):
            if dados[i][1] == nome:
                id_encontrado = dados[i][0]
                if i == len(dados) - 1:
                    id_next = dados[0][0]
                else:
                    id_next = dados[i+1][0]

        cursor = connection.cursor()
        comando_sql = "DELETE FROM sac WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()

        cursor = connection.cursor()
        consulta_sql = "SELECT id_sac FROM current_sac LIMIT 1"
        cursor.execute(consulta_sql)
        resultado = cursor.fetchone()

        if resultado[0] == id_encontrado:

            sql = "DELETE FROM current_sac"
            cursor.execute(sql)
            connection.commit()
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_sac (id_sac) VALUES (%s)"
            valores = (id_next,)
            cursor.execute(comando_sql, valores)
            connection.commit()

    cursor.close()
    connection.close()

def newGerente(nome, numero):
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )
    
    cursor = connection.cursor()
    comando_sql = "INSERT INTO gerente (nome, numero) VALUES (%s, %s)"
    valores = (nome, numero)
    cursor.execute(comando_sql, valores)
    connection.commit()

    dados = listarGerente()

    if len(dados) == 1:
        connection = MySQLdb.connect(
        host= "aws.connect.psdb.cloud",
        user="xv0oerf6bo5ct7fzs0ks",
        passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
        db= "chatbot",
        autocommit = True,
        ssl_mode = "VERIFY_IDENTITY"
        )

        cursor = connection.cursor()
        comando_sql = "INSERT INTO  current_gerente (id_gerente) VALUES (%s)"
        valores = (dados[0][0],)
        cursor.execute(comando_sql, valores)
        connection.commit()

    cursor.close()
    connection.close()

def deleteGerente(nome):
    dados = listarGerente()
    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if len(dados) == 1:
        cursor = connection.cursor()
        comando_sql = "DELETE FROM gerente WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()
        sql = "DELETE FROM current_gerente"
        cursor.execute(sql)
        connection.commit()

    else:

        for i in range(len(dados)):
            if dados[i][1] == nome:
                id_encontrado = dados[i][0]
                if i == len(dados) - 1:
                    id_next = dados[0][0]
                else:
                    id_next = dados[i+1][0]

        cursor = connection.cursor()
        comando_sql = "DELETE FROM gerente WHERE nome = %s"
        valor_para_excluir = nome
        cursor.execute(comando_sql, (valor_para_excluir,))
        connection.commit()

        cursor = connection.cursor()
        consulta_sql = "SELECT id_gerente FROM current_gerente LIMIT 1"
        cursor.execute(consulta_sql)
        resultado = cursor.fetchone()

        if resultado[0] == id_encontrado:

            sql = "DELETE FROM current_gerente"
            cursor.execute(sql)
            connection.commit()
            cursor = connection.cursor()

            comando_sql = "INSERT INTO  current_gerente (id_gerente) VALUES (%s)"
            valores = (id_next,)
            cursor.execute(comando_sql, valores)
            connection.commit()

    cursor.close()
    connection.close()

##############

def listarAtacado():

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os dados da tabela
    consulta = "SELECT * FROM atacado"
    cursor.execute(consulta)

    # Recupere todos os registros e armazene-os em uma lista
    dados = cursor.fetchall()

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    return dados

def listarGerente():

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os dados da tabela
    consulta = "SELECT * FROM gerente"
    cursor.execute(consulta)

    # Recupere todos os registros e armazene-os em uma lista
    dados = cursor.fetchall()

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    return dados

def listarVarejo():

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os dados da tabela
    consulta = "SELECT * FROM varejo"
    cursor.execute(consulta)

    # Recupere todos os registros e armazene-os em uma lista
    dados = cursor.fetchall()

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    return dados

def listarSetorDeCompras():

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os dados da tabela
    consulta = "SELECT * FROM setor_de_compras"
    cursor.execute(consulta)

    # Recupere todos os registros e armazene-os em uma lista
    dados = cursor.fetchall()

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    return dados

def listarSac():

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os dados da tabela
    consulta = "SELECT * FROM sac"
    cursor.execute(consulta)

    # Recupere todos os registros e armazene-os em uma lista
    dados = cursor.fetchall()

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    return dados

##############

def BuscarAtacadoNome(nome):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = nome

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM atacado WHERE nome = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarVarejoNome(nome):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = nome

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM varejo WHERE nome = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarSetorDeComprasNome(nome):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = nome

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM setor_de_compras WHERE nome = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarSacNome(nome):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = nome

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM sac WHERE nome = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarGerenteNome(nome):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = nome

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM gerente WHERE nome = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor


##############


def BuscarAtacadoTel(tel):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = tel

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM atacado WHERE numero = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarVarejoTel(tel):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = tel

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM varejo WHERE numero = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarSetorDeComprasTel(tel):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = tel

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM setor_de_compras WHERE numero = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarSacTel(tel):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = tel

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM sac WHERE numero = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor

def BuscarGerenteTel(tel):

    connection = MySQLdb.connect(   
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    # Crie um cursor
    cursor = connection.cursor()

    # Valor que você deseja verificar na coluna (substitua pelo valor desejado)
    valor_a_verificar = tel

    # Execute a consulta SQL para verificar a existência do valor na coluna
    consulta = f"SELECT COUNT(*) FROM gerente WHERE numero = %s"
    cursor.execute(consulta, (valor_a_verificar,))

    # Recupere o resultado da consulta como um valor booleano (True se o valor existe, False se não existe)
    existe_valor = cursor.fetchone()[0] > 0

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()

    # Imprima o resultado como um valor booleano
    return existe_valor


##############


def atual_destinatario(opcao):

    connection = MySQLdb.connect(
    host= "aws.connect.psdb.cloud",
    user="xv0oerf6bo5ct7fzs0ks",
    passwd= "pscale_pw_kCF7WSzLn49RGmKiyLFYPGQajxbbG8P12jiGfouSMvm",
    db= "chatbot",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY"
    )

    if opcao == 1:
        tabela = 'current_atacado'
        next = 'atacado'
        id = 'id_atacado'
    elif opcao == 2:
        tabela = 'current_varejo'
        next = 'varejo'
        id = 'id_varejo'
    elif opcao == 3:
        tabela = 'current_setor_de_compras'
        next = 'setor_de_compras'
        id = 'id_setor_de_compras'
    elif opcao == 4:
        tabela = 'current_gerencia'
        next = 'gerencia'
        id = 'id_gerencia'
    else:
        tabela = 'current_sac'
        next = 'sac'
        id = 'id_sac'
    cursor = connection.cursor()

    consulta = "SELECT * FROM " + tabela +";"
    cursor.execute(consulta)
    dados = cursor.fetchall() # lista de current

    current = dados[0][1] # id atual

    cursor = connection.cursor()
    consulta = f"SELECT * FROM {next}"
    cursor.execute(consulta)
    dados_next = cursor.fetchall() # lista com todos

    for i in range(len(dados_next)):
        if dados_next[i][0] == current:
            numero = dados_next[i][2]
            if i == len(dados_next) - 1:

                id_next = dados_next[0][0]
            else:
                id_next = dados_next[i+1][0]
    cursor = connection.cursor()
    sql = f"DELETE FROM {tabela}"
    cursor.execute(sql)
    connection.commit()


    cursor = connection.cursor()
    comando_sql = f"INSERT INTO {tabela} ({id}) VALUES (%s)"

    valores = (id_next,)
    cursor.execute(comando_sql, (valores))
    connection.commit()



    cursor.close()
    connection.close()

    

    return numero
