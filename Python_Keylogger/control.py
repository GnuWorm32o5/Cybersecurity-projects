from pynput.mouse import Controller

def control_mouse():
    mouse = Controller()
    mouse.position = (10,20)


control_mouse()
