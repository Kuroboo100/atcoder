def f():
    m.append(1)

def main():
    global m
    m=[1,2,3]
    f()
    return m

print(main())