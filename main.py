# new_numbers = [new_item for item in list]

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

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
shor_names = [name.upper() for name in names if len(name) < 5]
