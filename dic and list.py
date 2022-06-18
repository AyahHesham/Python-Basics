Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f=[1,2,3,'ali',[2,3,4,5]]
f[-1]
[2, 3, 4, 5]
f[-2]
'ali'
f[0:4]
[1, 2, 3, 'ali']
f[0]=100

f
[100, 2, 3, 'ali', [2, 3, 4, 5]]
f*2
[100, 2, 3, 'ali', [2, 3, 4, 5], 100, 2, 3, 'ali', [2, 3, 4, 5]]
f*f
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    f*f
TypeError: can't multiply sequence by non-int of type 'list'
f.poop()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    f.poop()
AttributeError: 'list' object has no attribute 'poop'. Did you mean: 'pop'?
f.pop()
[2, 3, 4, 5]
f
[100, 2, 3, 'ali']
f*f
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f*f
TypeError: can't multiply sequence by non-int of type 'list'
f.pop()
'ali'
f
[100, 2, 3]
f*f
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f*f
TypeError: can't multiply sequence by non-int of type 'list'
TypeError: can't multiply sequence by non-int of type 'list'
SyntaxError: unterminated string literal (detected at line 1)

f.append(200)
f
[100, 2, 3, 200]
f.insert(0,50)
f
[50, 100, 2, 3, 200]
f.remove(2)
f
[50, 100, 3, 200]
del f[0]
f
[100, 3, 200]
f.sort()
f
[3, 100, 200]
f.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    f.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
f.sort(reverse=True)
f
[200, 100, 3]
d={'aya'=30,'alaa'=40,'ahmed'=50}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
d={'aya':50,'ahmed':60}
d['ahmed']
60
d.values()
dict_values([50, 60])
d.keys()
dict_keys(['aya', 'ahmed'])
d.items()
dict_items([('aya', 50), ('ahmed', 60)])
for i in d:
    print(i)

    
aya
ahmed
for x,y in d.items():
    print(x,y)

    
aya 50
ahmed 60
while x=<10:print(x);x+=1
SyntaxError: invalid syntax
while x<10:print(x);x+=1

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    while x<10:print(x);x+=1
TypeError: '<' not supported between instances of 'str' and 'int'
while u<10:print(u);u+=1

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    while u<10:print(u);u+=1
NameError: name 'u' is not defined
u=0while u<10:print(u);u+=1
SyntaxError: invalid decimal literal
u=0
while u<10:print(u);u+=1

0
1
2
3
4
5
6
7
8
9
