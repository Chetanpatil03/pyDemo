import os
import fnmatch

def search(direc, patt):
    match=[]
    for root, dir, files in os.walk(direc):
        for file in fnmatch.filter(files,patt):
            match.append(os.path.join(root,file))
    return match

Dir = input("Enter Directory :: ")
Patt = input("Enter Patterns (*.pdf) / File ::")

found = search(Dir,Patt)

if found:
    print("File found ::")
    for f in found:
        print(f)
else:
    print("Not found")