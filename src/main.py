# SyntaxWarning: import * only allowed at module level
from time import sleep
import threading
from pyautogui import Window, click


def activate_window(p: Window):
    """
    :param p: py32win
    """
    # ativa qualquer janela
    p.restore()
    p.show()
    p.activate()
    click(p.center, clicks=0)


def press_key_b4(key: str):
    from keyboard import is_pressed
    """
    Só dá break quando uma tecla específica é pressionada, e então, continua o código
    :param key:
    :return:
    """

    while True:
        #
        if is_pressed(key):
            if is_pressed(key):
                return True
        else:
            ...


def press_keys_b4(*keys: str):
    from keyboard import is_pressed
    """
    :param keys: any key you wish
    :return:
    """
    while True:
        for key in keys:
            if is_pressed(key):
                if is_pressed(key):
                    return key
            else:
                pass
                # print(key)


def foritab(n, *hkeys, interval=.05):
    import pyautogui as pygui
    """
    :param int n: how many times
    :param str hkey: hotkey
    :param float interval:
    :return:
    """
    for ii in range(n):
        for hkey in hkeys:
            pygui.hotkey(hkey, interval=interval)


def all_keys(*keys, interval=.13, only1_by1=True):
    import pyautogui as pygui
    from time import sleep
    """
    :param str keys: Any
    :param float interval:
    :param bool only1_by1: True [safe/DEFAULT]; False => Allows hotkeys with write
    :return:

    # Quando tiver hotkey, aparentemente sempre vai começar com ctrl, shift, alguma coisa do tipo... por isso
    # if cont > 0 and only_by1 True, break
    """
    full_hotkey_list = pygui.KEYBOARD_KEYS
    for cont, key in enumerate(keys):
        if key in full_hotkey_list:
            if cont > 0 and only1_by1:
                raise UserWarning(
                    "Security warning, SET only1_by1 as False [then you'll be able to use hotkeys with write]")

            list_keys = []
            for kd in keys:
                pygui.keyDown(kd, _pause=interval)
                list_keys.append(kd)
            list_keys.reverse()
            for k in list_keys:
                pygui.keyUp(k)
            if only1_by1:
                break
        else:
            pygui.write(key)
            sleep(interval)


def tk_msg(mensagem: str, time=7):
    """
    chamada em activate_driver_window
    :param mensagem: text displayed
    :param time: cont time before closes
    """
    import tkinter as tk

    class ExampleApp(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            tk.Label(text=mensagem, pady=10).pack()

            tk.Button(self, text="OK", fg='white', bg='black', command=self.destroy, activeforeground="black",
                      activebackground="green4", pady=10, width=10).pack()

            self.label = tk.Label(self, text="", width=10)
            self.label.pack()
            self.remaining = 0
            self.countdown(time)
            # self.after(time * 1000, lambda: self.destroy())

            self.geometry('500x250+1400+10')

        def countdown(self, remaining=None):
            if remaining is not None:
                self.remaining = remaining

            if self.remaining <= 0:
                self.label.configure(text="000000")
                self.destroy()
            else:
                self.label.configure(text="%d" % self.remaining)
                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)

    print('Mensagem: ', mensagem)
    ExampleApp().mainloop()
