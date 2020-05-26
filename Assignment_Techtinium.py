
def knapSack(W, wt,k,m,h):
    l=0
    print("Machines:")
    for i in wt:
        if W>=i:
            x=W//i
            W=W%i
            l=l+(x*k[i])
            print(m[i],x)
    print("Total Cost:",l*h)
l=list(input().rstrip().split())
W=int(l[2])
h=int(l[5])
m={320:"10XLarge",160:"8XLarge",80:"4XLarge",40:"2XLarge",20:"XLarge",10:"Large"}
wt1 = [160,80,40,20,10]
k1={160:1400,80:774,40:450,20:230,10:120}
print("Output:[")
print("{")
print("Region:NewYork")
knapSack(W,wt1,k1,m,h)
print("}")
wt2 = [160,40,10]
k2={160:1300,40:413,10:140}
print("{")
print("Region:India")
knapSack(W,wt2,k2,m,h)
print("}")
k={160:1180,80:670,20:200,10:100}
wt = [160,80,20,10]
print("{")
print("Region:China")
knapSack(W, wt, k,m,h)
print("}")
print("}")
