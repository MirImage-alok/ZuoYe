import random
#一：输入三个整数或小数，输出它们的和（如果结果是整数，就保留小数点后面一位的0）
print('%0.1f'%(float(input('请输入第一个数：'))+float(input('请输入第二个数：'))+float(input('请输入第三个数：'))))
print('='*60)
#二、利用内置字符串函数len()，strip()，split()，find()，lower()，upper()，replace()等对字符串进行相关处理。
ts=input('连续输入数字，用空格分开：')
print('此字符串的长度是：',len(ts))
print('仅删去字符串第1、2个元素的结果：',ts.strip(ts[:2]))
print('仅删去字符串最后第1、2个元素的结果：',ts.strip(ts[-2:]))
print('将此字符串转换为列表，按‘ ’分割：',ts.split("l"))
print('将此字符串转换为列表，按‘ ’分割，仅分割2次：',ts.split(' ',2))
tx=int(random.uniform(0,len(ts)+1))
tx+=tx%2
print('即将查询“%s”的索引'%ts[tx])
print('“%s”的位置：'%ts[tx],ts.find(ts[tx]))
ts2=input('输入一串字母吧：')
print(ts2.lower())
print(ts2.upper())
print(ts2.replace(ts2[:3],ts2[2::-1]))
print('='*60)
#三、用列表实现评委评分处理：输入6 个评分，去掉其中的最高分和最低分，计算平均分将其作为最后得分，并将剩下的评分从高到低排序。
mark=list(map(int,input('连续输入6个评分：').split()))
mark.remove(max(mark))
mark.remove(min(mark))
MeanMark=sum(mark)/len(mark)
print(MeanMark)
print(sorted(mark,reverse=True))
print('='*60)
#四、请编写一个程序，利用字典数据类型实现以下功能：输入一个武功值value，然后从上述字典列表嵌套中输出所有大于该value的人物名字和武功值。
GongliTable={'张三丰':90,'郭靖':93,'黄药师':91,'梅超风':87,'陆大安':52,'柯镇恶':64,'段誉':85}
MarkedValue=int(input('输入一个武功值:'))
TargetKey=[]
for (i,j) in GongliTable.items():
    if MarkedValue < j:
        TargetKey.append(i)
print('武功值大于%d分的人物有%d名，分别是：'%(MarkedValue,len(TargetKey)))
for i in TargetKey:
    print(i,':',GongliTable[i])