import tkinter as tk
from tkinter import messagebox
from observer import TaskObserver
from command import Command, AddTaskCommand, DeleteTaskCommand, Invoker
from strategy import NotifyTaskAddStrategy, NotifyDeleteStrategy, Context
from decorator import ShowMessageBoxDecorator
class ToDoApp(tk.Tk):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tasks = []
        return cls._instance
    
    def __init__(self):
        super().__init__()
        self.invoker = Invoker()

        frame = tk.Frame(self)
        frame.pack(pady=10)

        self.listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self, width=40)
        self.entry.pack(pady=10)

        add_button = tk.Button(self, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.RIGHT, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task == '':
            messagebox.showwarning("(!)", "Please name your task.")
            return
        notify_add_strategy = NotifyTaskAddStrategy()
        self.invoker.set_command(AddTaskCommand(self, task))
        command = self.invoker.execute_command()
        context = Context(notify_add_strategy)
        context.execute_strategy(command)

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("(!)", "Please select a task to delete.")
            return
        notify_delete_strategy = NotifyDeleteStrategy()

        self.invoker.set_command(DeleteTaskCommand(self, selected_task_index))
        command = self.invoker.execute_command()
        context = Context(notify_delete_strategy)
        context.execute_strategy(command)

    
    

if __name__ == '__main__':
    app = ToDoApp()

    app.mainloop()
