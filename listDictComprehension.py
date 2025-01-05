# ls=[i**2 for i in range(1,10)]
# print(ls)

# l=[i for i in range(1,21)if i%2==0 ]
# print(l)

# d={f"The square of {x}":x**2 for x in range(1,21)}
# print(d)

mark = [15,19,18]
st = ["Prafull","Bhavesh","Chetan"]
dc={st[i]:mark[i] for i in range(len(mark))}
print(dc)
