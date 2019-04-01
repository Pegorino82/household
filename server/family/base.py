class SingletonMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        cls.__instance = None
        return type.__new__(cls, clsname, bases, clsdict)

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance
