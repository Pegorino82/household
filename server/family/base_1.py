import abc


class AbstractSource(abc.ABC):
    '''
    (например организация - постоянный работодатель, фриланс..., или для расходов - заправка, магазин...)
    контролирует наличие у источника дохода/цели расходования:
    - названия
    '''

    @abc.abstractmethod
    def name(self):
        pass


class Source(AbstractSource):
    '''абстрактный источник дохода/расхода'''

    def __init__(self, name, is_regular=False):
        '''
        :param name: источник дохода/цель расходования
        :param is_regular: посоянный доход/расход
        '''
        self._name = name
        self._is_regular = is_regular

    def name(self):
        return self._name

    def is_regular(self):
        return self._is_regular


class BudgetItem:
    '''
    источник поступления в бюджет/цель расходования
    '''

    def __init__(self, source: Source, amount: float, is_income=True):
        self.source = source  # композиция
        self.amount = amount if self.is_income else amount * -1
        self._is_income = is_income

    def is_income(self):
        return self._is_income

    def __str__(self):
        return f'{self.source.name} -> {self.amount}' if self.is_income() else f'{self.source.name} <- {self.amount}'


class BudgetAction:
    '''
    описывает на кого/что были расходованы средства, кто произвел пополнения в бюджет
    '''

    def __init__(self, family_member, budget_item: BudgetItem):
        self.family_member = family_member  # член семьи или кто-то не из семьи (возможно придется придумать адаптер)
        self.item = budget_item


class BudgetItemFactory:
    '''фабричный метод для создания статьи бюджета (поступления/расходы)'''
    INCOME = 'поступление'
    OUTCOME = 'расход'

    def create_budget_item(self, action, amount, source: Source):
        '''
        создает статью бюджета
        :param action: поступление или расход
        :param source: источник/цель
        :param amount: сумма
        :return:
        '''
        item = None
        if action == self.INCOME:
            item = BudgetItem(source, amount, is_income=True)
        elif action == self.OUTCOME:
            item = BudgetItem(source, amount, is_income=False)

        return item