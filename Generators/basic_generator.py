
def gen(n):
    for i in range(n):
        yield i
        
g=gen(5)
for i in g:
    print(i)