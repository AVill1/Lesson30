
def third():
    #print("hello!")
    try:
        print("begin third")
        n = int(input("INPUT NUMBER: "))
        if n == 1:
            5/0
        elif n == 2:
            int("hello")  # ValueError
        else:
           # a + b         # NameError
            raise NameError(1,2,3,4,5,6,"fghhjk","iopiop")
        print("hello")
    except (ZeroDivisionError, ValueError, NameError) as exc:
        print("exception  was handled:")
        print(exc)
        print(repr(exc))
        print(exc.args[1])


    # except ValueError:
    #     print("exception ValueError was handled...")
    #
    # except NameError:
    #     print("exception NameError was handled...")
    a + b
    print("end third")

def second():
    print("begin second")
    third()
    print("end second")

def first():
    print("begin first")
    second()
    print("end first")


def main():
    print("begin main")
    first()
    print("end main")

main()