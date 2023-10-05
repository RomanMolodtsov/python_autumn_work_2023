str = input('Введите генетический код(А, Г, Ц, Т): ').upper()
def correct_str(str):
    print(str)
    str1 = str.replace('АГ', 'ГА')
    str2 = str1.replace('ЦТ', 'ЦАГТ')
    print(str2)
    return str2
correct_str(str)
