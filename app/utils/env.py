import os
from dotenv import load_dotenv

def load_env(dotenv_path):
    """
    Подгрузка переменных окружения из файла .env
    """
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return dict(os.environ)
