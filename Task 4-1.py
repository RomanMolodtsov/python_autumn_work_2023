# Калькулятор
cal = input('Введите действие(например "4 * 4"): ').split()
if cal[1] == '+': print(int(cal[0])+int(cal[2]))
elif cal[1] == '-': print(int(cal[0])-int(cal[2]))
elif cal[1] == '*': print(int(cal[0])*int(cal[2]))
elif cal[1] == '/' and cal[2] != '0': print(int(cal[0])/int(cal[2]))
else: print('Error!')