
def num_coins(cents):
    coins =[25, 10, 5, 1]
    num_of_coins= 0 
    for coin in coins:
        num_of_coins += cents//coin
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

print(num_coins(31))