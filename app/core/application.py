import PySimpleGUI as sg
import threading
import time
import pyautogui
import re

from .layouts import get_layout

class Application():
    window = None

    interval = 3
    # Начальные данные
    x,y = 0,0
    # количество срабатываний кликера
    count_def = 10
    count = count_def
    # Показатель необходимо ли останавливать поток
    thread_stop = False

    defaults = {
        "count_input": count,
        "interval_input": interval
    }

    def __init__(self, env_vars):
        self.env_vars = env_vars

    def setText(self, el, text):
        self.window.Element(el).Update(text)

    def thread_function(self):
        while True:
            self.setText("count", f"Осталось: {self.count}")

            self.count -= 1
            if self.thread_stop or not self.count:
                self.setText("info", "Кликер не запущен")
                self.setText("count", "")
                self.count = self.count_def
                return

            pyautogui.moveTo(self.x, self.y)
            pyautogui.click()
            time.sleep(self.interval)

    def start(self):
        sg.theme("BluePurple")
        self.window = sg.Window(self.env_vars.get("app_name"),
            [
                [sg.TabGroup([[
                    sg.Tab("Главная", get_layout(self, "main_layout")),
                    sg.Tab("Настройки", get_layout(self, "settings_layout")),
                    sg.Tab("Информация", get_layout(self, "info_layout"))
                ]],
                key="-TAB GROUP-", expand_x=False, expand_y=False)]
            ]
        )

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == "Выход":
                thread_stop = True
                break

            if event == "Получить координаты":
                xpos, ypos = pyautogui.position()
                self.x, self.y = xpos, ypos
                self.window["-XOUT-"].update(self.x)
                self.window["-YOUT-"].update(self.y)
            elif event == "Запустить":
                self.thread_stop = False
                self.setText("info", "Кликер запущен")

                t = threading.Thread(target=self.thread_function)
                t.start()
            elif event == "Остановить":
                self.thread_stop = True
                self.setText("info", "Кликер не запущен")
            elif event == "Сохранить":
                interval = "".join(re.findall("[0-9]+", values.get("interval_input")) if values.get("interval_input") not in (None, "") else 0)
                count = "".join(re.findall("[0-9]+", values.get("count_input")) if values.get("count_input") not in (None, "") else 0)
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
