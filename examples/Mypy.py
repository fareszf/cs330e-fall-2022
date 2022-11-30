"""
Potential benefits of mypy-style static typing:
Static typing can make programs easier to understand and maintain. Type declarations can
serve as machine-checked documentation. This is important as code is typically read much
more often than modified, and this is especially important for large and complex programs.
Static typing can help you find bugs earlier and with less testing and debugging. Especially in
large and complex projects this can be a major time-saver.

Static typing can help you find difficult-to-find bugs before your code goes into production. This
can improve reliability and reduce the number of security issues.

Static typing makes it practical to build very useful development tools that can improve
programming productivity or software quality, including IDEs with precise and reliable code
completion, static analysis tools, etc.

You can get the benefits of both dynamic and static typing in a single language. Dynamic typing
can be perfect for a small project or for writing the UI of your program, for example. As your
program grows, you can adapt tricky application logic to static typing to help maintenance.
-http://mypy.readthedocs.io/en/latest/faq.html
-------------
Install mypy "pip install mypy"

Mypy will type check your code statically: this means that it will 
check for errors without ever running your code, just like a linter.

if you try directly running mypy on your existing Python code, 
it will most likely report little to no errors: you must add type 
annotations to your code to take full advantage of mypy. 
"""
"""
Dynamically Typed Hello World 
(A function without type annotations is considered to be dynamically typed by mypy) 
By default, mypy will not type check dynamically typed functions. 
"""
def hello(name):
   return 'Hello ' + name

print(hello('World'))

"""
Statically Typed Hello World
You can teach mypy to detect these kinds of bugs by adding 
type annotations (also known as type hints).
"""
def s_hello(name: str) -> str:
   return 'Hello ' + name

print(s_hello('World'))

try :
   print(hello(1)) #Type Check Error
except TypeError :
   pass

try :
   print(s_hello(1)) #incompatible type "int"; expected "str"
except TypeError :
   pass


from typing import Any
def one():
   return 1
def two() -> int:
   return 2
def three() -> None: #Does not expect return value
   return 3
def four() -> str: #Expects string; Returns integer
   return 4
def five() -> Any:
   return 5

a = one()
print(a)
b= two()
print(b)
c = three()
print(c)
d = four()
print(d)
e = five()
print(e)
assert isinstance(e, int)

"""
Dynamically Typed Fibonacci Function
"""
def inc(n):
   x = n
   for i in range(0,x):
      yield i

nums = inc(5) #Dynamically Typed Variable
for num in nums:
   print(num)

"""
Statically Typed Fibonacci Function
"""
from typing import Iterator #imports specific types
def s_inc(n: int) -> Iterator[int]: #n must be int; output must be Iterator[int]
   x = n
   for i in range(0,x):
      yield i

nums = s_inc(5) #Statically typed variable
for num in nums:
   print(num)