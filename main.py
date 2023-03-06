import tkinter as tk
import urllib.request as urlR

root = tk.Tk()
root.title("Send Email")
root.geometry("275x300")

def check_connection(host):
    try:
        urlR.urlopen(host)
        print("Connected")
        return True
    except Exception as e:
        print(e)
        return False

if check_connection('http://google.com'):
    print("connected")
else:
    print("no connection")


tk.Button(root, text="Compose").grid(row=0, column=0, sticky="nesw")

root.mainloop()