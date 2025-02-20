import os
import subprocess
import tkinter as tk

def open_cmd_and_show_textbox():
    # CMDを開く
    subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    # Tkinterウィンドウを開く
    root = tk.Tk()
    root.title("Hello World Window")
    root.geometry("300x100")
    
    label = tk.Label(root, text="Hello World", font=("Arial", 16))
    label.pack(pady=20)
    
    root.mainloop()

# ボタンをクリックすると関数が実行されるGUI
app = tk.Tk()
app.title("Launcher")
app.geometry("200x100")

button = tk.Button(app, text="Click Me", command=open_cmd_and_show_textbox)
button.pack(pady=20)

app.mainloop()
