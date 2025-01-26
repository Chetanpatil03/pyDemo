a=14
b=85
def func():
    global a
    a=19
    print(a)

print(a)
func()
print(a)

