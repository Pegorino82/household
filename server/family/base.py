import abc


class AbstractBudgetItem(abc.ABC):
    '''
    (например организация - работодатель, или для расходов конкретная заправка,
    конкретный магазин)
    контролирует наличие у источника дохода/цели расходования:
    - названия,
    - постоянный источник дохода/цель расходования или нет,
    ... в процессе добавить требования
    '''

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def is_regular(self):
        pass


class BudgetItem(AbstractBudgetItem):
    def __init__(self, name, amount, is_regular=False):
        '''
        :param name: источник дохода/цель расходования
        :param amount: размер поступления/расхода
        :param is_regular: посоянный доход/расход
        '''
        self._name = name
        self._amount = amount
        self._is_regular = is_regular

    def get_name(self):
        return self._name

    def is_regular(self):
        return self._is_regular

    def amount(self):
        return self._amount


class BudgetIncomeItem(BudgetItem):
    '''
    источник поступления в бюджет (например зар. плата, выигрыш ...)
    '''

    def __init__(self, source, amount: float, is_regular=False):
        super().__init__(name=source, amount=amount, is_regular=is_regular)

    def __str__(self):
        return f'{self.name} -> {self.amount}'


class BudgetOutcomeItem(BudgetItem):
    '''
    цель расходования (например питание, услуги ...)
    '''

    def __init__(self, target, amount: float, is_regular=False):
        super().__init__(name=target, amount=amount, is_regular=is_regular)

    def __str__(self):
        return f'{self.name} <- {self.amount}'


class BudgetIncomes:
    '''
    описывает кто принес поступления в бюджет
    '''

    def __init__(self, source, budget_income_item: BudgetIncomeItem):
        self.source = source  # член семьи или кто-то не из семьи (возможно придется придумать адаптер)
        self.item = budget_income_item


class BudgetOutcomes:
    '''
    описывает на что (кого) потратили
    '''

    def __init__(self, source, budget_outcome_item: BudgetOutcomeItem):
        self.source = source  # на кого-то из семьи, на всю семью или вне семьи (возможно придется придумать адаптер)
        self.item = budget_outcome_item


class BudgetItemFactory:
    '''фабричный метод для создания статьи бюджета (поступления/расходы)'''
    INCOME = 'поступление'
    OUTCOME = 'расход'
    DEFAULT = ''

    def create_budget_item(self, action, source, amount):
        '''
        создает статью бюджета
        :param action: поступление или расход
        :param source: источник (пока название)
        :param amount:
        :return:
        '''
        if action == self.INCOME:
            item = BudgetIncomeItem(source, amount)
        elif action == self.OUTCOME:
            item = BudgetOutcomeItem(source, amount)
        else:
            item = BudgetItem(source, amount)
        return item
