import PySimpleGUI as sg
import pyautogui
import time
import threading

version = "0.0.1"
# интервал в секундах
interval = 3
# Начальные данные
x,y = 0,0
# количество срабатываний кликера
num_to_start = 10
thread_stop = False

sg.theme('BluePurple')

layout = [
          [sg.Text('Координаты:')],
          [sg.Text('X:'), sg.Text(str(x),size=(15,1), key='-XOUT-'), sg.Text('Y:'), sg.Text(str(y), size=(15,1), key='-YOUT-')],
          [sg.Text('Кликер не запущен.', key='info')],
          [sg.Text('', key='count')],
          [sg.Button('Запустить'), sg.Button('Остановить')],
          [sg.Button('Получить координаты')],
          [sg.Button('Выход')],
          [sg.Text(f'Версия приложения: {version}')]
]

def setText(el, text):
    window.Element(el).Update(text)

def thread_function():
    global num_to_start, thread_stop
    while True:
        print('thread_func')

        num_to_start -= 1
        if thread_stop or not num_to_start:
            setText("info", "Кликер не запущен")
            return

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)

window = sg.Window('Авто-кликер', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    
    if event == 'Получить координаты':
        xpos, ypos = pyautogui.position()
        x, y = xpos, ypos
        window['-XOUT-'].update(x)
        window['-YOUT-'].update(y)
    elif event == 'Запустить':
        thread_stop = False
        setText("info", "Кликер запущен")

        t = threading.Thread(target=thread_function, daemon=True)
        t.start()
    elif event == 'Остановить':
        thread_stop = True
        setText("info", "Кликер не запущен")

window.close()