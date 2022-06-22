Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Number         square')
Number         square
print('----------------------')
----------------------
forx in range(10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    forx in range(10)
NameError: name 'forx' is not defined
forx in range(10):
    
SyntaxError: invalid syntax
for x in range(11):
    print(x,'   ',y)

    
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    print(x,'   ',y)
NameError: name 'y' is not defined
for x in range(11):
    print(x,'   ',x*x)

    
0     0
1     1
2     4
3     9
4     16
5     25
6     36
7     49
8     64
9     81
10     100
print('Number\tsquare')
print('----------------------')
for x in range(11):
    print(x,'\t',x*x)
    
SyntaxError: multiple statements found while compiling a single statement
print('Number\tsquare')
print('----------------------')
for x in range(11):
    print(x,'\t',x*x)
    
SyntaxError: multiple statements found while compiling a single statement
print('Number\tsquare')

print('----------------------')

for x in range(11):
    print(x,'\t',x*x)
    
SyntaxError: multiple statements found while compiling a single statement
print('Number\tsquare')
Number	square
for x in range(11):
    print(x,'\t',x*x)

    
0 	 0
1 	 1
2 	 4
3 	 9
4 	 16
5 	 25
6 	 36
7 	 49
8 	 64
9 	 81
10 	 100
