#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv)
    sum = 0
    for i in range(1, num):
        sum += int(argv[i])
    print("{}".format(sum))
