Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LIST
a=['python','dsa','ml','ai']
a
['python', 'dsa', 'ml', 'ai']
type(a)
<class 'list'>
print(a[2])
ml
#APPEND
a.append('sql')
a
['python', 'dsa', 'ml', 'ai', 'sql']
#EXTEND
a=['a','b','c',['d','e'])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=(['a','b','c',['d','e'])
   
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=['a','b','c']
   
a.extend(['d','e'])
   
a
   
['a', 'b', 'c', 'd', 'e']
#INSERT
   
b=['mounisha','pranathi']
   
b.insert(1,'nikky')
   
b
   
['mounisha', 'nikky', 'pranathi']
#INDEX
   
m=[1,2,3,4]
   
m.index(3)
   
2
>>> #COPY
...    
>>> m.copy()
...    
[1, 2, 3, 4]
>>> #pop
...    
>>> A=['VJA','VIZAG','HYD']
...    
>>> a.pop()
...    
'e'
>>> 'vja'
...    
'vja'
>>> a.pop(1)
...    
'b'
>>> a.pop('VJA')
...    
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pop('VJA')
TypeError: 'str' object cannot be interpreted as an integer
>>> #REMOVE
...    
