import sqlite3
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter

# Инициализация роутера
router = Router()

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


# Создание таблицы для работы с состояниями пользователя
class FinancesForm(StatesGroup):
    category_1 = State()
    category_2 = State()
    category_3 = State()
    expenses_1 = State()
    expenses_2 = State()
    expenses_3 = State()


# Обработчики для управления личными финансами
@router.message(F.text == "Личные финансы")
async def finances(message: Message, state: FSMContext):
    await state.set_state(FinancesForm.category_1)
    await message.answer(text="Введите первую категорию расходов:")


@router.message(StateFilter(FinancesForm.category_1))
async def category_1(message: Message, state: FSMContext):
    await state.update_data(category_1=message.text)
    await state.set_state(FinancesForm.expenses_1)
    await message.answer(text="Введите расходы для первой категории:")


@router.message(StateFilter(FinancesForm.expenses_1))
async def expenses_1(message: Message, state: FSMContext):
    await state.update_data(expenses_1=float(message.text))
    await state.set_state(FinancesForm.category_2)
    await message.answer(text="Введите вторую категорию расходов:")


@router.message(StateFilter(FinancesForm.category_2))
async def category_2(message: Message, state: FSMContext):
    await state.update_data(category_2=message.text)
    await state.set_state(FinancesForm.expenses_2)
    await message.answer(text="Введите расходы для второй категории:")


@router.message(StateFilter(FinancesForm.expenses_2))
async def expenses_2(message: Message, state: FSMContext):
    await state.update_data(expenses_2=float(message.text))
    await state.set_state(FinancesForm.category_3)
    await message.answer(text="Введите третью категорию расходов:")


@router.message(StateFilter(FinancesForm.category_3))
async def category_3(message: Message, state: FSMContext):
    await state.update_data(category_3=message.text)
    await state.set_state(FinancesForm.expenses_3)
    await message.answer(text="Введите расходы для третьей категории:")


@router.message(StateFilter(FinancesForm.expenses_3))
async def expenses_3(message: Message, state: FSMContext):
    data = await state.get_data()
    telegram_id = message.from_user.id

    cursor.execute('''
        UPDATE users 
        SET category_1 = ?, category_2 = ?, category_3 = ?, expenses_1 = ?, expenses_2 = ?, expenses_3 = ? 
        WHERE telegram_id = ?''',
        (
            data['category_1'], data['category_2'], data['category_3'],
            data['expenses_1'], data['expenses_2'], float(message.text),
            telegram_id
        )
    )
    conn.commit()

    await state.clear()
    await message.answer(text="Ваши данные о категориях и расходах сохранены.")
