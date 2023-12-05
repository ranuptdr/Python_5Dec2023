name = input('Please enter your name')

age = input("Please enter your age")
# TypeCast    string --> Float
age = float(age)
# string --> Float

# if age is greater than you can vote
if age >=18 :
    print(''' you can vote''')
else:
    print('you can\'t vote')