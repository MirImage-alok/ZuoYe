# T1
fileConsed1, fileConsed2 = open('Netlens/06fd/A.txt', 'r'), open('Netlens/06fd/B.txt', 'r')
fileConsed1_str, fileConsed2_str = fileConsed1.read(), fileConsed2.read()
fileConsed1.close()
fileConsed2.close()
with open('Netlens/06fd/C.txt', 'w') as fileConsed:
    fileConsed_str = list(fileConsed1_str + fileConsed2_str)
    fileConsed_str.sort()
    fileConsed_str = ''.join(fileConsed_str)
    fileConsed.write(fileConsed_str)


# T2
# 用于输出平均分
def outAvg(Lst):
    sum1,sum2=0,0
    for line in Lst:
        L1=line.strip().split()
        sum1+=int(L1[1])
        sum2+=int(L1[2])
    count=len(Lst)
    avg1=sum1/count
    avg2=sum2/count
    print("数学平均成绩为：%4.1f"%avg1)
    print("语文平均成绩为：%4.1f"%avg2)
# 用于找出不及格
def outUnpass(Lst):
    print("两门成绩均不及格的学生姓名缩写、数学和语文成绩为：")
    for line in Lst:
        L1 = line.strip().split()
        if int(L1[1])<60 and int(L1[2])<60:
            print(line)
# 用于找出好学生
def outNice(Lst):
    print("两门课平均分在90以上的学生姓名缩写、数学和语文成绩为：")
    for line in Lst:
        L1=line.strip().split()
        f_score=round((int(L1[1])+int(L1[2]))/2)
        if f_score>=90:
            print(line)
# 程序主体
f=open("Netlens/06fd/class_score.txt",encoding='gbk')
Lst=f.readlines()
outAvg(Lst)
outUnpass(Lst)
outNice(Lst)