from abc import ABC, abstractmethod


class TaskObserver(ABC):
    @abstractmethod
    def update(message):
        ...


class concreteObserver(TaskObserver):
    def update(message):
        print(f'{message}')
