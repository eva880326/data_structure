data = [73, 65, 52, 24, 83, 17, 35, 96, 41, 9]
def print_header():
    print("陣列     [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]")
    print("------------------------------------------------")
    print("排序前:", end="")
    for n in range(len(data)):
        print("%4d" % data[n], end="")
    print(" ")