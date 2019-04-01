from family import FamilyBudget, Family

if __name__ == '__main__':
    b = FamilyBudget()
    f = Family(family_budget=b)
    f.add_to_budget(5000)
    print(f)
