import sqlite3  
import os       

DBFILENAME = "comidasdb.sqlite"  # Nome do arquivo do banco de dados

def getconnection():
#Abre uma conexão com o banco de dados SQLite."""

# Estabelece comunicação com o arquivo do banco de dados
    conn = sqlite3.connect(DBFILENAME)
    conn.row_factory = sqlite3.Row
# Executa um comando PRAGMA no SQLite para garantir que as regras de chave estrangeira sejam sempre aplicadas.
# Isso é crucial para manter a integridade dos dados (ex: não permitir uma movimentação para uma comida que não existe).
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def ensuredb():
# Verifica se o arquivo do banco de dados já existe
    if not os.path.exists(DBFILENAME):
        scriptpath = os.path.join(os.path.dirname(__file__), "db_init.sql")
        if os.path.exists(scriptpath):
            with getconnection() as conn:
                with open(scriptpath, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())

        else:
# Gera erro caso o arquivo db_init.sql não esteja disponível
            raise FileNotFoundError("db_init.sql não encontrado. Coloque db_init.sql na mesma pasta.")