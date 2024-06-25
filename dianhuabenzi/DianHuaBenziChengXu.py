import csv
def st1():
    Bf=open('Netlens/dianhuabenzi/count.csv','r')
    lines=Bf.readlines()
    lines=[i.split(',')[0:2] for i in lines]
    inst=input("请输入待查询联系人：")
    for i in lines:
        if i[0]==inst:
            print("%s的电话是%s"%(inst,i[1]))
            Bf.close()
            A=input('按任意键继续或按Ctrl+C终止程序')
            break
def st2():
    Bf=open('Netlens/dianhuabenzi/count.csv','r')
    lines=Bf.readlines()
    lines=[i.split(',')[0:2] for i in lines]
    nam=input('请输入名称：')
    tel=input('请输入电话：')
    lines.append([nam,int(tel)]) 
    Bf.close()
    with open('Netlens/dianhuabenzi/count.csv', 'w', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in lines:
            writer.writerow(row)
    A=input('按任意键继续或按Ctrl+C终止程序')
def st3():
    Bf=open('Netlens/dianhuabenzi/count.csv','r')
    lines=Bf.readlines()
    lines=[i.split(',')[0:2] for i in lines]
    inst=input("请输入待删除联系人：")
    for i in range(len(lines)):
        if lines[i][0]==inst:
            print("%s的电话是%s"%(inst,lines[i][1][:-1]))
            sct=input('[此联系人将在键入Enter后被删除]')
            del lines[i]
            break    
    Bf.close()
    with open('Netlens/dianhuabenzi/count.csv', 'w', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in lines:
            writer.writerow(row)
    A=input('按任意键继续或按Ctrl+C终止程序')
def st4():
    Bf=open('Netlens/dianhuabenzi/count.csv','r')
    lines=Bf.readlines()
    lines=[i.split(',')[0:2] for i in lines]
    inst=input("请输入待查询联系人：")
    for i in range(len(lines)):
        if lines[i][0]==inst:
            print("%s的电话是%s"%(inst,lines[i][1][:-1]))
            sct=input('此电话将被修正为：')
            lines[i][1]=sct
            break    
    Bf.close()
    with open('Netlens/dianhuabenzi/count.csv', 'w', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in lines:
            writer.writerow(row)
    A=input('按任意键继续或按Ctrl+C终止程序')
def st5():
    Bf=open('Netlens/dianhuabenzi/count.csv','r')
    lines=Bf.readlines()
    lines=[i.split(',')[0:2] for i in lines]
    print('''接下来将展示整张通讯录：
================================''')
    for i in lines:
        print('%s : %s'%(i[0],i[1]))
    Bf.close()
    print('''================================
          展示完毕''')
    A=input('按任意键继续或按Ctrl+C终止程序')
while True:
    print('本系统可以实现查找存储在文件中的联系人并输出其联系号码、添加新联系人及其号码、删除联系人、更新联系人号码、输出所有联系人及其号码功能。 ')
    print('请输入数字以启动服务:')
    print('''[1] : 查找的朋友
[2] : 添加新的朋友  
[3] : 删除通讯录中的朋友  
[4] : 修改通讯录中朋友的联系电话  
[5] : 显示所有的通讯录列表
[6] : 退出程序 ''')
    stTG=input("[请键入数字以启动服务：]")
    if stTG == '1':
        st1()
    if stTG == '2':
        st2()
    if stTG == '3':
        st3()
    if stTG == '4':
        st4()
    if stTG == '5':
        st5()
    if stTG == '6':
        exit()  