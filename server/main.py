from family import FamilyMember, Family, \
    Source, BudgetItem, BudgetAction, BudgetActionFactory

if __name__ == '__main__':
    # создали членов семьи
    father = FamilyMember('John', 'D', 'Black', '1962-12-30')
    mother = FamilyMember('Mary', 'D', 'Black', '1970-1-15')
    son = FamilyMember('Jack', 'J', 'Black', '2000-7-15')
    # print(son.is_child)

    # создали семью и добавили членов семьи
    family = Family()
    family.add_member(father)
    family.add_member(mother)
    family.add_member(son)
    # print(family)

    # создаем источники доходов/расходов
    fathers_job = Source("Father's job")
    fathers_freelance = Source("Father's freelance", is_regular=False)
    mothers_job = Source("Mothers's job")
    near_home_shop = Source("Near home shop")
    far_from_home_shop = Source("Far from home shop", is_regular=False)
    children_shop = Source("Children shop", is_regular=False)

    # создаем действия с бюджетом
    factory = BudgetActionFactory()
    in_1 = factory.create_budget_action('поступление', 50000, father, fathers_job)
    in_2 = factory.create_budget_action('поступление', 45000, mother, mothers_job)
    out_1 = factory.create_budget_action('расход', 2000, son, children_shop)

    # добавляем в семью
    family.add_to_budget(in_1)
    family.add_to_budget(in_2)
    family.add_to_budget(out_1)


    print('Семья >>', family)
    print('Дети >>', family.get_children())
    print('Взрослые >>', family.get_adult())
    print('Получили по имени >>', family.get_by_name('John'))
