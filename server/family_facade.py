from family import *


class FamilyFacade:
    '''управляет семьей'''

    def __init__(self, family_: Family):
        self._family = family_
        self._sources = []  # список источников дохода/расхода

    @property
    def family(self):
        '''получаем семью'''
        return self._family

    ###################################
    def get_all_members(self):
        '''получаем всех членов семьи'''
        return self.family.get_all_members()

    def get_children(self):
        '''получаем детей'''
        return self.family.get_children()

    def get_adult(self):
        '''получаем взрослых'''
        return self.family.get_adult()

    def add_member(self, name, patronymic, surname, birthdate):
        '''добавляем нового члена'''
        new_member = FamilyMember(name=name, patronymic=patronymic, surname=surname, birthdate=birthdate)
        self.family.add_member(new_member)

    ###################################
    @property
    def sources(self):
        return self._sources

    def get_source(self, name):
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
        return self.family.budget

