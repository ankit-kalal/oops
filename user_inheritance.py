
class User():

    def login(self):
        print("login")

    def register(self):
        print("register")



class Student(User):

    def enroll(self):
        print("enroll")

    def review(self):
        print("review")


stu = Student()


stu.login()
stu.register()
stu.enroll()
stu.review()