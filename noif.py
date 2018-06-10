def div (x):
    a=["xxxxxx",x,x]
    b=a[x%3]
    return b
def div2 (x):

    a=["xxxxxxxx",x,x,x,x]
    b=a[x%5]

    return b
def fin(out,x):
    a=["Linianos","",x,"",x,"","","Linio","Linio","IT","IT"]
    b=a[len(out)%14]
    print b
array =[]
for x in range(100):
    out=""
    out=out+str(div(x))
    out=out+str(div2(x))
    

    fin(out,x)
    out=""
print "IT"
