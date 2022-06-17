Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sum(x,y):
    result=x+y
    print(result)
    return(result)

sum(3,4)
7
7
x=sum(8,9)
17
x*7
119
print(x)
17
x=5
y=6
print(x+y)
11
def s():
    x=5
    y=6
    print(x+y)
s()
SyntaxError: invalid syntax
s()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s()
NameError: name 's' is not defined
s()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s()
NameError: name 's' is not defined
def mysum():
    x=4
    y=7
    print(x+y)

    
mysum()
11
s()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s()
NameError: name 's' is not defined
s ()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s ()
NameError: name 's' is not defined
def darb(x=0,y=0):
    return x*y
darb(5,10)
SyntaxError: invalid syntax

darb(5,10)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    darb(5,10)
NameError: name 'darb' is not defined
def darb(x=0,y=0):
    return x*y

darb(5,10)
50
darb(7)
0
s=darb(y=9,x=10)
print(s)
90
x
5
darb(y=5)
0
def da(x,y=1):
    return x*y

da(x=6)
6
da(y=11)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    da(y=11)
TypeError: da() missing 1 required positional argument: 'x'
'''anouminus function'''
'anouminus function'
mysum
<function mysum at 0x000001722D058310>
mys=lambda x,y=x-y
SyntaxError: invalid syntax
mys=lambda x,y:x-y
mys()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    mys()
TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'
mys(5,4)
1
print(mys(9,5))
4
'''
استدعاء الدالة في سطر واحد مع تعريفها
'''
'\nاستدعاء الدالة في سطر واحد مع تعريفها\n'
(lambda x,y:x/y)(70,7)
10.0
f=0
print(f)
0
def do():
    f=5
    print(f)

    
do()
5
print(f)
0
def do():
    global f
    f=5
    print(f)

    
do()
5
f
5
