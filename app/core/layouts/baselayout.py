class BaseLayout:
	# Разметка layout
	layout = None
	# Название layout
	name = None
	# Название вкладки
	tab_name = None
	# Прочая базовая информация для layout
	app_data = None

	def __init__(self, app_data):
		self.app_data = app_data

	def create_tab(self):
		return self.app_data.gui.Tab(self.tab_name, self.layout)
