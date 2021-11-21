my_string = 'spam eggs'               # single quotes
print(my_string)
my_string = 'doesn\'t'                # use \' to escape the single quote...
print(my_string)
my_string = "doesn't"                 # ...or use double quotes instead
print(my_string)
my_string = '"Yes," they said.'
print(my_string)
my_string = "\"Yes,\" they said."
print(my_string)
my_string = '"Isn\'t," they said.'
print(my_string)

print(" ")
print('\tFirst line.\n\tSecond line.')
print(r'\tFirst line.\n\tSecond line.')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(" ")
print(3 * 'un' + 'ium')             # 3 times 'un', followed by 'ium'
print('Py' 'thon')

print(" ")
my_string = ('Put several strings within parentheses'
             'to have them joined together.')
print(my_string)

print(" ")
my_string = 'Py'
print(my_string + 'thon')

print(" ")
my_string = 'Python'
print(my_string[0] + ' ' + my_string[5])
print(my_string[-1] + ' ' + my_string[-2] + ' ' + my_string[-6])
print(my_string[0:2] + ' ' + my_string[2:5])
print(my_string[:2] + ' ' + my_string[4:] + ' ' + my_string[-2:])
print(my_string[:2] + my_string[2:])
print(my_string[:4] + my_string[4:])
print('J' + my_string[1:])
print(my_string[:2] + 'py')
print(len(my_string))
