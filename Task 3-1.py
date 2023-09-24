sum_za = 0
b = 0
while True:
    za = int(input("Зарплата сотрудника:"))
    sum_za += za
    b +=1
    if za == 0:
        b -= 1
        print(sum_za/b)
        break