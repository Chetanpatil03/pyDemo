a=14
b=85
def func():
    global a
    a=19
    b=47
    print(a)
    print(b)

print(a)
func()
print(a)
print(b)
