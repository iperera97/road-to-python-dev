print("enter your email: ")
email = input()

print("enter your password")
password = input()

if email == "isuru@gmail.com" and password == "123":
    print("isuru successfully logged in")

elif email == "john@gmail.com" and password == "333":
    print("john successfully loggedin")

elif email == "max@gmail.com" and password == "999":
    print("max successfully loggedin")

else:
    print("email or password is invalid")
