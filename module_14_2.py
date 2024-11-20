import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполнение записями
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', str(i * 10), str(1000)))

# Выбор всех записей
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

# Обновление баланса в каждой 2-й записи
for i in range(len(users)):
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ('500', users[i][1]))

# Удаление каждой 3-й записи
for i in range(len(users)):
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users WHERE username = ?", (users[i][1],))

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = ?", ("6",))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
