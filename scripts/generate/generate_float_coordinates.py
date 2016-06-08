import sys
import random
import math

def main():
    """
    Generates some random coordinates.
    Each coordinate contains a X-axis and Y-axis floating point number (like in a 2D euclidean plane).
    Only one of each X and Y (in range(min, max)) coordinates can exist.

    Execute with: py -3 generate_float_coordinates.py [coordinates amount]

    There are two sets, set1, set2.
    The [coordinates amount] stands for the amount of numbers which will be generated for each set.
    Each number is added to the set.

    Then the size of both sets is taken, because there could have been generated one or more duplicates. These are only once available in the set (because of the properties of a set). Thus only the minimum size of the two sets is taken, let's say m.

    Both sets then are m times pop'ed. The value each pop returns then is processed. Currently only printing to the stdout (print()) in a csv format and writing to a file is supported.

    If written to a file:
    [amount]
    [x_i] [y_i]
    [x_i] [y_i]
    ... and so on.

    If printed:
    [x_i], [y_i]
    [x_i], [y_i]
    ... and so on.


    :author: Foresterre
    """
    name = "random.in"
    mini = 0.0000000000000000 # min inclusive
    maxe = 1.0000000000000001 # max exclusive

   PRINT_COORDINATES = False

    # ugly argument handling
    print(sys.argv)
    if len(sys.argv) == 3:
        name = sys.argv[2]
        print("write to disk: ", sys.argv[2])
    elif len(sys.argv) == 4:
        mini = float(sys.argv[2])
        maxe = float(sys.argv[3])
    elif len(sys.argv) != 2 and len(sys.argv) != 3 and len(sys.argv) != 5:
        print("Error: Wrong arguments:\nUsage:\npython generate_float_coordinates.py [amount of coordinates]")
        sys.exit(-1)

    if not str.isdecimal(sys.argv[1]):
        print("Error: The first argument should be decimal.")
        sys.exit(-1)


    amount = int(sys.argv[1])
    print("try amount: ", amount)

    print("min: ", mini)
    print("max: ", maxe)
    if (mini > maxe):
        print("Error: The minimum input should be smaller compared to the maximum input")
        sys.exit(-2)

    set1 = set()
    set2 = set()

    for x in range(0, amount):
        f1 = random.uniform(mini, maxe)
        f2 = random.uniform(mini, maxe)

        set1.add(f1)
        set2.add(f2)

    l = min(len(set1), len(set2))

    print("set1: len = ", len(set1))
    print("set2: len = ", len(set2))

    print("result: len = ", l)

    # clear file, append amount
    with open(name, 'w') as f:
        f.write(str(l))
        f.write("\n")


    # append each pop'ed coordinates
    # as noted above, the file is opened or created either way,
    # whether it is print only or not.
    with open(name, 'a') as f:
        for i in range(0, l):
            item1 = str(set1.pop())
            item2 = str(set2.pop())

            if PRINT_COORDINATES:
                print(item1, end=", ")
                print(item2)

            f.write(item1)
            f.write(" ")
            f.write(item2)
            f.write("\n")




if __name__ == '__main__':
    main()
