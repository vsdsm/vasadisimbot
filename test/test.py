def f(x):
    return x>10


a = [10,4,5,1,66,33,888,3]

b = filter(f,a)
# print(b)
# print(*b)

b = list(b)
print(b)
