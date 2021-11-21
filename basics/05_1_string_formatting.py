from string import Template

print('''
        #1 “Old Style” String Formatting (% Operator)
''')
errno = 50159747054
name = 'Bob'
print('Hello, %s' % name)
print('%x' % errno)
print('Hey %s, there is a 0x%x error!' % (name, errno))
print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno})

print('''
        #2 “New Style” String Formatting (str.format)
''')
print('Hello, {}'.format(name))
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

print('''
        #3 String Interpolation / f-Strings (Python 3.6+)
''')
print(f'Hello, {name}')
print(f"Hey {name}, there's a {errno:#x} error!")
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

print('''
        #4 Template Strings (Standard Library)
''')
templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))

data = ("John", "Wick", 133.55)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % (data[0], data[1], data[2]))