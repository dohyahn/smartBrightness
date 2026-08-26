from screen_brightness_control import get_brightness, set_brightness, list_monitors_info
from pynput import keyboard
from sys import exit

displayCount = len(list_monitors_info())
displaySelected = 0
brightnessList = [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 16, 18, 21, 24, 27, 31, 34, 37, 42, 46, 53, 58, 64, 72, 79, 87, 100]

displayBrightnessList = list()

for display in range(displayCount):
    displayBrightnessList.append(get_brightness()[display])

def brightnessIncrease():
    global displayBrightnessList
    for brightness in brightnessList:
        if displayBrightnessList[displaySelected] < brightness:
            set_brightness(brightness, display=displaySelected)
            print(f'Brightness increased to {brightness} on monitor {displaySelected}')
            displayBrightnessList[displaySelected] = brightness
            break

def brightnessDecrease():
    global displayBrightnessList
    for brightness in reversed(brightnessList):
        if displayBrightnessList[displaySelected] > brightness:
            set_brightness(brightness, display=displaySelected)
            print(f'Brightness decreased to {brightness} on monitor {displaySelected}')
            displayBrightnessList[displaySelected] = brightness
            break

def displayIndexIncrease():
    global displaySelected
    displaySelected = (displaySelected + 1) % displayCount
    print('display set to : ', displaySelected)

def displayIndexDecrease():
    global displaySelected
    displaySelected = (displaySelected - 1) % displayCount
    print('display set to : ', displaySelected)

def quit():
    exit()

with keyboard.GlobalHotKeys({
        '<ctrl>+<up>'   : brightnessIncrease,
        '<ctrl>+<down>' : brightnessDecrease,
        '<ctrl>+<left>' : displayIndexDecrease,
        '<ctrl>+<right>': displayIndexIncrease,
        '<ctrl>+<esc>'  : quit}) as h:
    h.join()
