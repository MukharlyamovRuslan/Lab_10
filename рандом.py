from random import randrange
import logging
# Настройка логгирования
logging.basicConfig(filename="Lab_10.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("Логи для теста")
# Ввод числа N пользователем и проверка на ошибку
while True:
    try:
        logging.info("Запрос числа N")
        N1 = input('Введите натуральное число N : ')
        N = int(N1)
        if N < 1:
            print('Ошибка!!! Вы ввели ненатуральное число')
            logging.error(f"Ошбика ввода N числа пользователем, пользователь ввел - {N}")
            continue
        logging.info(f"Число N введенное ползователем {N}")
        break
    except ValueError:
        print('Вы ввели что-то не то')
        logging.error(f"Ошбика ввода N числа пользователем, пользователь ввел - {N1}")
# Ввод числа k пользователем и проверка на ошибку
while True:
    try:
        logging.info("Запрос числа k")
        k1 = input('Введите натуральное число k: ')
        k = int(k1)
        if k < 1:
            print('Ошибка!!! Вы ввели ненатуральное число')
            logging.error(f"Ошбика ввода k числа пользователем, пользователь ввел - {k}")
            continue
        logging.info(f"Число k введенное ползователем {k}")
        break
    except ValueError:
        print('Вы ввели что-то не то')
        logging.error(f"Ошбика ввода k числа пользователем, пользователь ввел - {k1}")
# Компьютер загадывате число
rand = randrange(1, N + 1)
logging.info(f"Число, которое компьютер загадал {rand}")
# Корректность диалога
nums_2_to_4 = [2, 3, 4]

if k % 100 >= 5 and k % 100 <= 20:
    print(f'У вас есть {k} попыток угадать число, которое я загадал')
elif k % 10 == 1 or k % 100 == 1:
    print(f'У вас есть {k} попытка угадать число, которое я загадал')
elif k % 10 in nums_2_to_4 or k % 100 in nums_2_to_4:
    print(f'У вас есть {k} попытки угадать число, которое я загадал')
# Цикл угадывания и проверка на ошибку
count = 0
cc = 1
c = 1
# for i in range(1, k + 1):
while True:
    try:
        if cc > k:
            break
        logging.info("Запрос угадать число")
        ans1 = input(f'({cc} ' + f'попытка) Введите число от 1 до {N}: ')
        ans = int(ans1)
        while ans < 1 or ans > N:
            print(f'Ошибка!!! Введите число входящее в диапазон от 1 до {N}')
            logging.error(f"Ошбика ввода числа пользователем, пользователь ввел - {ans}")
            ans = int(input(f'({cc} ' + f'попытка) Введите число от 1 до {N}: '))
        logging.info(f"{cc} " + "попытка - " + f"{ans}")
        if ans == rand:
            print('Правильно')
            logging.info(f"Ответ на {cc} попытку - Правильно")
            count += 1
            cc += 1
            break
        elif ans < rand:
            bigger = 'Неверно, загаданное число больше'
            print(bigger)
            logging.info(f"Ответ на {cc} попытку - {bigger}")
            cc += 1
            c += 1
        elif ans > rand:
            smaller = 'Неверно, загаданное число меньше'
            print(smaller)
            logging.info(f"Ответ на {cc} попытку - {smaller}")
            cc += 1
            c += 1
    except ValueError:
        print('Вы ввели что-то не то')
        logging.error(f"Ошбика ввода числа пользователем, пользователь ввел - {ans1}")
        c = cc
# Финальное сообщение
if count == 1:
    print(f'Вы угадали с {cc - 1} попытки')
elif count == 0:
    print('Попытки закончились')
logging.info("")