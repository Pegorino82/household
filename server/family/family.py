from .utils import calculate_age
from .base import BudgetAction
from observer import Subject

from functools import reduce


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

    def __repr__(self):
        return f'{self.name} {self.patronymic} {self.surname}'


class FamilyBudget:
    __amount = 0
    __incomes = []  # композиция
    __outcomes = []  # композиция

    def __str__(self):
        incomes = reduce(lambda x, y: x.item.amount + y.item.amount, self.get_incomes) if self.get_incomes else []
        outcomes = reduce(lambda x, y: x.item.amount + y.item.amount, self.get_outcomes) if self.get_outcomes else []
        return f'{self.get} incomes: {incomes}, outcomes: {outcomes}'

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

    def add(self, item: BudgetAction):
        if item.item.is_income:
            self.__incomes.append(item)  # композиция
            self.__amount += item.item.amount
        else:
            self.__outcomes.append(item)  # композиция
            self.__amount -= item.item.amount


class Family(Subject):
    __family_members = []
    __family_budget = None

    def __init__(self):
        __class__.__family_budget = FamilyBudget()  # композиция
        super().__init__()

    def __str__(self):
        return f'members count: {len(self.get_all_members())}, budget: {self.get_budget()}'

    def __repr__(self):
        return f'family'

    def add_member(self, family_member: FamilyMember):
        self.__family_members.append(family_member)

    def remove_member(self):
        pass

    def get_by_name(self, name):
        result = []
        for member in self.get_all_members():
            if member.name == name:
                result.append(member)
        return result

    def get_all_members(self):
        return self.__family_members

    def get_children(self):
        result = []
        for member in self.get_all_members():
            if member.is_child:
                result.append(member)
        return result

    def get_adult(self):
        result = []
        for member in self.get_all_members():
            if not member.is_child:
                result.append(member)
        return result

    @property
    def budget(self):
        return self.__family_budget

    def get_budget(self):
        return self.__family_budget.get

    def get_budget_incomes(self):
        return self.__family_budget.get_incomes

    def get_budget_outcomes(self):
        return self.__family_budget.get_outcomes

    def add_to_budget(self, item):
        self.__family_budget.add(item)
        self._subject_state = item, self.get_adult()  # передаем действие с бюджетом и список взрослых членов семьи
        self._notify()
