from .utils import calculate_age
from .base import BudgetIncomes, BudgetOutcomes, BudgetIncomeItem, BudgetOutcomeItem


class FamilyMember:
    __shift_age = 21  # возраст, с которого считаем, что человек взрослый

    def __init__(self, name, patronymic, surname, birthdate):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.birthdate = birthdate  # "%Y-%m-%d" or datetime

    @property
    def is_child(self):
        return calculate_age(born=self.birthdate) < self.__shift_age

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'


class FamilyBudget:
    __amount = 0
    __incomes = []  # композиция
    __outcomes = []  # композиция

    @property
    def get(self):
        '''
        получаем текущее состояние бюджета
        :return:
        '''
        return self.__amount

    @property
    def get_incomes(self):
        '''
        поступления
        :return:
        '''
        return self.__incomes

    @property
    def get_outcomes(self):
        '''
        расходы
        :return:
        '''
        return self.__outcomes

    def add(self, item: BudgetIncomes):
        self.__incomes.append(item)  # композиция
        self.__amount += item.item.amount()

    def remove(self, item: BudgetOutcomes):
        self.__outcomes.append(item)  # композиция
        self.__amount -= item.item.amount()


class Family:
    __family_members = []
    __family_budget = None

    def __init__(self):
        self.__family_budget = FamilyBudget()  # композиция

    def __str__(self):
        return f'members count: {len(self.get_all_members())}, budget: {self.get_budget()}'

    def add_member(self, family_member: FamilyMember):
        self.__family_members.append(family_member)

    def remove_member(self):
        pass

    def get_by_name(self, name):
        return list(map(lambda x: x.name == name, self.__family_members)) or None

    def get_all_members(self):
        return self.__family_members

    def get_children(self):
        pass

    def get_adult(self):
        pass

    def get_budget(self):
        return self.__family_budget.get

    def add_to_budget(self, item):
        self.__family_budget.add(item)

    def remove_from_budget(self, item):
        self.__family_budget.remove(item)
