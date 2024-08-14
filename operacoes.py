def soma(num):
    return num[0] + num[1], f'{num[0]} + {num[1]}'


def subtrai(num):
    return num[0] - num[1], f'{num[0]} - {num[1]}'

def multiplica(num):
    return num[0] * num[1], f'{num[0]} x {num[1]}'

def divisao(num):
    return num[0] / num[1], f'{num[0]} {chr(0x00F7)} {num[1]}'
