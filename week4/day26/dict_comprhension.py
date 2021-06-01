import random
students_score = {
    "alex": 89,
    "beth": 90,
    "akshith": 99,
    "ashwath": 98
}
names = ['alex', "beth", 'akshith','ashwath']
score ={i:random.randint(1,101) for i in names}
print(score)
passed_students = {i:score for (i, score) in score.items() if score>=60}
print(passed_students)