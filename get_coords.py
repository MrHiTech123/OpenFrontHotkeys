import threading
import pynput.mouse as mouse
 

def on_click(x, y):
    print('{}, {}'.format(x, y))

listeners: list[threading.Thread] = [
    mouse.Listener(on_click=on_click)
]

for listener in listeners:
    listener.start()

for listener in listeners:
    listener.join()

