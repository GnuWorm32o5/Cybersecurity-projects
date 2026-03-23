from pynput.mouse import Controller
from pynput.keyboard import Controller



def control_keyboard():
    keyboard = Controller()
    keyboard.type("I am freaking awesome.")

control_keyboard()