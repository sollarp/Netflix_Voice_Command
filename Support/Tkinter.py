import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("My GUI")

# Create label
label = tk.Label(root, text="Hello, World!", font=('Times', '30'), fg='lime green', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+850+50")
#label.master.lift()

label.master.wm_attributes("-topmost", True)
#label.master.wm_attributes("-disabled", True)
#label.master.wm_attributes("-transparentcolor", "white")

# Lay out label
label.pack()
label.update()
time.sleep(2)
label.master.destroy()

