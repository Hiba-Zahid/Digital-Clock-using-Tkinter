import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

label = tk.Label(root, font=('Helvetica', 40), fg='blue')
label.pack(pady=20)

update_time()
root.mainloop()
