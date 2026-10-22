Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators

#logical
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>b or b>a
True
a!=b or a==b
True
a<=b or b>=a
True
not True
False
not False
True

#identify
a=3
type(a) is int
True
type is not int
True
name='mounisha'
type(name) is str
True
type(name) is int
False
tye(name) is not str
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tye(name) is not str
NameError: name 'tye' is not defined. Did you mean: 'type'?
type(name) is not str
False
com=2+5j
type(com)is com
False
type(com) is complex
True

#membership
a=2,3,4,5,6,7
a=2,3,4,5,6,7,8,9
9 in a
True
24 in a
False
2 in a
True

#binary
a=2
b=5
bin(a)
'0b10'
#or|
a=4
b=8
a|b
12
#~
a=5
~a
-6
b=-4
~b
3
>>> (-b+1)
5
>>> (-a+1)
-4
>>> 
>>> #^XOR
>>> a=4
>>> b=9
>>> a^b
13
>>> a=5
>>> b=10
>>> a^b
15
>>> a=3
>>> a<<3
24
>>> a=6
>>> a<<2
24
>>> a=2
>>> a>>3
0
>>> a=8
>>> a>>2
2
