# type casting in Python

a="123"
print(type(a))  # Output: <class 'str'>

b=int(a)
print(type(b))  # Output: <class 'int'>

x=float(4+3.4)
print(type(x))  # Output: <class 'float'>  
print(x)

y=str(45)
print(type(y))  # Output: <class 'str'>
print(y)

z=bool(0)
print(type(z))  # Output: <class 'bool'>
print(z)

w=bool(5)
print(type(w))  # Output: <class 'bool'>
print(w)    


# In Python, the following values are considered False:
# None
# False
# Zero of any numeric type: 0, 0.0, 0j
# Empty sequences and collections: '', (), [], {}
# All other values are considered True.
print(bool(""))  # Output: False
print(bool([]))  # Output: False
print(bool(()))  # Output: False
print(bool({}))  # Output: False
print(bool(0))   # Output: False
print(bool(0.0)) # Output: False

d=bool("Hello")
print(type(d))  # Output: <class 'bool'>
print(d)    # Output: True

g=complex(3,4)
print(type(g))  # Output: <class 'complex'>
print(g)    # Output: (3+4j)