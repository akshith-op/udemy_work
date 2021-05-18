class Student:
    def __init__(self):
        self.name = 'Akshith'
        self.age = 13
        self.marks = 92
        print("__init__ is called")
    def talk(self):
        print('Name: ',self.name)
        print("my marks: ", self.marks)
        print("my age: ",self.age)
s1 = Student()
s1.name = 'ashwath'
print(s1.name)
s1.talk()
print(s1.marks)
s2 = Student()
print(s2.name)
print(s2.marks)
s2.talk()
