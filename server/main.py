from pprint import pprint
from family import FamilyMember, Family, \
    Source, BudgetActionBuilder
from observer import ConsoleSender

if __name__ == '__main__':
    # создали членов семьи
    father = FamilyMember('John', 'D', 'Black', '1962-12-30')
    mother = FamilyMember('Mary', 'D', 'Black', '1970-1-15')
    son = FamilyMember('Jack', 'J', 'Black', '2000-7-15')
    # print(son.is_child)

    # создали семью и добавили членов семьи
    family = Family()
    family.attach(ConsoleSender())  # добавляем наблюдателя за бюджетом
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
    builder = BudgetActionBuilder()
    in_1 = builder.create_budget_action(builder.INCOME, 50000, father, fathers_job)
    in_2 = builder.create_budget_action(builder.INCOME, 45000, mother, mothers_job)
    in_3 = builder.create_budget_action(builder.INCOME, 10000, father, fathers_freelance)
    out_1 = builder.create_budget_action(builder.OUTCOME, 2000, son, children_shop)
    out_2 = builder.create_budget_action(builder.OUTCOME, 500, family, near_home_shop)

    # добавляем в семью
    family.add_to_budget(in_1)
    family.add_to_budget(in_2)
    family.add_to_budget(out_1)
    family.add_to_budget(out_2)
    family.add_to_budget(in_3)

    print('Семья >>', family)
    print('Дети >>', family.get_children())
    print('Взрослые >>', family.get_adult())
    print('Получили по имени >>', family.get_by_name('John'))
    print('расходы >>', family.get_budget_outcomes())
    print('поступления >>', family.get_budget_incomes())

    family.add_to_budget(out_2)
    print('Семья >>', family)

    print(out_2 != out_1)
    print(out_2 > out_1)
    print(out_2 < out_1)

    # pprint(family.__class__.__dict__)
    # pprint(family.__dict__)
