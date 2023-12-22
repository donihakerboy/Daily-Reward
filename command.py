from abc import ABC, abstractmethod
import tkinter as tk

class Command(ABC):
    
    @abstractmethod
    def execute(self) -> str:
        pass

class AddTaskCommand(Command):
    def __init__(self, app, task):
        self._app = app
        self._task = task

    def execute(self) -> str:
        self._app.listbox.insert(tk.END, self._task)
        self._app.tasks.append(self._task)
        return self._task

class DeleteTaskCommand(Command):
    def __init__(self, app, task_index):
        self._app = app
        self._task_index = task_index

    def execute(self) -> str:
        deleted_task = self._app.tasks.pop(self._task_index)
        self._app.listbox.delete(self._task_index)
        return deleted_task

class Invoker:
    _command = None

    def set_command(self, command: Command):
        self._command = command
        return self._command
    
    def execute_command(self) -> str:
        if isinstance(self._command, Command):
            return self._command.execute()
