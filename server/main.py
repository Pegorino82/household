from family import FamilyMember, Family, \
    BudgetIncomes, BudgetOutcomes, BudgetIncomeItem, BudgetOutcomeItem

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

    print(family)

    in_ = BudgetIncomeItem('Job', 500, is_regular=True)
    income = BudgetIncomes(father, in_)
    family.add_to_budget(income)

    out = BudgetOutcomeItem('Shop', 20)
    outcome = BudgetOutcomes(mother, out)
    family.remove_from_budget(outcome)

    print(family)
