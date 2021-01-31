import sys
infile = open(sys.argv[1],"r")
rows = []
for i in infile:
    i = i.rstrip("\n")
    i = i.split(" ")
    rows.append(i)
def Check(): ## check if there is any column or row which is totally null
    for ii in rows:
        if ii.count(" ") == len(ii):
            rows.pop(rows.index(ii))
    x = -1
    while True:
        if x > 50:
            break
        x+=1
        temp = []
        try:
            if len(rows) == 1:
                temp.append(rows[0][x])
            else:
                for j in rows:
                    temp.append(j[x])
            if temp.count(" ") == len(temp):
                for k in rows:
                    ind = rows.index(k)
                    k.pop(x)
                    rows[ind] = k

        except:
            break

def Check2(): ## to check if there exists any possible value which has neighbour
    a = 0
    while True:
        try:
            abcc = 0
            for t in rows[a]:
                if len(neighfinder([a,abcc])) != 0:
                    return True
                abcc += 1
            a += 1
        except:

            return False

def Check3(): ## Deleting spaces in columns(or shifting to down)
    h = 0
    while True:
        if h > 50:
            break
        try:
            tmp, aa = [], []
            for tr in rows:
                tmp.append(tr[h])
            tmp2 = tmp[:]
            lenght = len(tmp) - 1
            for ty in tmp:
                try:
                    ty = int(ty)
                    aa.append(str(ty))
                    tmp2.remove(str(ty))
                except:
                    pass
            for tg in aa:
                tmp2.append(tg)
            tmp2.reverse()
            for tt in rows:
                tt[h] = tmp2[lenght]
                lenght -= 1
            h += 1
        except:
            break

def neighfinder(loc):  ## obviously by name it finds  a value's neigbnour if has same value
    loc1,loc2 = int(loc[0]),int(loc[1])
    founds = []
    value = rows[loc1][loc2]
    if value == " ":
        return founds
    try:
        if loc2 == 0 :
            pass
        elif rows[loc1][loc2-1] == value:
            founds.append([rows[loc1][loc2-1],loc1,loc2-1])
    except:
        pass
    try:
        if rows[loc1][loc2+1] == value:
            founds.append([rows[loc1][loc2+1],loc1,loc2+1])
    except:
        pass
    try:
        if loc1 == 0 :
            pass
        elif rows[loc1-1][loc2] == value:
            founds.append([rows[loc1-1][loc2], loc1-1, loc2])
    except:
        pass
    try:
        if rows[loc1+1][loc2] == value:
            founds.append([rows[loc1+1][loc2],loc1+1,loc2])
    except:
        pass
    return founds
def Func(loc): ## main function of this program. It uses other functions and executes the progress
    Neigh = []
    valu = rows[loc[0]][loc[1]]
    if valu == " ":
        return "sit1"
    elif len(neighfinder(loc)) == 0: # to check if our value has no neighbour
        return "sit2"
    else:
        Neigh.extend(neighfinder(loc))
        for ab in Neigh:
            if len(neighfinder([ab[1],ab[2]])) != 0:
                for cd in neighfinder([ab[1],ab[2]]):
                    if cd not in Neigh:
                        Neigh.append(cd)
    dic1 = dict()
    for el in Neigh:
        if str(el[1]) in dic1.keys():
            dic1[str(el[1])] = str(dic1[str(el[1])])+str(el[2])
        else :
            dic1[str(el[1])] = str(el[2])
    for tx in dic1.keys():
        for jk in sorted(dic1[tx],reverse=True):
            rows[int(tx)][int(jk)] = " "
    return Fibonacci(len(Neigh))*int(valu)

def Fibonacci(number,count=1,aaa=1,bbb=1):
    if count == number:
        return aaa
    else:
        bbb = aaa+bbb
        aaa = bbb-aaa
        return Fibonacci(number,count+1,aaa,bbb)

score = 0
while True: ## loop of a game ,it continues until there is no neighbour left.
    Check()
    Check3()
    if not Check2():
        for de in rows:
            print(*de)
        print("\nYour Score is : ", score,"\n")
        print("&&& Game Over &&&")
        break
    else:
        for de in rows:
            print(*de)
        print("\nYour score is: ", score, "\n")
        inp = (input("Please enter a row and column number: "))
        row, col = int(inp.split(" ")[0])-1, int(inp.split(" ")[1])-1
        try:
            val = rows[row][col]
        except:
            print("Your input is out of bounds!\n")
            continue
        result = Func([row, col])
        if result == "sit1":
            print("\nPlease enter a correct size!\n")
        elif result == "sit2":
            pass
        else:
            score = score+result
            Check()
            Check3()