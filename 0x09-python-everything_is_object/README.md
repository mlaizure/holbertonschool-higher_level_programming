- 0: What function would you use to print the type of an object?
- 1: How do you get the variable identifier (which is the memory address in the CPython implementation)?
- 2: In the following code, do a and b point to the same object?
```
	>>> a = 89
	>>> b = 100
```
- 3: In the following code, do a and b point to the same object?
```
	>>> a = 89
	>>> b = 89
```
- 4: In the following code, do a and b point to the same object?
```
	>>> a = 89
	>>> b = a
```
- 5: In the following code, do a and b point to the same object?
```
	>>> a = 89
	>>> b = a + 1
```
- 6: What do these 3 lines print?
```
	>>> s1 = "Holberton"
	>>> s2 = s1
	>>> print(s1 == s2)
```
- 7: What do these 3 lines print?
```
	>>> s1 = "Holberton"
	>>> s2 = s1
	>>> print(s1 is s2)
```
- 8: What do these 3 lines print?
```
	>>> s1 = "Holberton"
	>>> s2 = "Holberton"
	>>> print(s1 == s2)
```
- 9: What do these 3 lines print?
```
	>>> s1 = "Holberton"
	>>> s2 = "Holberton"
	>>> print(s1 is s2)
```
- 10: What do these 3 lines print?
```
	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3]
	>>> print(l1 == l2)
```
- 11: What do these 3 lines print?
```
	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3]
	>>> print(l1 is l2)
```
- 12: What do these 3 lines print?
```
	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> print(l1 == l2)
```
- 13: What do these 3 lines print?
```
	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> print(l1 is l2)
```
- 14: What does this script print?
```
	l1 = [1, 2, 3]
	l2 = l1
	l1.append(4)
	print(l2)
```
- 15: What does this script print?
```
	l1 = [1, 2, 3]
	l2 = l1
	l1 = l1 + [4]
	print(l2)
```
- 16: What does this script print?
```
	def increment(n):
    	    n += 1

	a = 1
	increment(a)
	print(a)
```
- 17: What does this script print?
```
	def increment(n):
    	    n.append(4)

	l = [1, 2, 3]
	increment(l)
	print(l)
```
- 18: What does this script print?
```
	def assign_value(n, v):
    	    n = v

	l1 = [1, 2, 3]
	l2 = [4, 5, 6]
	assign_value(l1, l2)
	print(l1)
```
- 19: function that returns a copy of a list
- 20: In `a = ()` is `a` a tuple?
- 21: In `a = (1, 2)` is `a` a tuple?
- 22: In `a = (1)` is `a` a tuple?
- 23: In `a = (1, ) is `a` a tuple?
- 24: What does this script print?
```
	a = (1)
	b = (1)
	a is b
```
- 25: What does this script print?
```
	a = (1, 2)
	b = (1, 2)
	a is b
```
- 26: What does this script print?
```
	a = ()
	b = ()
	a is b
```
- 27: Will the last line of this script print `139926795932424`?
```
	>>> id(a)
	139926795932424
	>>> a
	[1, 2, 3, 4]
	>>> a = a + [5]
	>>> id(a)
```
- 28: Will the last line of this script print `139926795932424`?
```
	>>> a
	[1, 2, 3]
	>>> id (a)
	139926795932424
	>>> a += [4]
	>>> id(a)
```
- 29: *insert link*
- 30: function that returns a string n times the number of the iteration
- 31: class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`
- 32: Assuming we are using a CPython implementation of Python3 with default options/configuration:
```
a = 1
b = 1
```
How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)\
How many int objects are created by the execution of the second line of the script (`103-line2.txt`)
- 33: Assuming we are using a CPython implementation of Python3 with default options/configuration:
```
a = 1024
b = 1024
del a
del b
c = 1024
```
How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)\
How many int objects are created by the execution of the second line of the script (`104-line2.txt`)\
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (`104-line3.txt`)\
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (`104-line4.txt`)\
How many int objects are created by the execution of the last line of the script (`104-line5.txt`)
- 34: Assuming we are using a CPython implementation of Python3 with default options/configuration:
```
print("I")
print("Love")
print("Python")
```
Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (`105-line1.txt`)
- 35: Assuming we are using a CPython implementation of Python3 with default options/configuration:
```
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)\
How many string objects are created by the execution of the second line of the script (`106-line2.txt`)\
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (`106-line3.txt`)\
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (`106-line4.txt`)\
How many string objects are created by the execution of the last line of the script (`106-line5.txt`)
