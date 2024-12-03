from datetime import timedelta, datetime
from random import randint, choice as rc
import sqlite3

# Функция для преобразования дат в строку ISO 8601 перед вставкой в базу данных
def adapt_datetime_iso(dt):
    return dt.isoformat()

# Функция для преобразования строк ISO 8601 обратно в объект datetime при чтении из базы данных
def convert_datetime_iso(s):
    return datetime.fromisoformat(s)

# Регистрируем адаптеры и конвертеры для работы с датами
sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("DATETIME", convert_datetime_iso)

# Подключаемся к базе данных с включенным режимом конвертации дат
conn = sqlite3.connect(r'C:/Users/Игорь/PycharmProjects/KNB/Igor/db/northwind.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()

# Функция для генерации случайных дат
def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

# Получаем информацию для заказов
c.execute("SELECT DISTINCT ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry FROM [Orders]")
locations = [(row[0], row[1], row[2], row[3], row[4], row[5]) for row in c.fetchall()]

c.execute("SELECT DISTINCT EmployeeId FROM [Employees]")
employees = [row[0] for row in c.fetchall()]

c.execute("SELECT DISTINCT ShipperId FROM [Shippers]")
shippers = [row[0] for row in c.fetchall()]

c.execute("SELECT DISTINCT CustomerId FROM [Customers]")
customers = [row[0] for row in c.fetchall()]

# Генерируем новые заказы
for i in range(randint(15000, 16000)):
    sql = """INSERT INTO [Orders] (CustomerId, EmployeeId, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, 
             ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    location = rc(locations)
    order_date = random_date(datetime.strptime("2012-07-10", "%Y-%m-%d"), datetime.today())
    required_date = random_date(order_date, order_date + timedelta(days=randint(14, 60)))
    shipped_date = random_date(order_date, order_date + timedelta(days=randint(1, 30)))
    params = (
        rc(customers),  # CustomerId
        rc(employees),  # EmployeeId
        order_date,  # OrderDate
        required_date,  # RequiredDate
        shipped_date,  # ShippedDate
        rc(shippers),  # ShipVia
        0.00,  # Freight
        location[0],  # ShipName
        location[1],  # ShipAddress
        location[2],  # ShipCity
        location[3],  # ShipRegion
        location[4],  # ShipPostalCode
        location[5],  # ShipCountry
    )
    c.execute(sql, params)

# Подтверждаем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("Данные успешно добавлены!")

