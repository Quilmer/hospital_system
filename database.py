import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="hospital_db",
        autocommit=True     # ⚠️ faz o autoteste para evitar esquecer de dar commit()
    )
    return connection

# print("Ficheiro executado!")  

if __name__ == "__main__":
    print("Entrou no teste!")  # linha de teste
    try:
        conn = get_connection()
        print("Ligação à base de dados OK!")
        conn.close()
    except Exception as e:
        print("Erro:", e)