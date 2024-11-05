from typing import List, Tuple

# для конвертации стоимости бондов
BOND_PRICE_MULTIPLIER = 10


def calculate_bond_income(bond: Tuple[int, str, int, int]) -> float:
    start_day, name, price, quantity = bond
    redemption_price = 1000 * quantity
    coupon_income = 30 * quantity
    income = (redemption_price + coupon_income) - (price * BOND_PRICE_MULTIPLIER * quantity)
    return income


def max_profit_bonds(n: int, m: int, s: int, bonds: List[Tuple[int, str, int, int]]) -> List:
    # Рассчитаем доходность для каждого бонда и отсортируем по ней
    bonds_with_income = [(bond, calculate_bond_income(bond)) for bond in bonds]
    bonds_with_income.sort(key=lambda x: x[1], reverse=True)

    selected_bonds = []
    total_cost = 0

    total_income = 0

    # Подбор бондов в рамках бюджета
    for bond, income in bonds_with_income:
        start_day, name, price, quantity = bond

        if start_day <= n:
            cost = price * BOND_PRICE_MULTIPLIER * quantity

            max_lots = min(s // cost, m)  # Максимальное количество лотов, которое мы можем купить для этого бонда

            if max_lots > 0:
                selected_bonds.append(bond)
                total_cost += cost * max_lots
                s -= max_lots * cost
                total_income += income * max_lots

    return [total_income, selected_bonds]


if __name__ == '__main__':
    # Пример использования
    n = 2
    m = 2
    s = 8000
    bonds = [
        (1, 'alfa-05', 100.2, 2),
        (2, 'alfa-05', 101.5, 5),
        (2, 'gazprom-17', 100, 2),
    ]

    result = max_profit_bonds(n, m, s, bonds)

    print(result[0])
    for rec in result[1]:
        print(f'{rec}')
    print()
