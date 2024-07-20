hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# creating a variable total_price
total_price = 0

# looping through prices and adding them to total_price
for price in prices:
  total_price += price

# printing the total_price
print(total_price)

# creating a variable average_price that is the total price divided by the number of prices
average_price = total_price / len(prices)

# checking average_price
print('Average Haircut Price: ', average_price)

new_prices = [price - 5 for price in prices]
# checking new_prices
print(new_prices)

# creating a new variable total_revenue
total_revenue = 0
# making a for loop to create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  # adding the product of prices[i] (the price of the haircut at index position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue
  total_revenue += prices[i] * last_week[i]

# printing results of total_revenue
print('Total Revenue: ', total_revenue)

# finding the average daily revenue by dividing total_revenue by 7
average_revenue = total_revenue / 7
print('Average Daily Revenue: ', average_revenue)

# creating a comprehension list cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)