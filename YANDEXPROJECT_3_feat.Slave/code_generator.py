from random import choice


def get_code():
    symbols = list('QWERTYUIOPASDFGHJKLZXCVBNM' + 'qwertyuiopasdfghjklzxcvbnm' + '1234567890')
    while True:
        code = ''
        for _ in range(20):
            code += choice(symbols)
        if True:  # проверка на повторение кода
            break
    return code

