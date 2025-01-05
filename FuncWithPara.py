def add(a,b):
    def summ(a):
        return sum(a)
    
    def Summ(b):
        return sum(b)
    
    return summ(a) + Summ(b)

def sayhello():
    print("Hello from funcntion")

def say(a="chetan", b="Bunty"):
    print(f"First : {a}, Second {b}")


a=[15,563,6,8,14,6]
b=[i for i in range(1,11)]
print(add(a,b))

say()
sayhello()

