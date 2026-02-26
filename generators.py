#1
def count_up_to(n):
    for i in range(1, n+1):
        yield i

g = count_up_to(5)

for num in g:
    print(num)
#2
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for x in even_numbers(10):
    print(x)
#3
g = (i*i for i in range(5))

for x in g:
    print(x)