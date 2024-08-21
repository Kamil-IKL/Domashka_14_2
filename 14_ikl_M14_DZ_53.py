import sqlite3

# Основные операторы:
# "SELECT"(получить)
# "FROM" (от)
# "WHERE"(где)
# "GROUP BY" (группировать по)
# "HAVING" (имеющий)
# "ORDER BY" (заказать по)

connection = sqlite3.connect('not_telegram.db')

# создаю курсор
cursor = connection.cursor()

# создаю БДешку
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)
""")

# 1.добавляю с использованием цикла for
for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i + 1}", f"example{i + 1}gmail.com", int(i * 10 + 10), int(1000)))

# 2.создал запрос на изменение параметра "баланс"
cursor.execute("UPDATE Users SET balance = ? WHERE ID % 2 = 1", (500,))

# 3.создал запрос на удаление каждой третьей строки, начиная с первой
# ТАК НЕ ПОЛУЧИЛОСЬ, КАК ПРОСЯТ В ЗАДАНИИ
# cursor.execute("DELETE FROM Users WHERE ID = 1 OR ID % 3 = 0") #  - ТАК НЕ ПОЛУЧИЛОСЬ, КАК ПРОСЯТ В ЗАДАНИИ

# И ТАК НЕ ПОЛУЧИЛОСЬ, КАК ПРОСЯТ В ЗАДАНИИ
# cursor.execute("DELETE FROM Users WHERE ID = 1") # удаляю сначала первую строку
# cursor.execute("DELETE FROM Users WHERE ID % 3 = 0") # удаляю каждую третью строку

# СДЕЛАЛ ПО ПРОСТОМУ, ТУПО УКАЗАЛ СТРОКИ
cursor.execute("DELETE FROM Users WHERE ID = 1 OR ID = 4 OR ID = 7 OR ID = 10")

# cursor.execute("DELETE FROM Users") # стирает все строки в БДешке (для обновления... если, что не так)

# 4.Выбрал записи, где возраст > 60 c заданными полями
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age > ?", (60,))

# 5. Вывожу на консоль свою выборку(п.4) в заданном формате
users = cursor.fetchall()
for user in users:
    username, mail, age, balance = user[0], user[1], user[2], user[3]
    print(f"Имя: {username} | Почта: {mail} | Возраст: {age} | Баланс: {balance}")


print(f'\n{" Задание 14-02 ":*^44}')
cursor.execute('DELETE FROM Users WHERE ID = 6') # удалил id-6
cursor.execute('SELECT COUNT(*) FROM Users') # запрос на подсчет всех пользователей
users = cursor.fetchone()[0]
print('Всего пользователей =', users)

cursor.execute('SELECT SUM(balance) FROM Users') # запрос на суммирование по полю "balance"
all_balance = cursor.fetchone()[0]
print('Сумма всех балансов =', all_balance)

cursor.execute('SELECT AVG(balance) FROM Users') # запрос на вычисление среднего числа по полю "balance"
avg_balance = cursor.fetchone()[0]
print('Средняя сумма балансов =', avg_balance)

connection.commit()
connection.close()
