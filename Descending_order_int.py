
num = input("please enter a number: ")
int(num)
def Descending_order(num):
    l = []
    if num >= 0:
        for number in num:
            l += number
        l.sort(reverse=True)
        print(l)
    else:
        print("Please enter numbers greater than 0")
