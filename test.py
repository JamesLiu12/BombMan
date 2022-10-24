# from time import sleep
# from pynput import keyboard
# import os
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
class A:
    def __init__(self) -> None:
        self.a = 1
a = A()
g = [a]
del g[0]
print(len(g))
print(a.a)