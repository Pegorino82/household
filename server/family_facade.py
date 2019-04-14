from family import *


class FamilyFacade:
    '''управляет семьей'''

    def __init__(self, family_: Family):
        self.__family = family_
        self._sources = []  # список источников дохода/расхода
        self.action_builder = BudgetActionBuilder()

    @property
    def actions(self):
        return self._family.budget.get_incomes

    @property
    def _family(self):
        '''получаем семью'''
        return self.__family

    ###################################
    def get_all_members(self):
        '''получаем всех членов семьи'''
        return self._family.get_all_members()

    def get_children(self):
        '''получаем детей'''
        return self._family.get_children()

    def get_adult(self):
        '''получаем взрослых'''
        return self._family.get_adult()

    def add_member(self, name, patronymic, surname, birthdate):
        '''добавляем нового члена'''
        new_member = FamilyMember(name=name, patronymic=patronymic, surname=surname, birthdate=birthdate)
        self._family.add_member(new_member)

    ###################################
    @property
    def sources(self):
        '''возвращает все источники которые использовались в семье'''
        return self._sources

    def get_source(self, name):
        '''возвращает все источники с именем'''
        result = []
        for source in self.sources:
            if source.name == name:
                result.append(source)
        return result

    def _is_source_exists(self, name, is_regular):
        '''
        проверяет существование источника дохода/расхода
        :param name:
        :param is_regular:
        :return: источник если существует иначе False
        '''
        for s in self.sources:
            if s.name == name and s.is_regular == is_regular:
                return s
            return False

    def add_source(self, name, is_regular=True):
        '''
        :param name:
        :param is_regular:
        :return: созданный источник или существующий
        '''
        if not self._is_source_exists(name, is_regular):
            new_source = Source(name=name, is_regular=is_regular)
            self._sources.append(new_source)
            return new_source
        return self._is_source_exists(name, is_regular)

    #################################
    def budget(self):
        return self._family.budget

    def add_to_budget(self, action, amount, family_member: FamilyMember, source: Source):
        new_action = self.action_builder.create_budget_action(action, amount, family_member, source)
        self._family.add_to_budget(new_action)

    def get_budget(self):
        return self._family.get_budget()

    def get_budget_incomes(self):
        return self._family.get_budget_incomes()

    def get_budget_outcomes(self):
        return self._family.get_budget_outcomes()


if __name__ == '__main__':
    family = Family()
    facade = FamilyFacade(family)

    # создаем членов семьи
    facade.add_member('Jack', 'D', 'Black', '1980-05-15')
    facade.add_member('Mary', 'C', 'Black', '1984-10-01')
    facade.add_member('Kate', 'M', 'Black', '2005-07-20')
    facade.add_member('Poll', 'D', 'Black', '2015-09-15')

    # создаем источники
    fathers_job = facade.add_source("Father's job")
    fathers_freelance = facade.add_source("Father's freelance", is_regular=False)
    mothers_job = facade.add_source("Mothers's job")
    near_home_shop = facade.add_source("Near home shop")
    far_from_home_shop = facade.add_source("Far from home shop", is_regular=False)
    children_shop = facade.add_source("Children shop", is_regular=False)

    print(facade.get_adult())
    print(facade.get_children())
    print(facade.sources)
    # производим действие с бюджетом
    facade.add_to_budget('поступление', 50000, facade.get_adult()[0], fathers_job)
    facade.add_to_budget('поступление', 40000, facade.get_adult()[1], mothers_job)
    print(facade.get_budget_incomes())
    print(facade.budget())

