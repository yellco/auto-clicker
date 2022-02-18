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
          [sg.Button('Запустить'), sg.Button('Остановить')],
          [sg.Button('Получить координаты')],
          [sg.Button('Выход')],
          [sg.Text(f'Версия приложения: {version}')]
]

def thread_function():
    global num_to_start, thread_stop
    while True:
        print('thread_func')

        num_to_start -= 1
        if thread_stop or not num_to_start:
            window.Element("info").Update('Кликер не запущен')
            return

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)

window = sg.Window('Авто-кликер', layout)

while True:
    # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    # print(positionStr, end='')
    # print('\b' * len(positionStr), end='', flush=True)

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    
    if event == 'Получить координаты':
        xpos, ypos = pyautogui.position()
        # window['-XOUT-'].update(values['-x-'])
        x, y = xpos, ypos
        window['-XOUT-'].update(x)
        # window['-YOUT-'].update(values['-y-'])
        window['-YOUT-'].update(y)
    elif event == 'Запустить':
        print('Zapusk')

        window.Element("info").Update('Кликер запущен')
        thread_stop = False
        t = threading.Thread(target=thread_function, daemon=True)
        t.start()
    elif event == 'Остановить':
        thread_stop = True
        window.Element("info").Update('Кликер не запущен')

window.close()