# Python Strings
Assume variable a holds 'Hello' and variable b holds 'Python', then:
## 1. + Operator 
 **Concatenation** - Adds values on either side of the operator
```python
>>> a + b
HelloPython
```
### 2. * Operator:
 **Repetition** - Creates new strings, concatenating multiple copies of the same string.
 ```python
 >>> a*2
HelloHello
```
### 3. [ ] : 
**Slice** - Gives the character from the given index.
```python
>>> a[1]
e
```
### 4. [ : ]: 
**Range Slice** - Gives the characters from the given range
```python
>>> a[1:4]
ell
```
### 4. in: 
**Membership** - Returns true if a character exists in the given string
```python
>>> H in a
True
```
### 5. not in: 
**Membership** - Returns true if a character does not exist in the given string
```python
>>> M not in a
True
```
### 6. r/R

**Raw String** - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark. 
```python
>>>print (r'\n')
\n

>>>print (R'\n')
\n
```
### 7. %: Format - Performs String formatting
One of Python's most useful features is the string format operator % (which we have used before). This operator is unique to strings. The following is an example. 
```python
>>> print("My name is %s and I am %d years old!" % ('Kumar', 20)) 
```

My name is Kumar and I am 20 years old!

Here is the list of complete set of symbols which can be used along with %:

|Format Symbol| Conversion|
|:------------:|:---------:|
|%c                      |character|
|%s |                        string conversion via str() prior to formatting|
|%i |                         signed decimal integer|
|%d                   |      signed decimal integer|
|%u                    |     unsigned decimal integer|
|%o          |               octal integer|
|%x                 |        hexadecimal integer (lowercase letters) |
|%X                 |       hexadecimal integer (UPPERcase letters) |
|%e                 |       hexadecimal integer (UPPERcase letters) |
|%E           |             exponential notation (with UPPERcase 'E')|
|%f           |              exponential notation (with UPPERcase 'E')|
|%g                     |   the shorter of %f and %e|
|%G                     |  the shorter of %f and %E|
