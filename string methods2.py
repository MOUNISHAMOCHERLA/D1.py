Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#UPPER
a='mounisha'
a.upper()
SyntaxError: multiple statements found while compiling a single statement
a='code'
a.upper()
'CODE'
b='python'
b.upper()
'PYTHON'
b[0].upper
<built-in method upper of str object at 0x00007FFB3E5092B0>
#LOWER
c='MOUNISHA'
c.lower()
'mounisha'
#CAPITALIZE
str='my name is mounisha'
str.capitalize()
'My name is mounisha'
#TITLE
str='my name is mounisha'
str.title()
'My Name Is Mounisha'
d='pYTHON'
d[0].upper()
'P'
str.capitalize()
'My name is mounisha'
str.title()
'My Name Is Mounisha'
b='Python COURSE'
b.upper()
'PYTHON COURSE'
str1='codegnanpfs'
str1.isalpha()
True
str1.isupper()
False
str2='aero space'
str.islower()
True
q1='abc123'
q1.isdigit()
False
q1.isalpha()
False
a='mounisha'
a.startswith(h)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.startswith(h)
NameError: name 'h' is not defined
a.startswith('o')
False
a.endswith('a')
True
m='mounisha@123'
m.isalnum()
False
m='mounisha123'
m.isalnum()
True
#STRIP
#RSTRIP, LSTRIP
a='  mounisha '
a.rstrip()
'  mounisha'
a.lstrip()
'mounisha '
a='pranathi is bad girl'
a.strip()
'pranathi is bad girl'
a.rstrip()
'pranathi is bad girl'
b='pranahiisgoodgirl'
b.split()
['pranahiisgoodgirl']
f='python course')
SyntaxError: unmatched ')'
f='python course'
f.split()
['python', 'course']
f[0].upper()
'P'
f[0].cpitalize()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    f[0].cpitalize()
AttributeError: 'str' object has no attribute 'cpitalize'. Did you mean: 'capitalize'?
f[0].capitalize()
'P'
#join()
a='apple','banana','avocado'
a.join()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.join()
AttributeError: 'tuple' object has no attribute 'join'
''.join(a)
'applebananaavocado'
''m.join(a)
SyntaxError: invalid syntax
''a.join(a)
SyntaxError: invalid syntax
'a'.join(a)
'appleabananaaavocado'
b='mynameismounisha'
's'.join(b)
'msysnsasmsesisssmsosusnsissshsa'
#STRING CONCATENATION
a='code'
b='gnan'
print(a+b)
codegnan
print(a+''b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a+''+b)
codegnan
print(a+' '+b)
code gnan
fname='kl'
lname='university'
print(fname+lname)
kluniversity
print(fname+'   '+lname)
kl   university
print(fname.upper())
KL
print(fname.upper()+' '+lname.capitalize())
KL University

#FORMATTING
a='mounisha'
b='KLU'
print('word is:',a+b)
word is: mounishaKLU
a='hello guys'
print('greeting you:',a)
greeting you: hello guys

#FORMAT
a='mounisha'
b='pranathi'
print('hi {}{}'.format(a,b))
hi mounishapranathi
print('hi {} hi {}',format(a,b))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('hi {} hi {}',format(a,b))
ValueError: Invalid format specifier 'pranathi' for object of type 'str'
>>> print('hi {} hi {}',.format(a,b))
SyntaxError: invalid syntax
>>> print('hi {} hi {}'.format(a,b))
hi mounisha hi pranathi
>>> 
>>> #FSTRING
>>> a='abcd'
>>> b='1234'
>>> print(f'alphabets{a} numbers{b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'alphabets{a} numbers{b}')
...       
alphabetsabcd numbers1234
>>> a=4
...       
>>> a=4
...       
>>> 
>>> 
>>> a=4
...       
>>> b=5
...       
