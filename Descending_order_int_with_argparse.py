import argparse

parse = argparse.ArgumentParser()
parser.add_argument('numbers', type = int, nargs='+')


num = input("please enter a number: ")
num_list = num
print(num_list)
num_list= [int(item) for item in num_list]
num_list.sort(key=int, reverse=True)
print("num_list : ", num_list)
