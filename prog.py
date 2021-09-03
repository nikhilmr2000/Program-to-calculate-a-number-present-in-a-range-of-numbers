#if 3 is found in a range of 100 and 200
#n=100,m=200,k=3
#Find the elements that contain 3 between 100 and 200
#sample output::: 103,113,123,130,131,132,133,134,135,136,137,138,139,143,153,163,173,183,193

n=int(input())
m1=int(input())
k=int(input())

s=""
l=[]
for i in range(n,m1):
    s+=str(i)
    p=len(s)
    lh=i
    k=0
    gh=i
    m=0
    while(k>=0):
        z=gh%10
        if(z==k):
            m=m+1
        gh=gh//10
        k=k+1
        if(k==p):
            break
    if(m>0):
        l.append(i)
    s=""
print(l)
 
