import random

MAX_INCREASE = 0.175	# 10%
MAX_DECREASE = 0.05	# 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))
day=0

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    day=day+1
    if random.randint(1, 2) == 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    print("On day",day,"price is: ${:,.2f}".format(price))