z = [1, 3, 2, 4, 'Alice', 'Bob']
z.sort(key=str)
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
'ABC'.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'.split()
'MyABCnameABCisABCSimon'.split('ABC')
'My name is Simon'.split('m') 