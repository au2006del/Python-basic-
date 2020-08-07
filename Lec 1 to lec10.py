Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> prog = {'JS':'ATOM', 'CS':'VS', 'Python':['Pycharm','Subline'],'Java':{'JSE','Netbeans','JEEE':'Eclipse'}}
SyntaxError: invalid syntax
>>> prog = {'JS':'ATOM', 'CS':'VS', 'Python':['Pycharm','Subline'],'Java':{'JSE':'Netbeans','JEEE':'Eclipse'}}
>>> porg ['JS']
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    porg ['JS']
NameError: name 'porg' is not defined
>>> prog ['JS']
'ATOM'
>>> prog ['CS']
'VS'
>>> prog ['Pyhton']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    prog ['Pyhton']
KeyError: 'Pyhton'
>>> prog ['Python']
['Pycharm', 'Subline']
>>> Prog ['Java']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Prog ['Java']
NameError: name 'Prog' is not defined
>>> prog ['Java']
{'JSE': 'Netbeans', 'JEEE': 'Eclipse'}
>>> prog ['Java']['JEE']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    prog ['Java']['JEE']
KeyError: 'JEE'
>>> prog ['Java']['JEEE']
'Eclipse'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> num = 5
>>> num
5
'
>>> address
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    address
NameError: name 'address' is not defined
>>> id (num)
1772709024
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> name = 'Anshul'
>>> id(name)
60625120
>>> 
>>> 
>>> 
>>> a= 10
>>> b=a
>>> a
10
>>> b
10
>>> id(a)
1772709104
>>> id(b)
1772709104
>>> k=10
>>> id(k)
1772709104
>>> a=9
>>> id(a)
1772709088
>>> id(b)
1772709104
>>> 
>>> 
>>> k=a
>>> id(k)
1772709088
>>> PI
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    PI
NameError: name 'PI' is not defined
>>> pi
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> PI
3.15
>>> type (PI)
<class 'float'>
>>> 
>>> 
>>> 
>>> num = 2.5
>>> num
2.5
>>> type (num)
<class 'float'>
>>> 
>>> 
>>> num = 5
>>> num
5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> num
(6+9j)
>>> type(num)
<class 'complex'>
>>> 
>>> 
>>> a= 5.6
>>> b= int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> b
5
>>> type(b)
<class 'int'>
>>> k=float(b)
>>> b
5
>>> k = float(b)
>>> k
5.0
>>> type()k
SyntaxError: invalid syntax
>>> 
>>> type(k)
<class 'float'>
>>> 
>>> k =6
>>> c= complex(b,k)
>>> c
(5+6j)
>>> b < k
True
>>> bool = b < k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b > k
False
>>> int(TRUE)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    int(TRUE)
NameError: name 'TRUE' is not defined
>>> int (tru)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int (tru)
NameError: name 'tru' is not defined
>>> 
>>> 
>>> int (true)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    int (true)
NameError: name 'true' is not defined
>>> int (True)
1
>>> int
<class 'int'>

>>> int (False)
0
>>> range (10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list (range(2,11,2))
[2, 4, 6, 8, 10]
>>> list (range(3,11,3))
[3, 6, 9]
>>> type(range)
<class 'type'>
>>> 
>>> 
>>> d = {'Anshul':'Iphone', 'Ronak':'Samsung', 'Karan':'Nokia', 'Manoj':'Oppo'}
>>> d
{'Anshul': 'Iphone', 'Ronak': 'Samsung', 'Karan': 'Nokia', 'Manoj': 'Oppo'}
>>> d.keys()
dict_keys(['Anshul', 'Ronak', 'Karan', 'Manoj'])
>>> d.values()
dict_values(['Iphone', 'Samsung', 'Nokia', 'Oppo'])
>>> d['Anshul']
'Iphone'
>>> d.get('Karan')
'Nokia'
>>> 
