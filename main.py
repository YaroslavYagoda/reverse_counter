schet = input('Введите положительное целое число: ')
try:
    schet = int(schet)
except ValueError:
    print('Неверный формат числа!')
    exit()

while schet >= 0:
    print(schet)
    schet -= 1
