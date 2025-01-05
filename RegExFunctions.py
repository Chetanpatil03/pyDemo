import re


txt = "The rain in spain"
a=re.search("ai",txt)
print(a.start())

b=re.findall("ai",txt)
print(b)

c=re.split("\\s",txt)
print(c)

d=re.sub("spain","India",txt)
print(d)