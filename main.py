def first():
    try:
        num = int(input('Введите число, которое хотите поделить на 3: '))
    except ValueError:
        print('Вы ввели не число')
    else:
        if num % 3 == 0:
            print(f'Число {num} делится на три')
        else:
            print('Число не делится на 3')


def second():
    try:
        num = int(input('Введите число, на которое хотите поделить число 100: '))
        result = 100 / num
    except ValueError:
        print('Вы ввели не число')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    else:
        if num > 100:
            print('Введено число большее, чем 100')
        else:
            print(f'100 можно поделить на {num}, результат равен {result}')


def third():
    date = input('Введите дату, разделённую точкой: ').split('.')
    if int(date[2]) % 100 == int(date[0]) * int(date[1]):
        print('Дата является магической!')
    else:
        print('Дата не является магической')


def fourth():
    ticket = input('Введите номер билета: ')
    symbols_ticket = list(ticket)
    amount1 = 0
    amount2 = 0

    if len(ticket) % 2 != 0:
        print('Вы ввели билет, в котором нечётное количество цифр')
    else:
        for i in symbols_ticket[0:int(len(symbols_ticket) // 2)]:
            amount1 += int(i)
        for j in symbols_ticket[int(len(symbols_ticket) // 2): int(len(symbols_ticket)) + 1]:
            amount2 += int(j)
        if amount1 == amount2:
            print('Билет счастливый!')
        else:
            print('Билет не счастливый')
