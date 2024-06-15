#
这里用来存放Python课的作业
=
我的编程环境使用VS code的文件夹模式，故在其他平台上运行时可能会因为相对引用路径而产生一些问题
抄的时候记得改
目录：
-
	0318.py
	  	一：输入三个整数或小数，输出它们的和（如果结果是整数，就保留小数点后面一位的0）
	  	二、利用内置字符串函数len()，strip()，split()，find()，lower()，upper()，replace()等对字符串进行相关处理。
	  	三、用列表实现评委评分处理：输入6 个评分，去掉其中的最高分和最低分，计算平均分将其作为最后得分，并将剩下的评分从高到低排序。
	  	四、请编写一个程序，利用字典数据类型实现以下功能：输入一个武功值value，然后从上述字典列表嵌套中输出所有大于该value的人物名字和武功值。
   	04fd.py
     实验四
	  	T1、编写函数，求斐波那契数列第n项的值，其中F0=1，F1=1，Fn=Fn-1+Fn-2。
	  	T2、使用time 函数库中的函数求当前系统的日期，并计算当前日期是本年度的第几天。（提示：使用time函数库中的strftime()函数可以获得当前日期的字符形式；为了判断今年的年份是不是闰年，我们需要使用int()函数将获得的字符串格式的日期数据转换成整数；判断某年是否为闰年的规则为：闰年的年份应该可以被4整数但不能被100整数，或者该年份直接能被400整除；为了简化程序，可以在程序开始处设置两个列表，分别存放平年和闰年中每个月的天数，只需根据今年的年份是否为闰年选择使用对应列表中的数据进行累加即可得到系统日期为该年中的第几天。）
	  T3、发红包了！请从Li的好友列表中依次读取好友的姓名（lst = ["Tom","Rose","小明","王强"]），并给他（她）发送一个1-10元之间的随机红包，打印在屏幕上，并编写函数显示谁是最幸运的人（红包最大的那个人）。（提示：本题需要建立一个字典存放人名和他随机得到的红包；使用random.uniform(1,10)可生成1-10以内的随机数。）
	  T4、编写input()和output()函数完成学生数据记录的输入与输出，要求记录条数不小于5条，每个学生信息包括学号，姓名及三门课程的成绩。要求使用list来模拟学生记录结构。
    06fd/06fd.py
     实验五
     	T1、有两个磁盘文件A.txt和B.txt，各存放一行字符，请编写程序把这两个文件中的信息合并，并按字母顺序排列，输出到一个新文件C.txt中。
		T2、当前工作目录下有一个文件名为class_score.txt的文本文件，存放着某班学生的学号（第1列）、数学课成绩（第2列）和语文课成绩（第3列），每列数据用制表符（\t）进行分隔，文件内容如下所示，请编程完成下列要求：（1）分别求这个班数学和语文的平均分（保留1位小数）并输出。  （2）找出两门课都不及格（<60）的学生，输出他们的学号和各科成绩。 （3）找出两门课的平均分在90分以上的学生，输出他们的学号和各科成绩。
  	05fd/05fd.py
     实验六
 		T1 对班级各门课程的均分做出直方图，并对直方图进行标注；
		T2 做总分成绩分布图，纵坐标表示成绩，横坐标表示学号，画出总分的均分横线，让每位同学的总分圆点分布在均分线上下，以便于观察每位同学的成绩离开均分的距离。

