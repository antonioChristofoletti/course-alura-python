# Course Alura Python
Learning about Python.

## Highlights

- It is compiled and interpreted at the same time;
- Simplified languages, It is not necessary `{}` or `;`;
- The indentation defines scope, so It is mandatory to work correctly;
- weakly typed;

## Modeling Manage

It allows raw code that execute something or methods, classes and so on. Pretty much as Javascript.

It is possible define which function It is going to be called, if the module (file) be executed alone. Example:

```
if __name__ == "__main__":
    foo()
```

Importing modules is simples just as in others languages. Example:

```

import random
import foo

```

Using example:

```
random.randrange(1, 101)
foo.method_foo(args)
```

## Types

### String

- It is immutable, good for memory optimization. Since It is immutable, stuff like `string_foo[2] = 'C'` is strictly prohibit (Throw errors)
```
  string_a = 'abc'
  string_b = 'abc'
  
  print(id(string_a) == id(string_b))
  # It is true because Python is smart and points string_b to the same allocated memory as string_a, 
  no harm in this because changing the value of this string is impossible.

```
- Concatenating: `"Printing string {} an value {:.2f}".format(var1, var2)`;
- Interpolating: `f"Interpoling a var {var1}"`
- Useful funs:
  - `lower`
  - `upper`
  - `strip`
  - `startwith`,
  - `endwith`,
  - `SubString/slicing:` (First parameter is inclusive, but the second is not)
    - `string_foo[0:3]` 
    - `string_foo[10:]` 
  - `find:` get the first index of a substring in the string

### Sequence Type

`List Comprehension`: way to iterate and transform a list. 

Example:

- `value * 2 for value in list_values`;
- `if value % 2 == 0 value*2 else value for value in list_values`;
- `value for value in list_values if value % 2 == 0`

#### List

Easy to create, It doesn't have a limited size. It allows, items with different types.

- Creating: list_foo = `[1, 2, 3, 5.3, "String foo"]`
- Lowest value: `min(list)`
- Biggest value: `max(list)`
- Length: `len(list)`
- add item: `list.append(item)`
- remove item: ``
- Quantity of a specific item: `list.count("value")`
- First index in the list: `list.index("value"")`
- Check if a value is in the list: `value in list` or `value not in list`

#### Set

Sequence of unique values. Does not allow equals values.

- Creating: `set_foo = {1,2,3,4}`.
  - Empty `{}` does not create an empty set, but an empty dictionary. Uses `set()`
- Share most part of the common methods found in List.
- Converting list to set: `set(list)`
- Computing standard math operations such as union, intersection, difference, and symmetric difference.
- It does not have indexes, since It is an unordered list.

#### Duple

Immutable sequence list. Faster and more efficient than traditional list.

- Creating: `duple_foo = (1,2,3)`
- Share most part of the common methods found in List.

#### Array

Python has an array type which can be used for performance, however, even so, generally using the array type from numpy dependencies is more common.
So, try avoid it using the pure array, numpy is a better option.

Example native aray:
```
  import array as arr
  arr.array("d", [1, 3.5]) # array just accept one data type, so It is necessary pass as argument "d" (for numbers)
```

Example array numpy:
```
  import numpy as np
  numbers = np.array([1, 3.5])
```

#### Interesting stuff

##### Builtins enumarate

enumarate returns the list/tuple with the numeric index, It is a lazy function.

Example:

```
  students = (("Antonio", 23), ("Pedro", 33))
  
  for student in enumarate(students):
    print(f"Index {student[0]} - Student {student[1]}"
```

##### Unpacking tuple

It can be more than 2 elements whether necessary.

Example:

```
  students = (("Antonio", 23), ("Pedro", 33))
  
  for index, student in enumarate(students):
    print(f"Index {index} - Student {student}"
```

#### Sorting

```
# Simple sorting

foo_list = [30, 10, 20]

sorted(foo_list)
sorted(foo_list, reverse=True) or list(reversed(foo_list))
foo_list.sort()

# Sorting objects

foo_list_bank_account = [bank_acc_01, bank_acc_02, bank_acc_03, bank_acc_04]

sorted(foo_list_bank_account, key=function_that_reduce_the_object_to_a_comparatible_value)
sorted(foo_list_bank_account, key=attrgetter("attribute_compare"))

# Implement the methods:
# It means lesser than
def __lt__(self, other):
  return self.attr < other.attr
  
# Than
  sorted(foo_list_bank_account)
  
# Important implement in the class thwe total_ordering from functools to suport others comparasion: >=, <=
```

### Dictionary

- Creating: `dict_foo = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}`
- Using key to access value: `dict_foo['Flavio']`

### Null

Null in Python is known as None and It is a object of the class NoneType. All the Nones are pointed to the same object 
and It is not possible create new object of this class.

### Casting values to bool

It is possible realize an implicit conversion to bool. Examples:

```
  if "test":
    do this...
```

Empty `dict`, `list`, `duple` and `string` and the value `0` are convert to `False`, otherwise, It is converted to `True`.

## Input/Output File

There is no secret.

-> Open: `file_foo = open("filepath", access_modifier`;
  -> Access Modifier:
    - w: write and override;
    - a: append;
    - r: just read;
    - b: binary (For example images).

-> Write: `file_foo.write(string_foo)`;
-> Read: 
  - Iterate: `line in file_foo`
  - Read whole file: `file_foo.read()`
  - Read a line: `file_foo.readline()`
-> Close: `file_foo.close()`.
-> Working and then closing automatically:
  - ```
        with open("file_foo.txt", "r") as fileFoo:
        linesList = [line for line in fileFoo if fileFoo.strip() != ""]
    ```
  

## OOP

### Refreshing OOP

-> Data and behavior walk together;
-> Define rules and creates a universal languages to deal with objects and concepts from the real world;
-> avoid repeating code, centralize business rules;
-> Defines a template/pan for the objects;
-> Extending vs composition: Two types of data/behaviors inheritance: Extending generally is good, even so, It brings
a heavy coupling which can become a nightmare. In the other hand, composition allows integrating with less coupling, but It might
encourage code repetition. It is important think on this during inheritance relation creation

### Highlights

-> Python does not allow multiple constructor methods;
-> Accessing methods and attributes is the same as others languages;
-> all the methods need to have a parameter self which is a reference for the object. 
-> Python doesnot have Interfaces, It uses the concept of Duck Typing.

### Syntax

Similar to others languages. Example:

```
class Account:
  pass

# inheritance
class SavingAccount(Account):
  
  STATIC_ATTRIBUTE = 100
  
  #Constructor
  def __init__(self, specific_attributes...):
    
    # private attributes start with __
    self.__attr1 = attr1
    self.attr2 = attr2
    
  #Method
  def method_1(self, params_here....)
    pass
    
  @property
  def your_attribute_name(self):
    return self.__your_attribute_name

  @your_attribute_name.setter
  def your_attribute_name(self, your_attribute_name):
    self.__your_attribute_name = your_attribute_name
    
  @staticmethod
  def your_static_method(self)
    pass
  
  @classmethod
  def class_method_that_receives_a_instance(cls):
    pass
```

### Functions

It has traditional plain methods, static methods and class methods.
Static methods are generally used for utility and to demonstrate that a specific function will not change a object.
Class methods could be used for factory object pattern and also to change properties related to the class.

### Encapsulation

Access Attributes mainly through methods: `use properties (Check syntax topic above)`

Methods: `def _private_method_foo(self, params...)` or `def __private_method_foo(self, params...)`

Attributes: `self.__attr1 = attr1` or `self._attr1 = attr1`

obs.:
Double underline It is still possible to access from outside, using obj._ClassName__attribute_name
Having this in mind, using just one underline is enough, however, It is just a consensus and just one underline has no meaning to the language as double underline.
Double underline can be problematic in inheritance.

### Python Data Model

Methods that works as an API to make objects work with idiomatic languages features.
You can think of the data model as a description of Python as a framework.  It formalizes the interfaces of the 
building blocks of the language itself, such as sequences, iterators, functions, classes, context managers, and so on.

These methods are also known as magic methods. They don't need to ve invoke because the python is going to use it. Examples:

- `__str__` work just as toString() in Java;
- `__eq__` check if 2 objects are considered the same. It allows idiomatic language feature like `object1 == object2`
- `__lt__` used for sorting and checking if a object is bigger or smaller than others
- `__repr__` prints an object in a nice way for debugging;
- `__getitem__` works as a Java Iterador Interface, however more powerful, It is a communication channel in order to allow python syntax resources, such as:
  - something `in` your_object
  - your_object[0]
  - for i `in` your_object.
- __init__ construtor;
- There are many others

### ABC (Abstract Basic Classes)

Default abstract classes that python provides in order to define better the idea of strong typing, structured-code and also avoid recreation of these common classes.
Differently of others languages, abstract classes might have abstract methods with implementation that can be reused whether necessary.

Example:

```
from collections.abc import Sized

class MyCustomList(Sized):
    def __init__(self, description):
        self.descricao = description

    def __str__(self):
        return self.description
        
    def __len__(self):
        return len(self.list)

list = MyCustomList()
print(list)
```

### Multiple inheritance

It is allowed. Just need to add the parent classes separate by a ','. Example:

```
class A:
    def a(self):
        print('a')

class B:
    def b(self):
        print('b')

class C(A, B):
    def d(self):
        print('C')
```

Python has an algorithm in order to find which parent class has the specific resource that the object wants to call.

Ultra basic narrowed down explanation:
1- if the object does not have the resource is going to check the inherited classes;
2- The checking is always from the left to the right, so the order matters;
3- Check all the classes in the same level and then check the parents classes and then parent's parents classes and go on, always looking from the left to the right;

### Mixin

**Explanation from stackoverflow: https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful**

A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

- You want to provide a lot of optional features for a class.
- You want to use one particular feature in a lot of different classes.

For an example of number one, consider werkzeug's request and response system. I can make a plain old request object by saying:

```
class Request(BaseRequest):
    pass
```

If I want to add accept header support, I would make that

```
from werkzeug import BaseRequest, AcceptMixin

class Request(AcceptMixin, BaseRequest):
    pass
```

If I wanted to make a request object that supports accept headers, etags, authentication, and user agent support, I could do this:

```
from werkzeug import BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin

class Request(AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin, BaseRequest):
    pass
```

The difference is subtle, but in the above examples, the mixin classes weren't made to stand on their own. 
In more traditional multiple inheritance, the AuthenticationMixin (for example) would probably be something more like Authenticator. 
That is, the class would probably be designed to stand on its own.