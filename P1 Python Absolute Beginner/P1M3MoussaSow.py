# create function, call and test

def cheese_order(max_order=110, min_order=1, price=7.99, order_amount=0):
    # cast to numbers (order_amount comes in as string from input)
    order_amount = float(order_amount)
    max_order = float(max_order)
    min_order = float(min_order)
    price = float(price)

    if order_amount > max_order:
        print(f"{order_amount} is more than currently available stock")
    elif order_amount < min_order:
        print(f"{order_amount} is below minimum order amount")
    else:
        total = order_amount * price
        print(f"{order_amount} costs ${total:.2f}")

order = input("Moussa Sow, enter cheese order weight (numeric value): ")
cheese_order(order_amount=order)