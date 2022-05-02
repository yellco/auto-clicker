from .baselayout import BaseLayout


class MainLayout(BaseLayout):
	def __init__(self, name, tab_name, app_data):
		super().__init__(app_data=app_data)
		self.layout = [
			[app_data.gui.Text("Кликер не запущен.", key="info")],
			[app_data.gui.Text("Координаты:")],
			[
				app_data.gui.Text("X:"), app_data.gui.Text(str(app_data.x_coord), size=(15, 1), key="-XOUT-"),
				app_data.gui.Text("Y:"), app_data.gui.Text(str(app_data.y_coord), size=(15, 1), key="-YOUT-")
			],
			[app_data.gui.Text("", key="count")],
			[app_data.gui.Button("Запустить"), app_data.gui.Button("Остановить")],
			[app_data.gui.Button("Получить координаты")],
			[app_data.gui.Button("Выход")]
		]
		self.name = name
		self.tab_name = tab_name
