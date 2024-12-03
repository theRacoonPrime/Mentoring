import sqlite3
import os

# Путь к папке для хранения базы данных
db_dir = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db'
db_path = os.path.join(db_dir, 'northwind.db')

# Если папка не существует, создаем её
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Подключаемся к базе данных
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Функция для выполнения SQL-скрипта из файла
def execute_sql_script(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)
    connection.commit()

# Выполняем SQL-скрипт для создания структуры базы данных
execute_sql_script(r'C:\Users\Игорь\Desktop\northwind-SQLite3-main\northwind-SQLite3-main\src\create.sql')

print('Структура базы данных успешно создана!')

# Закрываем соединение с базой данных
connection.close()
