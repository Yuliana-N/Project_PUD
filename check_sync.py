import psycopg2
try:
    connection = psycopg2.connect(
        dbname="dwhak_stage",        # Имя базы данных
        user="nesterovich_yuyu",            # Пользователь
        password="EUUt2rLx",
        password_db="bOxKLz3",   # Пароль
        host="10.35.1.102",      # Хост (например, localhost или IP-адрес)
        port="5432"                 # Порт (обычно 5432)
    )
    print("Соединение установлено!")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dwhak_stage.pud.users")

except Exception as e:
    print("Ошибка при подключении к Greenplum:", e)
