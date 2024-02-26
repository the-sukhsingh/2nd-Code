Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3,4,5]
>>> list2 = [1,2,2.3,4,6]
>>> list3 = [1,11.5,4+9j]
>>> list4 = [1,'Sukh',4.6,'P']
>>> list1+list2
[1, 2, 3, 4, 5, 1, 2, 2.3, 4, 6]
>>> list1*5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> list1[2]
3
>>> list1[-2]
4
>>> list1[3:]
[4, 5]
>>> list1[2] = 8
>>> list1
[1, 2, 8, 4, 5]
>>> tup1 = (1,2,3,4,5)
>>> tup2 = (4,8.5,2+4j,'Sukh')
>>> tup1[2]
3
>>> tup1[2] = 6
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tup1[2] = 6
TypeError: 'tuple' object does not support item assignment
