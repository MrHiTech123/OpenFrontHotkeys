import threading
from enum import Enum
from typing import NamedTuple
import pyautogui
import pynput.mouse as mouse
import pynput.keyboard as keyboard
import pynput.keyboard

from data_storage import *




    
# def on_click(x, y):
#     print('{}, {}'.format(x, y))

def get_char(key: "pynput.keyboard._win32.KeyCode"):
    try:
        return key.char
    except AttributeError:
        return None

def on_press(key: "pynput.keyboard._win32.KeyCode"):
    
    char = get_char(key)
    
    if char == 'q':
        raise SystemExit(0)
    
    build = Build.from_key(char)
    if build is not None:
        build.do()
        return
    
    action = Action.from_key(char)
    if action is not None:
        action.do()

listeners: list[threading.Thread] = [
    # mouse.Listener(on_click=on_click)
    keyboard.Listener(on_press=on_press)
]

for listener in listeners:
    listener.start()

for listener in listeners:
    listener.join()



