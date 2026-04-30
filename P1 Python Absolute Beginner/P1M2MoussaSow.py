
def fishstore(fish, price):
    return f"Fish Type: {fish} costs ${price}"
fish_entry = input("Enter fish type: ")
price_entry = input("Enter price: ")
print(f"Report for Moussa Sow. {fishstore(fish_entry, price_entry)}")