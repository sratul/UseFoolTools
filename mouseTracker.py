import pyautogui
from pynput.mouse import Listener,Button
import time
from tkinter import Tk,Label
from PIL import ImageTk, Image

previous_press = 0

def on_click(x, y, button, pressed):
    global previous_press
    if pressed and button == Button.middle:
            current_time = time.time()

            diff_left = current_time - previous_press
            print('diff left:', diff_left)
            if diff_left < 0.3:
                print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
                # height = 1920
                # width = 1080
                # pyautogui.moveTo(height / 2, width / 2)

                #Create an instance of tkinter frame
                win = Tk()

                w,h= 100,100

                win.title("Mouse here")
                #Set the geometry of tkinter frame
                win.geometry('%dx%d+%d+%d' % (w, h, x, y))

                #Initialize a Label widget
                # Label(win, text= "Mouse \n here",
                # font=('Helvetica 40 bold')).pack(pady=20)

                win.attributes("-topmost", True)

                win.overrideredirect(True)
                
                resized_image= Image.open("mouse.png").resize((w,h))
                img = ImageTk.PhotoImage(resized_image)
                panel = Label(win, image = img)
                panel.pack(side="bottom",fill= "both",expand="false")

    
                #Automatically close the window after 3 seconds
                win.after(700,lambda:win.destroy())

                win.mainloop()


            previous_press = current_time

with Listener(on_click=on_click) as listener:
    listener.join()

