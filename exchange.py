import requests
from aiogram import Router, F
from aiogram.types import Message
from config import Config

# Инициализация роутера
router = Router()


# Обработчик запроса курса валют
@router.message(F.text == "Курс валют")
async def exchange_rates(message: Message):
    url = f'https://v6.exchangerate-api.com/v6/{Config.EXCHANGE_API_KEY}/latest/USD'
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            await message.answer(text="Не удалось получить данные о курсе валют!")
            return

        usd_to_rub = data['conversion_rates']['RUB']
        usd_to_eur = data['conversion_rates']['EUR']
        eur_to_rub = usd_to_rub / usd_to_eur

        await message.answer(text=f"1 USD = {usd_to_rub:.2f} RUB\n1 EUR = {eur_to_rub:.2f} RUB")
    except:
        await message.answer(text="Не удалось получить данные о курсе валют!")
