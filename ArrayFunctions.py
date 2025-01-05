import array as arr

data = arr.array("i",[25,6,5,9,8,13,6,9,2,9])
print(data)

data.append(69)
print(data)

data.insert(0,19)
print(data)

print(f"Index of 8 is {data.index(8)}")
print(f"count of 6 is {data.count(6)}")

data.remove(9)
print(data)

data.pop(0)
print(data)