"""String :
string is immutable ,modifications can not be made"""
# a="python"
# print(a,type(a))
# print(a[0])
# a[0]='P'

# print(dir(str))


# n="hEllo PyThon"
# print(n.capitalize())


# name="hEllo PyThon"
# print(name.casefold())
# print(name.lower())

# name="hEllo PyThon"
# print(len(name))
# print(name.index('h'))
# print(name.upper())
# print(name.lower())

# 2ab="4_hello python"
# print(n.count('l'))
# prnt(n.enidswith(n))
# print(n.index('o'))
# print(n.rindex('n'))
# print('2ab'.isidentifier())

# print('ab'.isidentifier())

# n="   hello sreeja ,  "
# print(n.strip())
# print(n.rstrip())
# print(n.lstrip())
# c="Python Programing"
# print(c.removeprefix('p')) 
# print(c.removeprefix('P'))
# print(c.removesuffix('ing'))

# name="hEllo pyThon"
# n=name.encode()
# print(n)
# n=name.decode()
# print(n)
# print(name.title())
# print(name.capitalize())
# print(name.istitle())

# c='Hello Python'
# print(c.istitle())
# print(c.index('h'))
# print(c.count('h'))

# s="hEllo pyThon"
# print(s.endswith(''))
# print(s.endswith(' '))
# print(s.endswith('n'))

# s="hEllo pyThon"
# print(s.startswith(''))
# print(s.startswith(' '))
# print(s.startswith("h"))


# s=" hEllo pyThon"
# print(s.startswith(''))
# print(s.startswith(' '))
# print(s.startswith(' h'))
# print(s.startswith('h'))

# v=''
# print(v.isspace())
# c=' '
# print(c.isspace())
# a='  '
# print(a.isspace())
# g='n'
# print(g.isspace())


'''tupple'''


# a=11,'hi',2.4
# print(a.index(11))

# a=1,2,6,3.3,3333.3,'jhbfio','hdbjugr',4
# print(a.count(2))

'''set'''

# a={}
# print(a,type(a))

# a={1,2,2}
# a.clear()
# print(a)

# a={2,4,3.3,3}
# b=3,'hi',3.4
# a.add(b)
# print(a)

# a={2,4,3.3,3}
# b={3,'hi',3.4}
# print(a.difference(b))


a={2,4,"hi",3.3,3}
b={3,'hi',3.4}
c={3,4,3.4}
print(a.intersection(b))
