f = open("numbers.txt", "r")
sum = 0

for line in f:

    
    number = int(line)
    sum += number
    print (f"Total is {sum}")

f.close()