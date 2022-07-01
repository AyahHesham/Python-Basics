Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
m=1
for x in (1,11):
    print(f'{m}*{x}={m*x}')

    
1*1=1
1*11=11
for x in range(1,11):
    print(f'{m}*{x}={m*x}')

    
1*1=1
1*2=2
1*3=3
1*4=4
1*5=5
1*6=6
1*7=7
1*8=8
1*9=9
1*10=10
for m in range(1,6):
    for x in range(1,10):
        print(f'{m}*{x}={m*x}')

        
1*1=1
1*2=2
1*3=3
1*4=4
1*5=5
1*6=6
1*7=7
1*8=8
1*9=9
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
for m in range(1,6)
SyntaxError: expected ':'
for m in range(1,6):
    for x in range(1,11):
        print(f'{m}*{x}={m*x}')
    print('---------------------')

    
1*1=1
1*2=2
1*3=3
1*4=4
1*5=5
1*6=6
1*7=7
1*8=8
1*9=9
1*10=10
---------------------
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
---------------------
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30
---------------------
4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36
4*10=40
---------------------
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50
---------------------
start=int(input('Enter the start'))
Enter the start
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    start=int(input('Enter the start'))
ValueError: invalid literal for int() with base 10: ''
end=int(input('Enter the end'))
Enter the end
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    end=int(input('Enter the end'))
ValueError: invalid literal for int() with base 10: ''
for m in range(start,end+1):
    for x in range(1,11):
        print(f'{m}*{x}={m*x}')
    print('------------------')

    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for m in range(start,end+1):
NameError: name 'start' is not defined
start=int(input('enter the start'))
enter the start2
end=int(input('enter the end'))
enter the end5
for x in range(start,end+1):
    for y in range(1,11):
        print(f'{x}*{y}={x*y}')
    print('---------------------')

    
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
---------------------
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30
---------------------
4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36
4*10=40
---------------------
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50
---------------------


