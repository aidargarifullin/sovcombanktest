# расчет процентных долей для долевого строительства
import random


def calculate_percentages(n, *args):

    assert n == len(args), "Число долей должно совпадать"

    total = sum(args)

    # Вычисление процентов для каждой доли
    percentages = [(fraction / total) for fraction in args]

    # Вывод результатов с точностью до трех знаков после запятой
    for percentage in percentages:
        print(f"{percentage:.3f}")


if __name__ == '__main__':

    length = int(input("Введите количество случайных величин для проверки "))

    test_values = [round(random.uniform(1, 10), 1) for _ in range(length)]

    print('Запускаю функцию для следующего набора значений: ' + ", ".join(f"{value}" for value in test_values))

    calculate_percentages(len(test_values), *test_values)
