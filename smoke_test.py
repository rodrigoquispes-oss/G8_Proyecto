import psycopg2

def run_smoke_test():
    try:
        # Credenciales según tu Vista Física [cite: 212, 214]
        conn = psycopg2.connect(
            host="localhost",
            database="postgres", 
            user="postgres",
            password="postgres" 
        )
        print("✅ Smoke Test: Conexión a PostgreSQL EXITOSA")
        conn.close()
    except Exception as e:
        print(f"❌ Smoke Test: Error de conexión -> {e}")

if __name__ == "__main__":
    run_smoke_test()