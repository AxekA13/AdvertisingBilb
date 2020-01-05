import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from View.BasicWindow import Window
from Presenters import ViewAdvUserPresenter
from tkinter import messagebox

lock = threading.Lock()
import time


class ViewAdvertising(Window):
    def __init__(self, device):
        super().__init__()
        self.show_video(device)

    def show_video(self, device):
        self.set_window(device.name)
        self.configure(bg='white')
        video_name = device.get_schedule_timer()
        # ViewAdvUserConrtoller.ViewAdvUserController(user).get_advertising_list(device)
        my_label = tk.Label(self)
        my_label.pack()
        for vid in video_name:  # This is your video file path
            self.video = imageio.get_reader(vid)
            thread = threading.Thread(target=self.stream, args=(my_label,))
            thread.daemon = 2
            thread.start()


    def stream(self, label):
        with lock:
            for image in self.video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image
