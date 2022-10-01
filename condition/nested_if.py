print("please enter email")
email = input()
print("please enter password")
password = input()
print("please enter gender")
gender = input()
print("please enter status")
status = input()

if status == "on":
    status = "active"
else:
    status = "inactive"

print("please enter age")
age = input()

# user record
user_info = {
    "email": "isuru@gmail.com",
    "password": "123",
    "gender": "male",
    "status": "active",
    "age": 25
}

# email and password is valid -> check status
# if status inactive -> error message
# if status active -> successfully loggedin
# email or password invalid -> error message

if email == user_info["email"] and password == user_info["password"]:
    
    if status == "active":
        print("sucessfully logged in")

    else:
        print("account status should active")

else:
    print("email or password invalid")

