from abc import ABC , abstractmethod


# class Engine:
#     pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)



class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achivement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achivement):
        self.achievements.add(achivement['title'])

class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achivement):
        if achivement not in self.achievements:
            self.achievements.append(achivement)
