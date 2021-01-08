import random
def table():
    n=int(input("Enter the digit whose table you want to find "))
    wrong=random.randint(2,9)
    table=[i * n for i in range(1,11)]
    table1=[i * n for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,10)
    print(f"ROHAN DAS TABLE     :",table)
    print(f"ABHIRASHMI KI TABLE :",table1)
    for i in range(10):
        if table[i] != table1[i]:
            print("fault found at ",i+1,"rd/th position ")
            print("IT SHOULD BE :",table1[i],"insted of ",table[i])


if __name__ == '__main__':
    print(table())
