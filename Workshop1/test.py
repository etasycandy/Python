def top() :
    print("  ______  ")
    print(" /      \\")
    print("/        \\")

def bottom() :
    print("\\        /")
    print(" \\______/")

def line() :
    print("+--------+")

def egg() :
    top()
    bottom()
    print()

def cup() :
    bottom()
    line()
    print()

def stop() :
    top()
    print("|  STOP  |")
    bottom()
    print()

def hat() :
    top()
    line()
    print()


# main
print("Hoàng xếp hình")
egg()
cup()
stop()
hat()