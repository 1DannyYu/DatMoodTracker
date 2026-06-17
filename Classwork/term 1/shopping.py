# items = input("What do you need to buy? ")

# items_list = items.split()
# print(items_list)

msg = input("secret message: ")
scramble = input("scramble input: ")
list = msg.split(scramble)
print(''.join(list))
