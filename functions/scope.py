print(__name__) # builtin scope

__name__ = "max" # global

def outer():
    __name__ = "isuru" # enclose
    print(__name__)

    def inner():
        __name__ = "john" # local
        print(__name__)

    inner()

outer()
print(__name__)