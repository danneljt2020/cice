def generator():
    n = 1
    print('this is printed frist')
    yield n

    n += 1
    print('this is printed second')
    yield n


a = generator()

# next(a)
# next(a)
# using in loop
for item in generator():
    print(item)
