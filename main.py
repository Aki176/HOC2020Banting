# @Author: Aki176 - Duc Anh Vu
# @Last Modified: Dec 9, 2020
# @Description: DanMachi Tower Defense Game for HOC Banting 2020. (DanMachi is an Anime)

# Import necessary packages and module
import pygame as pg
import tkinter as tk
from statemachine import StateMachine

# Window size 1280x768 so it will be optimized for most devices.
WINDOW_SIZE = (1280, 768)

root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
image_file = ("splash.gif")
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# show the splash screen for 3000 milliseconds then destroy
root.after(3000, root.destroy)
root.mainloop()

# Run the game
def main():
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("music.mp3")
    pg.mixer.music.play(-1)
    window_size = None
    for size in reversed(pg.display.list_modes()):
        if size[0] >= WINDOW_SIZE[0] and size[1] >= WINDOW_SIZE[1]:
            window_size = size
            break
    if window_size is None:
        print("What resolution are you using? 1280x768 is needed")
        return
    print("Game loaded succesfully!!! Enjoy <3")
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption("DanMachi Tower Defense - HOC 2020")
    statemachine = StateMachine(screen)
    statemachine.main_loop()

if __name__ == "__main__":
    main()
