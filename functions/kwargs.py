def sayHello(fname, lname):
    print(f"Hello {fname} {lname}")


# args
sayHello("isuru", "mahesh") # Hello isuru mahesh
sayHello("mahesh", "isuru") # Hello mahesh isuru

# keyword args
sayHello(fname="isuru", lname="mahesh") # Hello isuru mahesh
sayHello(lname="mahesh", fname="isuru") # Hello isuru mahesh