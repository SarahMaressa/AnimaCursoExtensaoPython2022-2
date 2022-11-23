# Importar a biblioteca sqlite3
import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# Criar um objeto do tipo cursor
cursor = conexao.cursor()

# Comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'Flash', 'Barry Allen', 'Herói(na)')"

# Executar o comando SQL
cursor.execute(sql)

# Confirmar o INSERT com Commit e fechar o banco
conexao.commit()
conexao.close()
