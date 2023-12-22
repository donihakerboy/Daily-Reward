from tkinter import messagebox
class Decorator:
    def __init__(self, observer):
        self._observer = observer

    def update(self, message) -> str:
        messagebox.showwarning(message=f"{message}")

class ShowMessageBoxDecorator(Decorator):
    def update(self, message) -> str:
        messagebox.showwarning(message=f"{message}")