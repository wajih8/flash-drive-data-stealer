from pickle import load
import shutil
with open("das.dat", "r")as f:
    a=f.readline(-1)

with open("das.dat", "rb")as f:
    x = (load(f))
    for i in x:
        xa = (i["original"])
        while xa.find('\\') != -1:
            xa = xa[xa.find('\\')+1:]
        shutil.copy(i["fake"], a+xa)
        print(i["fake"][-24:])
