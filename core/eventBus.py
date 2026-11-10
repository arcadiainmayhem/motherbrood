


class EventBus():
    def __init__(self):
        self.listeners = {}



    def suscribe(self, name , fn):
        self.listeners.setdefault(name , []).append(fn)




    def emit(self,name, *args):
        for fn, in self.listeners.get(name , []):
            fn(*args)