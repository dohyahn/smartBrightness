from screen_brightness_control import get_brightness, set_brightness, list_monitors_info
from pynput import keyboard
from sys import exit

d_c = len(list_monitors_info())
d = 0
b_l = [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 16, 18, 21, 24, 27, 31, 34, 37, 42, 46, 53, 58, 64, 72, 79, 87, 100]
b_c = len(b_l)

def brightness_up():
    b_r = get_brightness()[d]
    b_i = 0
    for i in range(b_c):
        if b_r <= b_l[i]:
            b_i = i
            break
    b_i = min(b_i + 1, b_c - 1)
    set_brightness(b_l[b_i], display=d)
    print('Brightness set to : ', get_brightness()[d])

def brightness_down():
    b_r = get_brightness()[d]
    b_i = 0
    for i in range(b_c-1, -1, -1):
        if b_r >= b_l[i]:
            b_i = i
            break
    b_i = max(b_i - 1, 0)
    set_brightness(b_l[b_i], display=d)
    print('Brightness set to : ', get_brightness()[d])

def monitor_left():
    global d
    if d==0:
        d = d_c - 1
    else:
        d -= 1
    print('Monitor set to : ', d)

def monitor_right():
    global d
    if d==d_c-1:
        d = 0
    else:
        d += 1
    print('Monitor set to : ', d)

def quit():
    exit()

with keyboard.GlobalHotKeys({
        '<ctrl>+<up>'   : brightness_up,
        '<ctrl>+<down>' : brightness_down,
         '<ctrl>+<left>' : monitor_left,
        '<ctrl>+<right>': monitor_right,
        '<ctrl>+<esc>'  : quit}) as h:
    h.join()