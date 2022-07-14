from .baselayout import BaseLayout


class SettingsLayout(BaseLayout):
	"""
	Вкладка настроек
	"""
	def __init__(self, name, tab_name, app_data):
		super().__init__(app_data=app_data)
		self.layout = [
			[app_data.gui.Text("Введите количество срабатываний")],
			[app_data.gui.Input(key="count_input", default_text=app_data.defaults.get("count_input"))],
			[app_data.gui.Text("Введите интервал срабатываний")],
			[app_data.gui.Input(key="interval_input", default_text=app_data.defaults.get("interval_input"))],
			[app_data.gui.Button("Сохранить"), app_data.gui.Button("Отмена")]
		]
		self.name = name
		self.tab_name = tab_name
