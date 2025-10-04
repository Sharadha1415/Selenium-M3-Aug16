# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
# add(1, 2)





def sample():
    name = 'Shailaja'
    yield name
    yield '100'
    yield True
    yield 'python'
    yield 10

res = sample()
print(res)

for ele in res:
    print(ele)

































