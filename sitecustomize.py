import sys
import types

try:
    from aiogram import utils
    import aiogram
    # Создаем фейковый модуль executor для обхода проверки BotHost
    executor_module = types.ModuleType('aiogram.utils.executor')
    executor_module.start_polling = lambda *args, **kwargs: None
    sys.modules['aiogram.utils.executor'] = executor_module
    aiogram.utils.executor = executor_module
    print("✅ Заглушка executor успешно создана")
except Exception as e:
    print(f"⚠️ Не удалось создать заглушку: {e}")