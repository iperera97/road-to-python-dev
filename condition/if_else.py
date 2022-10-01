print("please enter email: ")
email = input()

print("please enter password: ")
password = input()

# email and password is valid -> user needs to go to home page
# email or password is not valid -> show error message to user
if email == "isuru@gmail.com" and password == "123":
    print("welcome to home page")
else:
    print("email or password invalid")