def get_student_dict(fname, lname):
    student = {
        "first_name": fname,
        "last_name": lname
    }
    return student

def get_student_list(fname, lname):
    student = [fname, lname]
    return student


s1 = get_student_list("isuru", "mahehs")
print(s1)
print(type(s1))