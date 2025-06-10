def listSum(lst):
    s = 0
    for elements in lst:
        s += elements
    return s
#print(listSum[5,4,3])
#print(listSum(5))

def strangelist(n):
    strangelist = []
    for i in range(0 ,n):
        strangelist.insert(0,i)
        return strangelist
print(strangelist(5))