import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False 
def oppo():  # 用于录入成绩
    name=input('请输入姓名：')
    num=input('请输入学号：')
    tel=input('手机号码：')
    c1=input('英语的成绩：')
    c2=input('高等数学的成绩：')
    c3=input('信息技术基础的成绩：')
    return [name+',',num+',',tel+',',c1+',',c2+',',c3+',\n']
# # 用于向文件录入成绩
# with open('Netlens/05fd/05.csv',mode='+a') as fd:
#     tn=int(input('班级共多少人：'))
#     for i in range(tn):
#         fd.writelines(oppo())
# 用于绘制班级各门课程的均分直方图
df=pd.read_csv('Netlens/05fd/05.csv',encoding='gbk')
col_mean=df[["英语","高等数学","信息技术基础"]].mean()
col_mean.plot(kind='bar')
plt.title(u'班级各门课程的均分直方图')
plt.xlabel(u'科目')
plt.ylabel(u'均分')
plt.show()
# 用于绘制总分成绩分布图
df["总分"] = df["英语"]+df["高等数学"]+df["信息技术基础"]
tab = df['总分'].values.mean()
plt.figure(figsize=(10, 10), dpi=80)
plt.scatter(range(len(df['总分'])),df['总分'])
plt.xticks(range(len(df['总分'])),df['学号'])
plt.axhline(y=tab,color='red',lw=3,ls='--')
plt.show()