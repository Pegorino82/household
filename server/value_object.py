from inspect import getfullargspec


class CannotBeChangeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__('You cannot change values, create a new one')


class ValueObject(object):
    '''базовый для ValueObject,
    определяет свойства, переданные в конструктор;
    запрещает устанавливать новые свойства;
    реализует интерфейс для равенства / неравентства экземпляров класса (по словарю)'''

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        # print(f'from Eq >> {getfullargspec(self.__init__)}')
        # print(f'from Eq >> {args, kwargs}')
        cls_props = getfullargspec(self.__init__)[0][1:]
        if args:
            for i, arg in enumerate(args):
                self.__dict__.update({cls_props[i]: arg})
        if kwargs:
            for key, val in kwargs.items():
                self.__dict__.update({key: val})
        return self

    def __setattr__(self, name, value):
        raise CannotBeChangeException

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__


class BudgetActionValueObject(ValueObject):
    '''Дополнительно реализут механизм сравнения BudgetAction по BudgetItem (по сумме поступления -
         болше, больше или равно, меньше, меньше или равно)'''

    def __gt__(self, other):
        return self.item > other.item

    def __ge__(self, other):
        return self.item >= other.item

    def __lt__(self, other):
        return self.item < other.item

    def __le__(self, other):
        return self.item <= other.item


if __name__ == '__main__':
    class T(ValueObject):

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
