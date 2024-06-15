# T1
def Feibo(n):
    cou=1
    fou=1
    for i in range(2,n):
        tap=fou+cou
        fou,cou=cou,fou
        fou=tap
    return fou
n=int(input())
print(Feibo(n))
    
# T2
import time as t
St1=t.localtime()
St2=[St1.tm_year,St1.tm_mon,St1.tm_mday]
def IfdateY(n,m,d):
    R=[31,29,31,30,31,30,31,31,30,31,30,31]
    L=[31,28,31,30,31,30,31,31,30,31,30,31]
    cot=0
    if n%4==0 and n%100!=0 or n%400==0:
        for i in range(m-1):
            cot+=R[i]
        return cot+d
    else:
        for i in range(m-1):
            cot+=L[i]
        return cot+d
print(IfdateY(St2[0],St2[1],St2[2]))

# T3
lst=["Tom","Rose","小明","王强"]
def Redpac(lst):
    import random as r
    n=len(lst)
    p={}
    lt=0
    for i in range(n):
        nt=r.uniform(1,10)
        p[lst[i]]=nt
        if nt>lt:
            nn=lst[i]
            lt=nt
    print('最幸运的人：',nn)
    print(p)
Redpac(lst)

# T4
def oppo():
    name=input('请输入姓名：')
    num=input('请输入学号：')
    c1=input('第一门课的成绩：')
    c2=input('第二门课的成绩：')
    c3=input('第三门课的成绩：')
    return [name,num,c1,c2,c3]
flag=True
lst=[['姓名','学号','第一门课的成绩','第二门课的成绩','第三门课的成绩']]
while flag:
    lst+=[oppo()]
    f=input('是否继续录入成绩（Y/N）：')
    if f == 'N' or f == 'n':
        flag=False
for i in lst:
    for j in i:
        print('%s|'%(j.center(10)),end='')
    print()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # T3
        # mst=10-dec
        # lst=r.shuffle(lst)
        # pacPEP=lst.pop()
        # redPEP=float('%0.2f'%(r.uniform(1,mst)))   # MFA under this line
        
        # while redPEP < 0.50 or mst-redPEP < 0:
        #     redPEP=float('%0.2f'%(r.uniform(1,10)))
        