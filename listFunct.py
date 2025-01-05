ls = [65,57,9,5,8,5,62,89,5]
print("Original : ",ls)

ls.append(10)
print(ls)

ls.insert(0,4)
print(ls)

print("Index of 8 : ",ls.index(8))
print("count of 5 : ",ls.count(5))

ls2 = ls.copy()
print(f"List 1 : {ls}")
print(f"List 2 : {ls2}")

ls2.sort()
print(ls2)

ls.reverse()
print(ls)

ls.remove(8)
print(ls)

ls.pop()
print(ls)

ls.pop(2)
print(ls)

ls.clear()
print(ls)