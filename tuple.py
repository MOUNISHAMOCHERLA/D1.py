Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #TUPLE
>>> a=(6,8.9.2+5j,'mounisha',True,False)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=(6,8.9,2+5j,'mounisha',True,False)
>>> print(a)
(6, 8.9, (2+5j), 'mounisha', True, False)
>>> type(a)
<class 'tuple'>
>>> print(a[1])
8.9
>>> a.count('b')
0
