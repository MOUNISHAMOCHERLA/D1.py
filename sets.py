Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #SETS{}
>>> a={1,2,6.7,2+5j,True,False,'mounisha'}
>>> print(a)
{False, 1, 2, 'mounisha', (2+5j), 6.7}
>>> type(a)
<class 'set'>
>>> b={5,7,10,12,14,15}
>>> print(b)
{5, 7, 10, 12, 14, 15}
>>> #add()
>>> a={'a,',2+9l,'mourya',9,7}
SyntaxError: invalid decimal literal
>>> a={'a,',2+l9,'mourya',9,7}
... 
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a={'a,',2+l9,'mourya',9,7}
NameError: name 'l9' is not defined
>>> a={1,2,3}
>>> a.add(6)
>>> a
{1, 2, 3, 6}
>>> #issubset
>>> a={1,2,3,4,5,6}
>>> b={1,4}
>>> b.issubset(a)
True
a.issubset(b)
False
#superset
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
b.superset(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.superset(a)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
b.issuperset(a)
False
#union()
a={5,6,7}
b=(1,2,3,4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b={1,2,3,4}
b.union(a)
{1, 2, 3, 4, 5, 6, 7}
#intersection()
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
b.intersection(a)
{8, 9, 7}
#update()
a={4,5,6,7,8,9}
={7,8,9,10,11,12}
SyntaxError: invalid syntax
b={7,8,9,10,11,12}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
#difference()
a={3,4,5,6,7,8}
b={8,9,10,11,12}
b.difference(a)
{9, 10, 11, 12}
a.difference(b)
{3, 4, 5, 6, 7}
#symmetric_difference
a={10,11,12,13,14,15,16,17}
b={13,14,15,16,17,18}
a.symmetric_difference(b)
{10, 11, 12, 18}
b.symmetric_difference(a)
{10, 11, 12, 18}
#intersection_update
a={1,2,3,4}
b={5,3,6,4}
a.intersection_update(b)
a
{3, 4}
b.intersection_update(a)
b
{3, 4}
#difference_update
a={1,2,3,4,5}
{1,2,6,7,8,9}
{1, 2, 6, 7, 8, 9}
a={1,2,3,4,5}
b={1,2,6,7,8,9}
a.difference_update(b)
a
{3, 4, 5}
b.difference_update(a)
b

b
{1, 2, 6, 7, 8, 9}
#symmetric_difference_update
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#pop
a={7,8,9,10,11,12}
pop()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    pop()
NameError: name 'pop' is not defined. Did you mean: 'pow'?
a.pop()
7
#remove()
a={7,8,9,10,11,12}
a.remove(3)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.remove(3)
KeyError: 3
a.remove(8)
a
{7, 9, 10, 11, 12}
#discard
b={1,2,3,4}
b.discard()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b.discard()
TypeError: set.discard() takes exactly one argument (0 given)
discard(4)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    discard(4)
NameError: name 'discard' is not defined
b.discard(4)
b
{1, 2, 3}
#copy()
s={1,2,3,4,5}
s.copy()
{1, 2, 3, 4, 5}
b=s.copy()
print(b)
{1, 2, 3, 4, 5}
#clear()
s.clear()
s
set()
b.clear()
b
set()
s.add('mounisha')
s
{'mounisha'}
#isdisjoint
a={1,2,3,4}
b={4,5,6,7}
a.isdisjoint(b)
False
