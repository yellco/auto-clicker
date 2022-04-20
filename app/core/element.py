import PySimpleGUI as sg
import threading
import time
import pyautogui

class Element():
    window = None

    interval = 3
    # Начальные данные
    x,y = 0,0
    # количество срабатываний кликера
    num_to_start_def = 10
    num_to_start = num_to_start_def
    # Показатель необходимо ли останавливать поток
    thread_stop = False

    def __init__(self, env_vars):
        self.env_vars = env_vars

    def setText(self, el, text):
        self.window.Element(el).Update(text)
    
    def thread_function(self):
        while True:
            self.setText("num_to_start", f"Осталось: {self.num_to_start}")

            self.num_to_start -= 1
            if self.thread_stop or not self.num_to_start:
                self.setText("info", "Кликер не запущен")
                self.setText("num_to_start", "")
                self.num_to_start = self.num_to_start_def
                return

            pyautogui.moveTo(self.x, self.y)
            pyautogui.click()
            time.sleep(self.interval)

    def start(self):
        sg.theme('BluePurple')
        self.window = sg.Window('Авто-кликер', 
            [
                [sg.Text('Координаты:')],
                [sg.Text('X:'), sg.Text(str(self.x),size=(15,1), key='-XOUT-'), sg.Text('Y:'), sg.Text(str(self.y), size=(15,1), key='-YOUT-')],
                [sg.Text('Кликер не запущен.', key='info')],
                [sg.Text('', key='num_to_start')],
                [sg.Button('Запустить'), sg.Button('Остановить')],
                [sg.Button('Получить координаты')],
                [sg.Button('Выход')],
                [sg.Text(f'Версия приложения: {self.env_vars.get("app-version")}')]
            ]
        )

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Выход':
                thread_stop = True
                break
            
            if event == 'Получить координаты':
                xpos, ypos = pyautogui.position()
                self.x, self.y = xpos, ypos
                self.window['-XOUT-'].update(self.x)
                self.window['-YOUT-'].update(self.y)
            elif event == 'Запустить':
                self.thread_stop = False
                self.setText("info", "Кликер запущен")

                t = threading.Thread(target=self.thread_function)
                t.start()
            elif event == 'Остановить':
                self.thread_stop = True
                self.setText("info", "Кликер не запущен")
        
        self.window.close()