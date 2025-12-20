import numpy

item_prices = [540, 120, 670, 920, 110]
discounted_prices = []

# how to apply 10% discount to all items
for price in item_prices:
    discounted_prices.append(price * .9)
    
print(discounted_prices)

np_item_prices = numpy.array(item_prices)

np_discounted_prices = np_item_prices * .9

print("item_prices:",np_item_prices)
print("discounted_prices: ",np_discounted_prices)

print(f"First price: {np_item_prices[0]}")

print(np_discounted_prices[np_discounted_prices>500])