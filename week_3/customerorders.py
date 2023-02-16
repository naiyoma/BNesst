orders = {}

with open("customer.txt", "r") as f:
    try:
        for line in f:
            name, number, numbers, items, count = line.strip().split(": ")
            customer = name.split(" ")[0] + " " + name.split(" ")[1]
            number = numbers.split(", ")[0]
            items = [int(x) for x in count.split(',')]
            items_dict = {}
            # import pdb; pdb.set_trace()
            for i in range(len(items)):
                items_dict["Item " + str(i+1)] = int(items[i])
            orders[int(number)] = {"Order Number": int(number), "Customer": customer, "Items": items_dict}
    except:
        pass

for order in orders.values():
    print(order)
