import tkinter as tk
import os
import shutil


class UserActionContr:
    def get_log(self):
        with open(r"C:\Users\nasty\PycharmProjects\Bilbords\user_action.log", "r") as file:
            old = file.read().splitlines()
        file.close()
        return old
