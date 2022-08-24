from play_utils.play import *

while True:
    i = input("How many pencils would you like to use:")
    try:
        n = int(i)
        if n > 0:
            break
        elif n == 0:
            print("The number of pencils should be positive")
        else:
            print("The number of pencils should be numeric")
    except:
        print("The number of pencils should be numeric")

while True:
    first = input("Who will be the first (John, Jack):")
    if first == "Jack" or first == "John":
        break
    print("Choose between John and Jack")

if first == "John":
    play_second(n)
else:
    play_first(n)



