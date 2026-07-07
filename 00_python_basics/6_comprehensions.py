# Comprehensions

# List [exp for item in iterable if conditon]

menu = ["Masala Chai", "Iced Lemon Tea", "Green Tea", "Iced Peach Tea", "Ginger Tea"]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

###################################################################################################

# Set {exp for item in iterable if condition}

set = {1,2,3,4,5,6,7,8,9,10}

divisible_by_2 = [num for num in set if num%2 == 0]
print(divisible_by_2)

recipes = {
    "masala chai" : ["ginger", "cardamom", "clove"],
    "elaichi chai" : ["cardamom", "clove"]
}

unique_spices = {spices for ingredients in recipes.values() for spices in ingredients}
print(unique_spices)

###################################################################################################

# Dictionary {exp for item in iterable if condition}

tea_prices_inr = {
    "masala": 40,
    "green": 50,
    "lemon": 100
}
print(tea_prices_inr.items())

tea_prices_usd = {tea:(price/80) for tea, price in tea_prices_inr.items()}
print(tea_prices_usd.items())

###################################################################################################

# used only for saving memory

# Generator (exp for item in iterable if condition})
    # [x for x in items] => make entire list in memory
    # (x for x in items) => like a stream

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups_above_5 = sum((sale for sale in daily_sales if sale > 5))
print(total_cups_above_5)       # gives back generator object (must be consumed => ex: wrapped around sum)
