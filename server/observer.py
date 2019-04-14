import abc


class Subject:
    def __init__(self):
        self._observers = set()  # наблюдатели
        # self._subject_state = None

    def attach(self, observer):
        '''добавляет наблюдателя'''
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        '''удаляет наблюдателя'''
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self, item, adults):
        '''оповещает'''
        for observer in self._observers:
            observer.changed(item, adults)


class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def changed(self, args):
        pass


class ConsoleSender(Observer):

    def changed(self, item, adults):
        '''оповещае взрослых об изменении бюджета'''
        for member in adults:
            if item.item.is_income:
                print(f'сообщение для {member}: пополнение на {item.item.amount}')
            else:
                print(f'сообщение для {member}: расход {item.item.amount}')


class SmsSender(Observer):

    def changed(self, args):
        pass
