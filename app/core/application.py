import threading
import time
import re
import pyautogui
import PySimpleGUI as sg

from .layouts.infolayout import InfoLayout
from .layouts.settingslayout import SettingsLayout
from .layouts.mainlayout import MainLayout


class Application:
	"""
	Основной класс приложения
	"""
	window = None

	# Интервал срабатывания
	interval = 3
	# Начальные данные
	x_coord, y_coord = 0, 0
	# Количество срабатываний кликера
	count_def = 10
	count = count_def
	# Показатель необходимо ли останавливать поток
	thread_stop = False
	# Список вкладок
	tabs_group = []
	# Привязываем sg к экземпляру
	gui = sg

	defaults = {
		"count_input": count,
		"interval_input": interval
	}

	def __init__(self, env_vars):
		self.env_vars = env_vars

	def set_text(self, element, text):
		"Установка текста"
		self.window.Element(element).Update(text)

	def thread_function(self):
		"""
		Подсчет кликера
		Запускается в отдельном потоке
		"""
		while True:
			self.set_text("count", f"Осталось: {self.count}")

			self.count -= 1
			if self.thread_stop or not self.count:
				self.set_text("info", "Кликер не запущен")
				self.set_text("count", "")
				self.count = self.count_def
				return

			pyautogui.moveTo(self.x_coord, self.y_coord)
			pyautogui.click()
			time.sleep(self.interval)

	def start(self):
		"Запуск кликера"

		self.gui.theme("BluePurple")

		# Создание layout и добавление к вкладкам
		for layout in [
			MainLayout(tab_name="Главная", name="main_layout", app_data=self),
			SettingsLayout(tab_name="Настройки", name="settings_layout", app_data=self),
			InfoLayout(tab_name="Информация", name="info_layout", app_data=self)
		]:
			self.tabs_group.append(layout.create_tab())

		self.window = self.gui.Window(
			self.env_vars.get("app_name"),
			[
				[self.gui.TabGroup(
					[self.tabs_group],
					key="-TAB GROUP-", expand_x=False, expand_y=False)]])

		while True:
			event, values = self.window.read()

			if event == self.gui.WIN_CLOSED or event == "Выход":
				self.thread_stop = True
				break

			if event == "Получить координаты":
				xpos, ypos = pyautogui.position()
				self.x_coord, self.y_coord = xpos, ypos
				self.window["-XOUT-"].update(self.x_coord)
				self.window["-YOUT-"].update(self.y_coord)
			elif event == "Запустить":
				self.thread_stop = False
				self.set_text("info", "Кликер запущен")

				addit_thread = threading.Thread(target=self.thread_function)
				addit_thread.start()
			elif event == "Остановить":
				self.thread_stop = True
				self.set_text("info", "Кликер не запущен")
			elif event == "Сохранить":
				interval = "".join(
					re.findall("[0-9]+", values.get("interval_input")) if values.get("interval_input") not in (
						None, "") else 0)
				count = "".join(re.findall("[0-9]+", values.get("count_input")) if values.get("count_input") not in (
					None, "") else 0)
				self.interval = int(interval)
				self.count = int(count)
				self.window["interval_input"].update(self.interval)
				self.window["count_input"].update(self.count)
			elif event == "Отмена":
				self.interval = self.defaults["interval_input"]
				self.count = self.defaults["count_input"]
				self.window["interval_input"].update(self.interval)
				self.window["count_input"].update(self.count)
		self.window.close()
