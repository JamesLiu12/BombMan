import time
from pynput import keyboard
import os
# import msvcrt
# def press(key):
#     print(key)
# with keyboard.Listener(on_press=press) as kl:
#     while True:
#         print('1')
#         sleep(1)
# from time import sleep
# import keyboard
# while True:
#     if keyboard.is_pressed('w'):
#         print('w')
#     if keyboard.is_pressed('s'):
#         print('s')
#     sleep(1/60)
# def move():
#     print('w')
# from pynput import keyboard,mouse
# with keyboard.Listener(on_press=move()) as KeyboardListener:
#     while True:
#         print('1')
#         time.sleep(0.1)
class A:
    def __init__(self) -> None:
        self.b = B(self)
class B:
    def __init__(self, a) -> None:
        self.a = a
a = A()
print(id(a.b))