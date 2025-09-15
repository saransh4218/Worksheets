# question 1
# def diff(n):
#     if(n>17):
#         diff=17-n
#         diff=diff*(-1)
#         diff=2*diff
#         print(diff)
#     else:
#         diff=17-n
#         print(diff)

# n=int(input("enter your number:"))
# diff(n)


# question 2


# def num(n):
#     if(n==2000):
#         print("the number entered is 2000")
#     if(n>=0 and n<100):
#         print("the number entered is invalid")
#     if(n>=100 and n<=1000):
#         print("the number entered is in the range of 100 to 1000")
#     if(n>1000 and n<2000):
#         print("the number entered is invalid")

# n=int(input("Enter the number here:"))
# num(n)


# question 3


# def stringrev(a):
#     reversed_string=a[::-1]
#     print(reversed_string)

# a=[]
# a=input("Enter your name:")
# stringrev(a)


# question 4


# def countcase(a):
#     upper=0
#     lower=0
#     for ch in a:
#         if ch.islower():
#             lower+=1
#         elif ch.isupper():
#             upper+=1
#     print("upper case letters",upper)
#     print("lower case letters",lower)

# a=input("Enter your full name: ")
# countcase(a)



# question 6


# def evenno(l):
#     for no in l:
#         if(no%2==0):
#             print(no)

# l=list(map(int,input("Enter the numbers:"))).split()
# evenno(l)

#question 7
# Q7
def robot():
    def move():
        print("Moving")
    move()

robot()

#question 8
# Q8
def student(name, age, course):
    print(student.__code__.co_varnames)

student("Ram", 20, "CSE")

#question 9
# Q9
def move_robot(x, y, d):
    if d == "up":
        y = y + 1
    elif d == "down":
        y = y - 1
    elif d == "left":
        x = x - 1
    elif d == "right":
        x = x + 1
    return (x,y)

print(move_robot(0,0,"up"))
print(move_robot(0,0,"right"))

#question 10
def classify_temperature(t):
    if t < 15:
        return "Cold"
    elif t >= 15 and t <= 30:
        return "Moderate"
    else:
        return "Hot"

print(classify_temperature(10))
print(classify_temperature(20))
print(classify_temperature(35))

#question 11
def is_goal_reached(path):
    x = 0
    y = 0
    for p in path:
        if p == "up":
            y = y + 1
        elif p == "down":
            y = y - 1
        elif p == "left":
            x = x - 1
        elif p == "right":
            x = x + 1
    if x == 2 and y == 0:
        return True
    else:
        return False

print(is_goal_reached(["up","right","right","down"]))
print(is_goal_reached(["right","right"]))

#question 12
class Student:
    def __init__(self, sid, sname, sclass):
        self.student_id = sid
        self.student_name = sname
        self.student_class = sclass

    def show(self):
        print("ID:", self.student_id)
        print("NAME:", self.student_name)
        print("CLASS:", self.student_class)

s = Student(1,"Ram","CSE")
s.show()

#question 13
class Student:
    def __init__(self, sid, sname, sclass):
        self.sid = sid
        self.sname = sname
        self.sclass = sclass

st1 = Student(1,"Ram","CSE")
st2 = Student(2,"Shyam","ECE")

print("Student1:", st1.sid, st1.sname, st1.sclass)
print("Student2:", st2.sid, st2.sname, st2.sclass)

#question 14
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def peri(self):
        return 2 * 3.14 * self.r

c = Circle(5)
print("AREA:", c.area())
print("PERI:", c.peri())

#question 15
class StringClass:
    def get_String(self):
        self.s = input("Enter string: ")

    def print_String(self):
        print(self.s.upper())

sc = StringClass()
# sc.get_String()
# sc.print_String()

# Question 16
class Robot:
    def __init__(self, name, task, battery_level):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        print(self.name, "performing", self.task)
        self.battery_level = self.battery_level - 10

    def recharge(self):
        self.battery_level = 100

    def status(self):
        print("NAME:", self.name)
        print("TASK:", self.task)
        print("BATTERY:", self.battery_level)

r = Robot("R2D2","cleaning",100)
r.perform_task()
r.status()
r.recharge()
r.status()