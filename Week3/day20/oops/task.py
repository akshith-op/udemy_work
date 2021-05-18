n = str(input("what's your name: "))
a = int(input("whats's your age: "))
m = int(input("your marks: "))
class Student:
    def __init__(self, n, m , a):
        self.name = n
        self.age = a
        self.marks = m
    def display(self):
        print("My name is ", self.name)
        print("my age is ", self.age)
        print("I got", self.marks, 'marks in mathematics')

s1 = Student(n,m,a)
s1.display()
