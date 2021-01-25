from pynput.mouse import Button , Controller
import time

mouse = Controller()

mouse.position = (25,1062)
mouse.click(Button.left , 1 )
time.sleep(0.2)
mouse.position = (35,1002)
mouse.click(Button.left , 1 )
time.sleep(0.2)
mouse.position = (60,933)
mouse.click(Button.left , 1 )
mouse.click(Button.left , 1 )


