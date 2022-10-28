x = 2


def f():
    print(x)  # Error
    x = 3
    print(3)


f()
"""
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: local variable 'x' referenced before assignment
>>>
"""

# whitn the body of a function all the x's all the same name
# have to refer to the same frame.

# 因为 python 的语法特征 这其实是一种混淆 等价的Go表达如下
# package main

# import "fmt"

# func main() {
# 	var x = 2 // x declared but not used
# 	f()
# }
# func f() {
# 	fmt.Println(x) // undecalred name：x
# 	x:=3
# 	fmt.Println(x)

# }
""" global variable """
x = 2


def f(x):
    print(x)  # global variable
    x = 3  # local variable
    print(3)


f(x)