Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a='python course'
>>> a[-1:-8:-3]
'eu '
>>> a[-1:-8:-2]
'ero '
>>> a[-2:-10:-3]
'son'
>>> a[-1:-12:-6]
'e '
>>> a[-4:-9:-2]
'ucn'
>>> 
>>> #IN +VE STRIDING, HIGHEST TO LOWEST NOT POSSIBLE
>>> #IN -VE STRIDING, LOWEST TO HIGHEST NOT POSSIBLE
>>> 
>>> a='python course'
>>> a[9:5:2]
''
>>> a[5:9:2]
'nc'
>>> a[-6:-10:-2]
'cn'
>>> a[::1]
'python course'
a[::-1]
'esruoc nohtyp'

#STRING METHOD
#len()
a='python'
len(a)
6
b='supercalifragilisticexpilidacious'
len(b)
33
c=''
len(c)
0
m='mounisha
SyntaxError: unterminated string literal (detected at line 1)
m='mounisha'
len(m)
8
f='    '
len(f)
4
#COUNT
a='twinkle twinkle little star'
a.count('twinkle')
2
a.count('t')
5
aa.count('a')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    aa.count('a')
NameError: name 'aa' is not defined. Did you mean: 'a'?
a.count('a')
1
a.count('')
28
a.count(' ')
3
a='1234'
a.count('3')
1
a=1,2,3,4,5
a.count(5)
1
#FIND A STRING
a='code'
a[2]
'd'
a.find('d')
2
b='hello'
b.find('l')
2
#ESCAPE SEQUENCES

\n new line
SyntaxError: unexpected character after line continuation character
#\t tab space
a='name:mounisha'\n'mobile no:1234567'
SyntaxError: unexpected character after line continuation character
a='name\nmobilenp\tmailid\ncollege\tbranch'
print(a)
name
mobilenp	mailid
college	branch
b='name:mounisha'\n 'branch:mca'
SyntaxError: unexpected character after line continuation character
b='name:mounisha\tbranch:mca\nmobile no:7416355487'
print(b)
name:mounisha	branch:mca
mobile no:7416355487
#REPLACE
a='wait until you succeed'
a.replace('wait','work')
'work until you succeed'
b='she is good'
b.replace('she','mounisha')
'mounisha is good'
a.replace('wait','work')
'work until you succeed'
a='wait until you succeed'
a.replace('wait','until','until','wait')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.replace('wait','until','until','wait')
TypeError: replace() takes at most 3 arguments (4 given)
