import random
import os


def main():


    n = random.randint(0,20)

    items = ["Cheese",4,1,"Orange",6,"Muppets","Frankenstein",3,2,"Orangutan",5,
    "Club","Sneeze",9,7,"Great",8,"Mate","Higher","Fast",10]

    print("amount in list is " + str(n)+ '\n')

    with open("list.txt",'a+') as f:
        for i in range(n):
            n = random.randint(0,20)
            print("List position is " + str(n) + '\n')

            f.write(str(items[n]) + "\n")


        f.seek(0)
        read_data = f.read()
        print(read_data)


def file_clear():

    with open("list.txt",'r+') as f:
        f.truncate(0)


def file_delete():

    os.remove("list.txt")


main()
#file_clear()
#file_delete()
