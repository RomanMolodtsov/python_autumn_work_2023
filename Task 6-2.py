def books_of_two(str1, str2):
    books1 = set(str1.split(', '))
    books2 = set(str2.split(', '))
    res = books1 & books2
    print(books1, books2)
    return print(res)
books_of_two('Война и мир, Руслан и людмила, Путь', 'Путь, Муму, Капитанская дочка')