import pytest
from app.utils.env import load_env
from main import dotenv_path


def test_load_env():
	"""
	Тестирование функционала подгрузки переменных окружения
	"""
	envs = load_env(dotenv_path)
	assert len(envs.keys()) > 0
