import os
from dotenv import load_dotenv

def load_env(dotenv_path):
    """
    Подгрузка переменных окружения из файла .env
    """
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError("Отсутствие .env файла")

    # Приведение к нижнему регистру
    env_lower = {key.lower():dict(os.environ).get(key) for key in dict(os.environ)}
    return env_lower
