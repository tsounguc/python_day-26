# new_numbers = [new_item for item in list]
import random

# Practice
# numbers = [1,2,3]
#
# new_numbers = [n + 1 for n in numbers]
#
# name = "Angela"
#
# new_list = [letter for letter in name]
#
# double_numbers = [number * 2 for number in range(1,5)]
#

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# shor_names = [name.upper() for name in names if len(name) < 5]

# Dictionary Comprehension
# new_dict =  {new_key: new_value for item in list}
# new_dict =  {new_key: new_value for (key, value) in diction.items()}
# new_dict =  {new_key: new_value for (key, value) in diction.items() if test }

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1,100) for student in names}
# passed_students = {student: score for (student, score) in students_score.items() if score > 60}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(f"{row.student}: {row.score}")
