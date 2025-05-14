def pro(n):
    l1=list(n)
    m=1
    for a in l1:
        m=m*a
    return m

n=(50,20,30,60)
print("Tuple",n)
print("Product:",pro(n))