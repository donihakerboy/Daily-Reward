from abc import ABC, abstractmethod
from observer import concreteObserver
from decorator import ShowMessageBoxDecorator


class Strategy(ABC):
    def __init__(self):
        self._observers = [concreteObserver, ]

    @abstractmethod
    def execute(self, task_name) -> None:
        pass


class NotifyTaskAddStrategy(Strategy):
    def execute(self, task_name) -> None:
        message = f"New task added: {task_name}"
        for observer in self._observers:
            observer = ShowMessageBoxDecorator(observer)
            observer.update(message)


class NotifyDeleteStrategy(Strategy):
    def execute(self, task_name) -> None:
        message = f"Task {task_name} deleted"
        for observer in self._observers:
            observer = ShowMessageBoxDecorator(observer)
            observer.update(message)


class NotifyEndStrategy(Strategy):
    def execute(self, task_name) -> None:
        message = f"Task {task_name} ended"
        for observer in self._observers:
            observer = ShowMessageBoxDecorator(observer)
            observer.update(message)


class Context:
    def __init__(self, strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, task_name) -> None:
        self._strategy.execute(task_name)
