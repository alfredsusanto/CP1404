import random

MAX_INCREASE = 0.175	# 10%
MAX_DECREASE = 0.05	# 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0

price = INITIAL_PRICE

def format_currency(price):
    currency= "Starting price: $ {:.2f}".format(price)
    return currency
result = format_currency(price)
print(result)

def format_currency2(price,day):
    currency2= "On day {} price is: ${:,.2f}".format(day,price)
    return currency2

day=0

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    day = day + 1
    if random.randint(1, 2) == 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    result2 = format_currency2(price,day)
    print(result2)


