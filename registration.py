import sqlite3
from aiogram import Router, F
from aiogram.types import Message

# Инициализация роутера
router = Router()

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY, 
        telegram_id INTEGER UNIQUE, 
        username TEXT
    )
''')
conn.commit()


# Обработчик регистрации пользователя
@router.message(F.text == "Регистрация в телеграм-боте")
async def registration(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = cursor.fetchone()

    if user:
        await message.answer(text="Вы уже зарегистрированы.")
    else:
        cursor.execute('INSERT INTO users(telegram_id, username) VALUES(?, ?)', (telegram_id, username))
        conn.commit()
        await message.answer(text="Вы успешно зарегистрированы.")
