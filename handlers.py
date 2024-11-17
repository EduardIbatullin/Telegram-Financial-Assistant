from aiogram import Router
from registration import router as registration_router
from exchange import router as exchange_router
from tips import router as tips_router
from finances import router as finances_router

# Главный роутер, объединяющий все обработчики
router = Router()
router.include_router(registration_router)
router.include_router(exchange_router)
router.include_router(tips_router)
router.include_router(finances_router)
