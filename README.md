# Telegram Финансовый Помощник

## Описание

Этот проект представляет собой Telegram-бота, который помогает пользователям управлять своими личными финансами, получать актуальные курсы валют и советы по экономии. Бот поддерживает регистрацию пользователей, позволяет сохранять и отслеживать личные расходы, а также предоставляет полезные рекомендации для оптимизации бюджета.

### Функциональные возможности:

1. **Регистрация пользователя:**
   - Пользователи могут зарегистрироваться в боте, чтобы использовать функционал личных финансов и сохранять свои данные.

2. **Курсы валют:**
   - Бот предоставляет актуальную информацию о курсах валют, таких как USD и EUR, по отношению к RUB.

3. **Советы по экономии:**
   - Пользователь может получить случайный совет по экономии средств, чтобы оптимизировать свой бюджет.

4. **Личные финансы:**
   - Пользователь может вводить категории расходов и соответствующие суммы, которые сохраняются в базе данных для дальнейшего анализа.

## Структура проекта

Проект структурирован по модульному принципу для легкой поддержки и расширения:

```
project_folder/
│
├── config.py         # Модуль конфигурации, загрузка переменных окружения
├── keyboard.py       # Модуль для создания клавиатуры
├── handlers.py       # Модуль, объединяющий все обработчики
├── registration.py   # Модуль для регистрации пользователей
├── exchange.py       # Модуль для работы с курсами валют
├── tips.py           # Модуль для предоставления советов по экономии
├── finances.py       # Модуль для работы с личными финансами
├── main.py           # Главный файл для запуска бота
├── requirements.txt  # Список зависимостей Python
└── users.db          # База данных SQLite для хранения информации о пользователях
```

### Модули:

- **config.py:** Загрузчик конфигураций и переменных окружения из `.env` файла.
- **keyboard.py:** Генерация клавиатуры для взаимодействия с пользователем.
- **handlers.py:** Объединение всех обработчиков (регистрация, курсы валют, советы, финансы) в один роутер.
- **registration.py:** Обработка регистрации пользователя и управление базой данных пользователей.
- **exchange.py:** Обработка получения курсов валют с внешнего API и отправка пользователю.
- **tips.py:** Предоставление случайного совета по экономии пользователю.
- **finances.py:** Управление личными финансами пользователя через FSM (Finite State Machine).
- **main.py:** Главный файл для запуска и настройки бота.

## Установка и настройка

### 1. Клонирование репозитория:

```bash
git clone https://github.com/EduardIbatullin/Telegram-Financial-Assistant.git
cd Telegram-Financial-Assistant
```

### 2. Установка зависимостей:

Убедитесь, что у вас установлен Python 3.10 или выше.

```bash
pip install -r requirements.txt
```

### 3. Создание и настройка `.env` файла:

Создайте `.env` файл в корневом каталоге проекта и добавьте в него следующие переменные:

```
TELEGRAM_API_TOKEN=your_telegram_bot_token
EXCHANGE_API_KEY=your_exchange_rate_api_key
X_RAPID_API_KEY=your_rapid_api_key
```

### 4. Запуск проекта:

```bash
python main.py
```

## Используемые технологии

- **Python 3.10+**
- **Aiogram 3.x** - Асинхронная библиотека для работы с Telegram API.
- **SQLite** - Легковесная база данных для хранения данных о пользователях.
- **Requests** - Библиотека для выполнения HTTP-запросов.
- **Python-dotenv** - Библиотека для работы с переменными окружения.

## База данных

Проект использует SQLite для хранения информации о пользователях. Таблица `users` сохраняет следующие данные:

- `id` (INTEGER) - Уникальный идентификатор пользователя.
- `telegram_id` (INTEGER) - Telegram ID пользователя.
- `username` (TEXT) - Имя пользователя.
- `category_1`, `category_2`, `category_3` (TEXT) - Категории расходов.
- `expenses_1`, `expenses_2`, `expenses_3` (REAL) - Соответствующие суммы расходов.

## Разработка и вклад

Если вы хотите внести свой вклад в проект, создайте форк репозитория и отправьте pull request с вашими изменениями.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности можно найти в файле LICENSE.

---

Надеемся, что этот бот станет полезным помощником в управлении вашими финансами!
 
