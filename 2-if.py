Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
username='aya'
if username=='aya'
SyntaxError: expected ':'

if username=='aya':
    print('yes')

    
yes
if username=='alaa'
SyntaxError: expected ':'
if username=='alaa':
    print('yes')
else:
    print('no')

    
no
x=5
x=5
if x>4:
    print('x>4')
elif x>=5:
    print("x>=5")
else:
    print('no')

    
x>4
y=200
if x>100:
    print('x>100')
    if x<200:
        print('x<200')
else:
    print('bye')

    
bye
bye
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    bye
NameError: name 'bye' is not defined
if y>100:
    print('y>100')
    if x<200:
        print('y<200')
else:
    print('bye')

    
y>100
y<200
usermae='aya'
passowrd='123'
if username=='aya' and passowrd='123':
    
SyntaxError: invalid syntax
if username=='aya' and passowrd=='123':
    print('yes')
else:
    print('no')

    
yes
if all([username='aya',passowrd='123']):
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if all([username=='aya',passowrd=='123']):
    print('yes')
else:
    print('bye')

yes
if username=='alaa' or password=='123':
    print('hello')
else
SyntaxError: expected ':'
:
    else:
        
SyntaxError: invalid syntax

    else:
        
SyntaxError: unexpected indent
else:
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
KeyboardInterrupt
if username=='alaa' or password=='123':
    print('hello')
else:
    print('bye')

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    if username=='alaa' or password=='123':
NameError: name 'password' is not defined. Did you mean: 'passowrd'?
if username=='alaa' or passowrd=='123':
    print('hello')
else:
    print('bye')

hello
if any([username=='alaa',password=='123']):
    print('hello')
else:
    print('bye')

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    if any([username=='alaa',password=='123']):
NameError: name 'password' is not defined. Did you mean: 'passowrd'?
if any([username=='alaa',passowrd=='123']):
    print('hello')
else:
    print('bye')

hello
if x==5:print('hi')

hi
print('x=5')if x==5 else print('bye')
x=5
