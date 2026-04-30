total = 0
items = ""

def adding_report(report="T"):
    global total
    global items

    total = 0
    items = ""

    print('Input an integer to add to the total or "Q" to quit')

    while True:
        entry = input('Enter an integer or "Q": ')

        if entry.isdigit():
            total = total + int(entry)

            if report == "A":
                items = items + entry + "\n"

        elif entry.upper().startswith("Q"):
            if report == "A":
                print()
                print("Items")
                print(items)
                print("Total")
                print(total)
                print("Calculated by: Moussa Sow")
            else:
                print()
                print("Total")
                print(total)
                print("Calculated by: Moussa Sow")
            break

        else:
            print(entry + " is invalid input")

adding_report("A")
adding_report("T")