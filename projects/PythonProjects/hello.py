# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200

# #////////////////////

# def grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 50:
#         return "C"
#     return "Fail"

# print(grade(82))  

# # /////////////////

# def can_buy_item(balance, price):
#     if balance < 0 or price < 0:
#         return "Invalid amount"
#     if balance >= price:
#         return "Purchase approved"
#     return "Insufficient balance"

# print(can_buy_item(1200,1000))

# //////////////

# def calculate_price(price):

#     if price >= 2000:
#         return price * 0.20

#     else :
#         return price * 0.10

# print(calculate_price(2100))
# print(calculate_price(876))
# ///////////////////////////////
#  Return "Free delivery" if order is 500 or more.
#  Otherwise return "Delivery charge: 50"
# def delivery_status(order_amount):

#     if order_amount >= 500:
#         return "free delivery"

#     else:
#         return "Delivery charge : 50"

# print(delivery_status(999))
# print(delivery_status(87))
# print(delivery_status(400))
