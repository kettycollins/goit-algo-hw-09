def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    coins_used = {}

    for coin in denominations:
        num_coins, amount = divmod(amount, coin)
        if num_coins > 0:
            coins_used[coin] = num_coins

    return coins_used

def find_coins_dyn(amount):
    denominations = [1, 2, 5, 10, 25, 50]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coins_used = {}

    for i, coin in enumerate(denominations):
        for j in range(coin, amount + 1):
            if min_coins[j - coin] + 1 < min_coins[j]:
                min_coins[j] = min_coins[j - coin] + 1
                coins_used[j] = coin

    result = {}
    remaining_amount = amount

    while remaining_amount > 0:
        coin = coins_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result


import timeit

amount = 113

greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100000)
dynamic_time = timeit.timeit(lambda: find_coins_dyn(amount), number=100000)

greedy_results = find_coins_greedy(amount)
dynamic_results = find_coins_dyn(amount)

print(f"Результат жадібного алгоритму: {greedy_results}, час: {greedy_time}")
print(f"Результат динамічного програмування: {dynamic_results}, час: {dynamic_time}")
