from .baselayout import BaseLayout


class InfoLayout(BaseLayout):
	def __init__(self, name, tab_name, app_data):
		super().__init__(app_data=app_data)
		self.layout = [
			[app_data.gui.Text(f"Версия приложения: {app_data.env_vars.get('app_version')}")],
			[app_data.gui.Text("Создано: Yellco в 2022 году")]
		]
		self.name = name
		self.tab_name = tab_name
