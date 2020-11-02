import tkinter as tk


def app():
    root = tk.Tk()
    root.title("Covid-Africa",)
    screen_width = int(root.winfo_screenwidth())
    screen_height = int(root.winfo_screenheight())
    window_x = 640
    window_y = 480

    position_x = (screen_width // 2) - (window_x // 2)
    position_y = (screen_height // 2) - (window_y // 2)
    root.geometry("{}x{}+{}+{}".format(window_x, window_y, position_x, position_y))
    root.resizable(width=False, height=False)
    # root.minsize(640, 480)
    return root
