number = float(input("Enter a number: "))

if number < 0:
    print("Negative number - no square root")
else:
    square_root = number ** 0.5
    print(square_root)


print("What is the capital of Australia?")
answer = input("Enter your answer: ")

if answer == "Canberra":
    print("Well done, correct!")
else:
    print("Sorry, the answer is Canberra.")
