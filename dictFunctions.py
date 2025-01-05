d = {1:"Java",2:"Python",3:"PHP"}
print("Original : ",d)

print(d.get(1))
print(d.items())
print(d.values())
print(d.keys())

d2 = d.copy()
print("Original : ",d)
print("Copied : ",d2)

d2.update({2:"C++"})#update existing
print(d2)

d2.update({4:"Python"})
print(d2)

d2.pop(3)
print(d2)

d2.popitem()
print(d2)

d2.clear()
print(d2)

marks = [19,18,19,17]
stud = ["Chetan","Prafulla","Bhavesh","Prakash"]

dic = {stud[i]:marks[i] for i in range(len(stud))}
print(dic)