def sayHello(fname, lname):
    print(f"Hello {fname} {lname}")


# args
sayHello("isuru", "mahesh")

# keyword args
sayHello(fname="isuru", lname="mahesh")
sayHello(lname="mahesh", fname="isuru")