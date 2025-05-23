# Tracing the code:
'''
def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75}
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))
'''

def titlize(sentence):
    words = sentence.split()
    # print(words)
    new_words = []

    for word in words:
        # print(f"Processing word: {word}, length: {len(word)}")
        if len(word) > 2:
            # print(f"Processing word: {word}, length: {len(word)}")
            word = word.capitalize()
            # print(f"Processing word: {word}, length: {len(word)}")
        new_words.append(word)
            # print(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
# titlize(title)
