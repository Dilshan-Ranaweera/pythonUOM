# python basics

## Python functions

### Empty Functions

Sometimes you may need to define a function with an empty body, one that does nothing. This is usually to act as a placeholder until the function is implemented at a later level. Anyhow, when you define empty functions you must use the pass statement.
```python 
def empty_func():
   pass
empty_func()
```
### Default Parameter
```markdown
In Functions defined with default parameters, if no argument is passed during the function call, a predefined default parameter is passed as the value for the function. Such parameters are specified in Python function definition in the <name>=<value>, format. This <value> becomes a default value for that parameter.
```
```python
def greet(name, msg="How are you?"):
   print(name + ", " msg)

greet("John")
greet("John", "Good Evening")
greet("Good Evening")
```
```markdown
John, How are you?
John, Good Evening
Good Evening, How are you?
>>>
You can see in the above examples, when any arguments are left out, the function assumes its default value.
```
### Arbitrary Arguments
In some function definitions, you will not know the exact number of arguments that need to be passed to the function during its call. In such situations you can use the *args syntax with the function definition.

```python
def add(*args):
    #sum() is an inbuilt function to sum up a list
    total=(sum(args))
    print("The sum : " ,total)

def greet(msg, *names):
    for name in names:
        print(msg + ", " + name)

#Calling add() function
add(1,4,5)

#Calling greet() function
greet("Hello","John","Maggie","Lucy")

The sum:10
Hello, John
Hello, Maggie
Hello, Lucy
>>>
```
### Docstrings
```markdown
The Docstrings are supposed to provide detailed documentation for a function. It can be composed of the function’s purpose, its list of arguments, its return values and any other information that the programmer thinks important to mention.

A docstring is added as the first statement in the body of a Python function. These need to be within quotation marks and the recommended convention to use the triple-quotes (in double quotes) as “”” docstring “”” . These can be on a single line or be multi lined as well. If the docstring fits on a single line both the opening and closing quotes should be on the same line.

We can also view the docstrings of built-in and user defined functions using the __doc___ attribute.
```
``` python
def calc(quantity, price):
    """Returns the product of quantity and price"""
    return quantity*price

print (calc.__doc__)

Returns the prodcut of quantity and price
>>>
```
Docstrings seem to be similar to the commenting. But the difference is that comments are not accessible for viewing during the program execution. And the purpose docstrings serve is different, they are in fact a more useful way of commenting.
```python
>>> print(print.__doc__)
```
