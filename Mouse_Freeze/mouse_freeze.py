from pynput.mouse import Controller
from pynput import keyboard
import threading
import time

mouse = Controller()
running = True

def lock_mouse():
    pos = mouse.position = (1000,10) # Initial position
    while running:
        mouse.position = pos
        time.sleep(0.1)

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        print("Escape pressed, exiting.")
        running = False
        return False #stop listener

#Run mouse lock in separate thread
t = threading.Thread(target=lock_mouse)
t.start()

# Listen for ESC key
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

t.join()