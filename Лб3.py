import sqlite3
import hashlib

# Підключення до бази даних
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Створення таблиці
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    login TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
""")
conn.commit()


# Хешування пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Додавання ТВОГО користувача (Фролов Михайло)
def add_default_user():
    login = "frolov"
    password = "12345"
    full_name = "Фролов Михайло"

    hashed_password = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
            (login, hashed_password, full_name)
        )
        conn.commit()
        print("Користувач Фролов Михайло доданий у БД")
    except sqlite3.IntegrityError:
        print("Користувач Фролов Михайло вже існує у БД")


# Перевірка автентифікації
def authenticate():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    hashed_password = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE login = ? AND password = ?",
        (login, hashed_password)
    )

    user = cursor.fetchone()

    if user:
        print("Авторизація успішна")
        print("Ласкаво просимо,", user[2])
    else:
        print("Невірний логін або пароль")


# Головна частина програми
add_default_user()
authenticate()

conn.close()