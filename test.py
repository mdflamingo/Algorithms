alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')

for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + smeshenie
    if i in alfavit:
        itog += alfavit[new_mesto]
    else:
        itog += i

print(itog)
