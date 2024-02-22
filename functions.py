def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Example usage:
# original_price = 300
# discount = 25  # 25% discount
    # To return the price if the discount is below 20%
original_price = 1000
discount = 15  # 15% discount
final_price = calculate_discount(original_price, discount)
print("Final Price after applying discount:", final_price)


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
if final_price == original_price:
    print("No discount applied. Original price:", final_price)
else:
    print("Final price after applying the discount:", final_price)



# def fn(a):
#     print(a)

# x = 90
# fn(x)

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)

# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)

# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)

# for num in range(1, 5):
#     print(num)

# def some_thing(number1, number2):
#     first_value = number1 + 8
#     second_value = number2 - 5
#     return first_value

# print(some_thing(13, 10))

# x = 0
# while x < 10:
#     x = x + 1



