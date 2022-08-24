import sys


def get_input(p):
    while True:
        j = input()
        if j not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
        elif int(j) > p:
            print("Too many pencils were taken")
        else:
            return int(j)


def play_john(n):
    print("|" * n)
    print("John's turn!")
    n = n - get_input(n)
    if n == 0:
        print("Jack won!")
        sys.exit()
    return n


def play_jack(n):
    print("|" * n)
    print("Jack's turn:")
    if n % 4 == 1 or n % 4 == 2:
        print("1")
        n -= 1
    else:
        k = n % 4 - 1 if n % 4 - 1 > 0 else 3
        print(k)
        n -= k
    if n == 0:
        print("John won!")
        sys.exit()
    return n


def play_second(n):
    while True:
        n = play_john(n)
        n = play_jack(n)


def play_first(n):
    while True:
        n = play_jack(n)
        n = play_john(n)
