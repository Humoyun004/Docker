import os

# Yaratgan muhut o'zgaruvchilarni olib keldim
surname = os.environ.get('last_name')
name = os.environ.get('first_name')
age = os.environ.get('age')

imported_text = f"Hello my name is {surname} {name} and I am {age}"

print(imported_text)
