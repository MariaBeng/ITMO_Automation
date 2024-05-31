# def task(a=(1, 2, 3, 4)):
#     return a[1]
#
# print(task())
#
# # def task1(r, pi=3.14159):
# #     return pi * r * r
# #
# # print(task1(2))
# a: int = 5
# b: float = 3.5
# c: str = 'meow'
# d: list = [1,2]
# e: bool = True
# def task_1(a: int, b: float, c: str, d: list, e: bool):
#     return a,b,c,d,e
#
# print(task_1(5, 3.5, 'meow', [1,2], True))


def task_2(a= [1,2,3,5,8,13,21]):
    return a[0:3]

print(task_2())



def task_3(a):
    return a * a

print(task_3(3))


# def task_1(a=5,b=3.5,c='meow',d=[1,2],e= True):
#     return  type(a), type(b), type(c), type(d), type(e)
#
# print(task_1())

a: int  = 5
b: float = 3.5
c: str = 'meow'
d: list = [1, 2]
e: bool = True

def task_1():
    return a,b,c,d,e
print(task_1())
def task_1():
       return type(a), type(b), type(c), type(d), type(e)
print(task_1())




