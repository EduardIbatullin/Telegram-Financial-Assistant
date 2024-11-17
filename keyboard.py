from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Создание клавиатуры с кнопками
def create_main_keyboard():
    button_registration = KeyboardButton(text="Регистрация в телеграм-боте")
    button_exchange_rates = KeyboardButton(text="Курс валют")
    button_tips = KeyboardButton(text="Советы по экономии")
    button_finances = KeyboardButton(text="Личные финансы")

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [button_registration, button_exchange_rates],
        [button_tips, button_finances]
    ], resize_keyboard=True)

    return keyboard
