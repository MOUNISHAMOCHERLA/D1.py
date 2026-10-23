Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#INDEXING

m='mounisha'
m[7]
'a'
str='my name is mounisha'
str[11]+[12]+[13]+[14]+[15]+[16]+[17]+[18]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str[11]+[12]+[13]+[14]+[15]+[16]+[17]+[18]
TypeError: can only concatenate str (not "list") to str
str[11]+str[12]+str[13]+str[14]+str[15]+str[16]+str[17]+str[18]
'mounisha'
str[2]+str[7]+str[10]
'   '
str[3]+str[4]+str[5]+str[6]
'name'
a='I am learning python full stack'
a[14]+a[15]+a[16]+a[17]a[18]+a[19]
SyntaxError: invalid syntax
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[2]+a[3]
'am'
a[21]+a[22]+a[23]+a[24]
'full'
b='Time is very precious'
b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
b[10]+b[11]+b[12]
'ry '
+b[8]+b[9]+b[10]+b[11]+b[12]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    +b[8]+b[9]+b[10]+b[11]+b[12]
TypeError: bad operand type for unary +: 'str'
b[8]+b[9]+b[10]+b[11]+b[12]
'very '
b[0]+b[1]+b[2]+b[3]
'Time'
b[8]+b[9]+b[10]+b[11]
'very'

#-ve indexing

a='vijayawada is a royal city'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-6]+a[-7]+a[-8]+a[-9]
'layo'
a[-6]+a[-7]+a[-8]+a[-9]+a[-10]
'layor'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-14]+a[-15]
'si'
a[-15]+a[-14]
'is'
b='vizag is a city of destiny'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'

#SLICING
a='codegnan'
a[:4]
'code'
a[4:]
'gnan'
a='work until you succeed'
a[15:22]
'succeed'
a[5:10]
'until'
a[0:4]
'work'
a[11:14]
'you'
b='simple is better than complex'
b[10:16]
'better'
b[0:6]
'simple'
b[22:29]
'complex'
b[7:9]
'is'
b[-13:-9]
' tha'
b='python is easy to learn'
b[-13:-9]
'easy'
b[-23:-11]
'python is ea'
[-23:-17]
SyntaxError: invalid syntax
b[-23:-17]
'python'
b[-5:]
'learn'
a='god is great'
a[-5:]
'great'
a[-12:-9]
'god'
a[-8:-6]
'is'
b[-5:0]
''
>>> 
>>> #STRIDING
>>> 
>>> a='data science'
>>> a[::]
'data science'
>>> a='cloud computing'
>>> a[3:11]
'ud compu'
>>> a[::5]
'c u'
>>> a[::8]
'cm'
>>> a[5:]
' computing'
>>> a[:12]
'cloud comput'
>>> a[::2]
'codcmuig'
>>> b='machine learning'
>>> b[1:9]
'achine l'
>>> b[9:2]
''
>>> b[1:9:2]
'ahn '
