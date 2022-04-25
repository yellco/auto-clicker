import PySimpleGUI as sg

def get_layout(self, name):
    # Главный экран
    main_layout = [
        [sg.Text("Кликер не запущен.", key="info")],
        [sg.Text("Координаты:")],
        [sg.Text("X:"), sg.Text(str(self.x),size=(15,1), key="-XOUT-"), sg.Text("Y:"), sg.Text(str(self.y), size=(15,1), key="-YOUT-")],
        [sg.Text("", key="count")],
        [sg.Button("Запустить"), sg.Button("Остановить")],
        [sg.Button("Получить координаты")],
        [sg.Button("Выход")]
    ]

    # Информационный экран
    info_layout = [
        [sg.Text(f"Версия приложения: {self.env_vars.get('app-version')}")],
        [sg.Text(f"Создано: Yellco в 2022 году")]
    ]

    # Экран настроек
    settings_layout = [
        [sg.Text("Введите количество срабатываний")], 
        [sg.Input(key="count_input", default_text=self.defaults.get("count_input"))],
        [sg.Text("Введите интервал срабатываний")], 
        [sg.Input(key="interval_input", default_text=self.defaults.get("interval_input"))],
        [sg.Button("Сохранить"), sg.Button("Отмена")]
    ]

    return locals().get(name)
