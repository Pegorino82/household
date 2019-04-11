from inspect import getfullargspec


class CannotBeChangeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__('You cannot change values, create a new one')


class EqChecker(object):
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        # print(f'from Eq >> {getfullargspec(self.__init__)}')
        # print(f'from Eq >> {args, kwargs}')
        cls_props = getfullargspec(self.__init__)[0][1:]
        if args:
            for i, arg in enumerate(args):
                # setattr(self, cls_props[i], arg)
                self.__dict__.update({cls_props[i]: arg})
        if kwargs:
            for key, val in kwargs.items():
                # setattr(self, key, val)
                self.__dict__.update({key: val})
        return self

    def __setattr__(self, name, value):
        raise CannotBeChangeException

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__


if __name__ == '__main__':


    class T(EqChecker):

        def __init__(self, a, b):
            # self.a = a
            # self.b = b
            pass

        def __str__(self):
            return f'a: {self.a}; b: {self.b}'


    t = T('aaa', b='bbb')
    t1 = T(1, b=2)
    t3 = T(a='aaa', b='bbb')
    print(t)
    print(t1)
    print(t != t1)
    print(t == t3)
