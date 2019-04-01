from datetime import datetime, timedelta
from .base import SingletonMeta


class FamilyMember:

    def __init__(self, name, patronymic, surname, birthdate):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.birthdate = birthdate

    @property
    def is_child(self):
        pass

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'


# используется всегда только один экземпляр бюджета
class FamilyBudget(metaclass=SingletonMeta):
    __amount = 0

    @property
    def get(self):
        return self.__amount

    def add(self, amount: (int, float)):
        self.__amount += amount

    def remove(self, amount: (int, float)):
        self.__amount -= amount


# используется всегда одна семья
class Family(metaclass=SingletonMeta):
    __family_members = []
    __family_budget = None

    def __init__(self, family_budget: FamilyBudget):
        self.__family_budget = family_budget  # композиция

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

    def get_budget(self):
        return self.__family_budget.get

    def add_to_budget(self, amount: (int, float)):
        self.__family_budget.add(amount)

    def get_from_budget(self, amount: (int, float)):
        self.__family_budget.remove(amount)
