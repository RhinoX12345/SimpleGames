import math
import random
import datetime as dt

def randoGenerate():
    def shuffle(arr, ref):
        def randShuffle(arr):
            for i in range(len(arr)*5):
                if round(random.random())==1:
                    temp = arr[i%len(arr)]
                    arr[i%len(arr)] = arr[(i+1)%len(arr)]
                    arr[(i+1)%len(arr)] = temp
            return arr
        def create(possible):
            for i in possible[0]:
                for j in possible[1]:
                    if j in [i]:
                        continue
                    for k in possible[2]:
                        if k in [i,j]:
                            continue
                        for l in possible[3]:
                            if l in [i,j,k]:
                                continue
                            for m in possible[4]:
                                if m in [i,j,k,l]:
                                    continue
                                for n in possible[5]:
                                    if n in [i,j,k,l,m]:
                                        continue
                                    for o in possible[6]:
                                        if o in [i,j,k,l,m,n]:
                                            continue
                                        for p in possible[7]:
                                            if p in [i,j,k,l,m,n,o]:
                                                continue
                                            for q in possible[8]:
                                                if q in [i,j,k,l,m,n,o,p]:
                                                    continue
                                                return [i, j, k, l, m, n, o, p, q]
        
        possible = []
        for i in range(len(arr)):
            temp = [1,2,3,4,5,6,7,8,9]
            for j in range(len(ref)):
                if ref[j][i]!=0:
                    temp.remove(ref[j][i])
                else:
                    break
            possible.append(temp)
        for i in range(len(possible)):
            possible[i] = randShuffle(possible[i])
        c = create(possible)
        return c
    
    b = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for l in range(0,9):
        while True:
            c = shuffle([1,2,3,4,5,6,7,8,9], b)
            term = True
            for i in range(0, 9):
                for j in range(0, 9):
                    if c[i] == b[j][i]:
                        term = False
                for j in range(math.floor(l/3)*3, l):
                    if c[i] in [b[j][i-i%3+0], b[j][i-i%3+1], b[j][i-i%3+2]]:
                        term = False
            if term:
                break
        b[l] = c
    b = [item for sublist in b for item in sublist]
    
    mapping = {}
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            mapping[f"{j}{i}"] = count
            count += 1
    
    ans = ""
    for i in b:
        ans+=str(i)
    
    r = False
    while r != True:  # Basic method
        t = int(dt.datetime.now().strftime("%S"))
        i = 0
        while True:
            i+=1
            if i>60:
                r = True
                break
            rand1 = random.randint(0, 80)
            while b[rand1] == 0:
                rand1 = random.randint(0, 80)
            rand2 = random.randint(0, 80)
            while b[rand1] == 0 and rand1 == rand2:
                rand2 = random.randint(0, 80)
            
            hold1 = b[rand1]
            hold2 = b[rand2]
            b[rand1] = 0
            b[rand2] = 0
            key = ""
            for j in b:
                key += str(j)
            
            r = checkUnique(key, 1)
            print(i, r, int(dt.datetime.now().strftime("%S"))-t > 3)
            if r != True:
                b[rand1] = hold1
                b[rand2] = hold2
                if (int(dt.time().strftime("%S")) - t) > 3:
                    key = ""
                    for j in b:
                        key += str(j)
                    r = checkUnique(key, 1)
                    break
                i-=1
            else:
                t = int(dt.datetime.now().strftime("%S"))
    key = ""
    for i in b:
        key+=str(i)
    return key
    
def checkUnique(key, n=0):
    b = []
    map = []
    for i in range(len(key)):
        b.append(int(key[i]))
        if key[i]=="0":
            map.append(i)
    def solver1(key):
        b = []
        for i in key:
            b.append(int(i))
        check = True
        for i in range(0,9):
            test1 = [1,2,3,4,5,6,7,8,9]
            test2 = [1,2,3,4,5,6,7,8,9]
            for j in range(0,9):
                if b[i*9+j]==0:
                    continue
                if b[i*9+j] in test1:
                    test1.remove(b[i*9+j])
                else:
                    check = False
            for j in range(0,9):
                if b[j*9+i]==0:
                    continue
                if b[j*9+i] in test2:
                    test2.remove(b[j*9+i])
                else:
                    check = False
            g = math.floor(i/3)*27+i%3*3
            test3 = [1,2,3,4,5,6,7,8,9]
            for j in range(0,3):
                for k in range(0,3):
                    if b[g+j*9+k]==0:
                        continue
                    if b[g+j*9+k] in test3:
                        test3.remove(b[g+j*9+k])
                    else:
                        check = False
        if check==True:
            return ["Success"]
        else:
            return ["Incorrect"]
    def recurse(mt, bt, key, n):
        print("|"*n)
        while True:
            count = 0
            for i in mt:
                c = 0
                iter = [1,2,3,4,5,6,7,8,9]
                g = math.floor(i/27)*27+math.floor((i%9)/3)*3
                for j in range(0,3):
                    for k in range(0,3):
                        if (g+j+k*9!=i and iter.count(bt[g+j+k*9])!=0):
                            iter.remove(bt[g+j+k*9])
                for j in range(0,9):
                    if (i-i%9+j!=i and iter.count(bt[i-i%9+j])!=0):
                        iter.remove(bt[i-i%9+j])
                    if (i%9+9*j!=i and iter.count(bt[i%9+9*j])!=0):
                        iter.remove(bt[i%9+9*j])
                if len(iter)==1:
                    bt[i] = iter[0]
                    mt.remove(i)
                    count+=1
                if len(iter)==0:
                    return False
            if count==0:
                break
        if len(mt)>0:
            iter = [1,2,3,4,5,6,7,8,9]
            g = math.floor(mt[0]/27)*27+math.floor((mt[0]%9)/3)*3
            for j in range(0,3):
                for k in range(0,3):
                    if (g+j+k*9!=mt[0] and iter.count(bt[g+j+k*9])!=0):
                        iter.remove(bt[g+j+k*9])
            for j in range(0,9):
                if (mt[0]-mt[0]%9+j!=mt[0] and iter.count(bt[mt[0]-mt[0]%9+j])!=0):
                    iter.remove(bt[mt[0]-mt[0]%9+j])
                if (mt[0]%9+9*j!=mt[0] and iter.count(bt[mt[0]%9+9*j])!=0):
                    iter.remove(bt[mt[0]%9+9*j])
            for j in iter:
                copy = bt.copy()
                copy[mt[0]] = j
                test = ""
                for k in copy:
                    test += str(k)
                r = solver1(test)
                s = r[0]
                if s=="Success":
                    mt2 = mt.copy()
                    mt2.pop(0)
                    a = recurse(mt2, copy, key, n+1)
        else:
            check = True
            for i in range(0,9):
                test1 = [1,2,3,4,5,6,7,8,9]
                test2 = test1.copy()
                for j in range(0,9):
                    try:
                        test1.remove(bt[i*9+j])
                        test2.remove(bt[j*9+i])
                    except:
                        check = False
                g = math.floor(i/3)*27+i%3*3
                test = test1.copy()
                for j in range(0,3):
                    for k in range(0,3):
                        try:
                            test.remove(bt[g+j*9+k])
                        except:
                            check = False
            t = ""
            for i in bt:
                t+=str(i)
            solutions.append(t)
    solutions = []
    recurse(map, b, key, 1)
    if n==0:
        if len(solutions)==0:
            return "No Solutions"
        elif len(solutions)==1:
            return f"1 Unique Solution: \n{solutions[0]}"
        elif len(solutions)>1:
            return f"Multiple Solutions: {len(solutions)}"
    else:
        return len(solutions)==1
    
#puzzle = randoGenerate()
puzzle = "800000000003600000070090200050007000000045700000100030001000068008500010090000400"
print(puzzle)
print(checkUnique(puzzle))
#print(checkUnique("500000000000860000000751020008007093002093500000180070007216000000000830000000000"))