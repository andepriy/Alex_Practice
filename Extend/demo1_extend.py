# Extend:Extend method adds each element of the iterable to the list,it has taken only one argument.
# l1=[1,2,3,4,'python','java',12.0,True]
# print(l1)
# [1, 2, 3, 4, 'python', 'java', 12.0, True]
# l1 .extend([11,22,00,'html'])
# print(l1)
# [1, 2, 3, 4, 'python', 'java', 12.0, True, 11, 22, 0, 'html']
# Postive index: It will start "0".
x =[1,2,3,4,5,6,7]
# print(x)
# [1, 2, 3, 4, 5, 6, 7]
# print(x[0])
# 1
# print(x[2])
# 3
# print([x])
# [[1, 2, 3, 4, 5, 6, 7]]
# Nagative indexin:It will start with"-1".
a=[11,'python',22,12.0,True,'java',6+3j,74,"level's",55,'total','pavan','swapna']
# print(a)
# [11, 'python', 22, 12.0, True, 'java', (6+3j), 74, "level's", 55, 'total', 'pavan', 'swapna']
# print(a[-2])
# pavan
# print(a[-5])
# level's
# print(a[-12])
# python
# Slicing:The combination of starting value & ending value.
# A slice object is used to specify how to slice a sequence.
# x =[1,2,3,4,5,6,7,8,9,10]
# print(x[0:5])
# [1, 2, 3, 4, 5]
# print(x[2:8])
# [3, 4, 5, 6, 7]
# Index():To returne the indexing position of the speciffices values.
# If you want to know the index value of the any list, then you will use index method() to check the index position of the any value.
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(s)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(s.index(17))
# 16
# print(s.index(9))
# 8