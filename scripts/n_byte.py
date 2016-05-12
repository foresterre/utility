import sys

def n_bytes(amount=1, file="n.bin",  byte=0x0):
    try:
        with open(file, 'wb') as f:
            f.write(bytes([byte] * amount))
    except Exception as e:
        invalid_exception_thrown(e)


def execute_as_message():
    print("Execute as: py -3 n_byte.py [amount (int)] [filename (str)]")


def invalid_argc():
    print("Arguments required: 2 or 3, given: ", args, "\nInput was:", " ".join(sys.argv))
    execute_as_message()
    exit(2)

def invalid_arg2_type():
    print("Amount argument has to be decimal.")
    execute_as_message()
    exit(3)

def invalid_exception_thrown(e):
    print("An unknown error occurred, message (if any):", str(e))
    exit(4)

# starting point of application,
# handles arguments
if __name__ == '__main__':
    AMOUNT = 0
    FILENAME = "n.bytes"

    args = len(sys.argv)

    if args >= 2 and args <= 3:

        # check second argument
        arg2 = sys.argv[1]
        if str.isdecimal(arg2):
            AMOUNT = int(arg2)
        else:
            invalid_arg2_type()

        if args == 3:
            FILENAME = sys.argv[2]

    else:
        invalid_argc()

    # generate the amount of 0-bytes
    n_bytes(amount=AMOUNT, file=FILENAME)
