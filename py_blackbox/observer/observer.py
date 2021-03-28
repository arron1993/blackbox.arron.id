class Observer():
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observables = {}

    def attach(self, event_name, callback):
        self._observables[event_name] = callback
