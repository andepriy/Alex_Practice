# Index():Search the tuple for a specified value and return the position of where it was found.
# t1=(1,2,3,4,5,6,7,'python','jango','sure',12)
# print(t1.index(1))
# o
# print(t1.index(3))
# 3

# ex:
# x=(1,2,3,4,5,6,11,'ee',2,3,44,55,66)
# print(x.index(66))
# 12
# a='cool'
# print(a.index('o',2,10))
# 2
# b='swapna'
# print(b.index('a',3,10))
# 5

# s={}
# print(s)
# {}
# print(type(s))
# <class 'dict'>

# SET:In python, we create sets by placing all the element inside curly braces{},separated by comma.
# s={1}
# print(s)
# {1}
# print(type(s))
# <class 'set'>

# ex:1
# s1={1,2,3,4,5,6,'mango',2.3,'list',"tuple",'list',3+5j,2.3,True,False}
# print(s1)
# SET is a unorder datatype
# {False, 1, 2, 3, 4, 5, 6, 2.3, 'mango', (3+5j), 'tuple', 'list'}

# Set doesn't allows duplicate values.
# s2={1,2,3,4,4,5,6,6,'mango',2.3,'list',"tuple",'list',3+5j,2.3,True,False}
# print(s2)
# {'list', 1, 2, 3, 4, 5, 6, 2.3, False, (3+5j), 'tuple', 'mango'}

x1={'chithanya','rajesh','priya','arif'}
# print(x1)
# {'rajesh', 'priya', 'chithanya', 'arif'}
# x1.add('python')
# print(x1)
# {'priya', 'python', 'chithanya', 'arif', 'rajesh'}
# x1.add('acer','hp')
# print(x1)
# TypeError: set.add() takes exactly one argument (2 given)

x1.update({'nokia','sony'})
print(x1)
# {'rajesh', 'chithanya', 'arif', 'sony', 'nokia', 'priya'}