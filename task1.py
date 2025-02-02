import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = [{} for _ in range(amount + 1)]
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = used_coins[i - coin].copy()
                used_coins[i][coin] = used_coins[i].get(coin, 0) + 1
    
    return used_coins[amount] if dp[amount] != float('inf') else {}

# Тest
amount = 113
start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print("Жадібний алгоритм:", greedy_result, "Час виконання:", greedy_time)
print("Динамічне програмування:", dp_result, "Час виконання:", dp_time)
