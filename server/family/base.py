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


# ? сделать его синглтоном с именем (как рассматривали пример на занятии с логерами)
class Source(AbstractSource):
    '''абстрактный источник дохода/расхода'''

    def __init__(self, name, is_regular=False):
        '''
        :param name: источник дохода/цель расходования
        :param is_regular: посоянный доход/расход
        '''
        self._name = name
        self._is_regular = is_regular

    @property
    def name(self):
        return self._name

    @property
    def is_regular(self):
        return self._is_regular

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class BudgetItem:
    '''
    источник поступления в бюджет/цель расходования
    '''

    def __init__(self, source: Source, amount: float, is_income=True):
        self.source = source  # композиция
        self.amount = amount if self.is_income else amount * -1
        self._is_income = is_income

    # @property
    def is_income(self):
        return self._is_income

    def __str__(self):
        return f'{self.source.name} -> {self.amount}' if self.is_income() else f'{self.source.name} <- {self.amount}'

    def __repr__(self):
        return f'{self.source.name} -> {self.amount}' if self.is_income() else f'{self.source.name} <- {self.amount}'


class BudgetAction:
    '''
    описывает на кого/что были расходованы средства, кто произвел пополнения в бюджет
    '''

    def __init__(self, family_member, budget_item: BudgetItem):
        self.family_member = family_member  # член семьи или кто-то не из семьи (возможно придется придумать адаптер)
        self.item = budget_item

    def __repr__(self):
        return f'{self.family_member} - {self.item}'

    def __str__(self):
        return f'{self.family_member} - {self.item}'


class BudgetActionBuilder:
    '''паттерн строитель'''
    INCOME = 'поступление'
    OUTCOME = 'расход'

    def create_budget_action(self, action, amount, family_member, source: Source):
        '''
        создает статью бюджета
        :param action: поступление или расход
        :param source: источник/цель
        :param family_member: член семьи
        :param amount: сумма
        :return:
        '''
        item = None
        if action == self.INCOME:
            item = BudgetItem(source, amount, is_income=True)
        elif action == self.OUTCOME:
            item = BudgetItem(source, amount, is_income=False)

        budget_action = BudgetAction(family_member, item)
        return budget_action
