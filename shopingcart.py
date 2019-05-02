item = [['iphone', 5800], ['mac', 12000], ['nikon', 22000], ['switch', 2300]]
shopping_cart = []
total_money = int(input("Enter your amount:"))
answer = ""
balance = ""
while answer != 'q':
    print("=".center(50, '='))
    for index, product_list in enumerate(item):
        print(index, product_list)
    print("=".center(50, '='))
    product_num = int(input("Enter the purchase product number:"))
    product = item[product_num]
    if total_money >= product[1]:
        shopping_cart.append(product)
        total_money -= product[1]
        balance = total_money
        print("Added \033[31;1m%s\033[0m into shopping cart,your current balance is \033[31;1m%s\033[0m" % (product[0], balance))
        answer = input('Whether to continue shopping? Any key continue; "q" exit:')
    else:
        exit("not sufficient funds")
else:
    print("Order as follows".center(50, '='))
    for order_list in shopping_cart:
        print(order_list)
    print("balance:\033[31;1m%s\033[0m" % balance)
    print("=".center(50, '='))
print("aaa")