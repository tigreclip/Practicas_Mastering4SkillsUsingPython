name, age = 'miguel', 22
print(name,'is', age, 'years old') # OLD WAY 1 > miguel is 22 years old
print(name + ' is ' + str(age) + ' years old') # OLD WAY 2 > miguel is 22 years old 

# REPLACEMENT FIELD
# The first {} is replaced with miguel
# The 2nd {} with 33
print('{} is {} years old'.format(name, age)) # miguel is 22 years old

# we call this string with curly braces {} as template

# print('{}{}{}'.format('Hey')) #  You need to provide 3 arguments
# IndexError: Replacement index 1 out of range for positional args tuple

print('{}{}{}'.format(1, 2, 3, 4, 5, 6)) # 123 - OK to provide, more are ignored


#tricky bun useless
print('{}') # {}
print('{{}}') # {{}}
print('{{{}}}'.format('Hey')) # {Hey} - if you want to surround an item with {}, use double: {{ }}
print('{{{{{{}}}}}}'.format('Hey')) # don't {{{}}}
print('{{{{{{{{}}}}}}}}'.format('Hey')) # don't  {{{{}}}}
 
####################################################################################################

name, age = 'miguel', 22

print('{0} is {1} years old'.format(name, age)) # {0}{1} posicional arguments
# miguel is 22 years old

# print('{0} is {2} years old'.format(name, age)) # indexError -> no idx 2
# IndexError: Replacement index 2 out of range for positional args tuple

print('{0} is {1} years old. Are you {1} years as {0}?'.format(name, age))
# miguel is 22 years old. Are you 22 years as miguel?
# pros: you provide positional arguments once and use it many

print('{name} is {AGE} years old. Are you {AGE} years as {name}?'.format(name=name, AGE=age))
# miguel is 22 years old. Are you 22 years as miguel?
# similary, we can use keywords arguments but flexible order!

# Be careful from mixing
print('{} is {age} years old'. format(name, age= age)) # miguel is 22 years old
print('{0} is {age} years old'.format(name, age=age)) # miguel is 22 years old

print('{1} is {age} years old'.format(age=age, name)) # 
#SyntaxError: positional argument follows keyword argument