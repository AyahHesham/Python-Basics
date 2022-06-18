Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=0
while x<10:
    print(x)
    x+=1

    
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
x
10
while x<10:print(x);x+=1


y=0
while y<10:print(y);y+=1

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
'''
nested loop
'''
'\nnested loop\n'
x=0
while x<5:
    print(x)
    x+=1

    
0
1
2
3
4
x=0
while x<5:
    print(x)
    y=0
    while y<5
    
SyntaxError: expected ':'
while x<5:
    print(x)
    y=0
    while y<5:
        print(y)
        y+=1
    x+=1

    
0
0
1
2
3
4
1
0
1
2
3
4
2
0
1
2
3
4
3
0
1
2
3
4
4
0
1
2
3
4
for letter in 'hesham':
    print(letter)

    
h
e
s
h
a
m
range(10)
range(0, 10)

range(0,10)
range(0, 10)
range(2,20,2)
range(2, 20, 2)
list[range(10)]
list[range(0, 10)]
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(1,20):
    print(x)

    
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
for x in range(5)
SyntaxError: expected ':'
;for x in range(5):
    
SyntaxError: invalid syntax
for x in range(5):
    print(x)
    for y in range(3)
    
SyntaxError: expected ':'
for x in range(5):
    print(x)
    for y in range(3):
        print(x,y)

        
0
0 0
0 1
0 2
1
1 0
1 1
1 2
2
2 0
2 1
2 2
3
3 0
3 1
3 2
4
4 0
4 1
4 2
for x in range(5):
    for y in range(3):
        print(x,y)

        
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2
for x in range(10):
    if x==6:
        print(x)

        
6
for x in range(10):
    if x==6:
    print(x)
    
SyntaxError: expected an indented block after 'if' statement on line 2
for x in range(10):
    if x==6:
    continue
SyntaxError: expected an indented block after 'if' statement on line 2
for x in range(10):
    if x==6:
        continue
    print(x)

    
0
1
2
3
4
5
7
8
9
for x in range(10):
    if x==6:
        break
    print(x)

    
0
1
2
3
4
5
