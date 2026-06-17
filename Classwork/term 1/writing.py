# f = open("newFile.txt","w")

# f.write("This is some text\n")
# f.write("Even more text\n")
# f.write("You said more right !\n")
# f.write("\n")
# f.write("MORE!!!\n")

# f.close()

# f = open("MyFile.txt", "a")

# f.write("No this is insufferable!\n")
# f.write("just stop please!! \n")
# f.write("I'm going home... \n")

# f.close()

import os

if os.path.isfile("MyFile.txt"):
    f = open("MyFile.txt", "r")
    for line in f:
        print(line)
    f.close()
