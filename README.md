# My-Python-Learning-Journey
It just a place to put what I have learnt in the Python class

##项目介绍  
1.题目1：征兵条件判断程序  
###知识点结合
我通过结合if-else语句条件判断、变量计算以及布尔变量来模拟征兵体检条件检查，完整实现了对年龄、身高、BMI和血糖等多项条件的综合判定。  
###题目  
假设你是一名大二的男性学生，你发现学校正在征兵，而你恰好有这样的想法，所以你决定去报名参加征集。首先你要满足年龄（18-22周岁）、身高（160cm以上）、体重（BMI 在 17.5至30 之间，且空腹血糖<7.0mmol/L）等多方面的条件，才能满足征兵的基础条件。
因此，我设计了一个包含年龄、身高、体重(BMI)和血糖的征兵条件判断程序。  
###设计思路   
通过顺序输入和条件判断，依次检查年龄、身高、BMI和血糖等征兵条件，使用if-else语句逐项验证并在最后汇总结果。

2.题目2：寻宝游戏  
###知识点结合  
我使用了if...elif...else语句加循环结合，设计了一个简单的寻宝游戏。  
###题目  
寻找宝藏游戏！这是一个寻宝游戏，你的选择决定你是否能寻找到宝藏。你在一个房间里，你的面前将会有三个门：左边门、中间门、右边门。其中，宝藏藏在了中间门里。左边的门里是一堵墙，右边门里空空如也。如果选到没有宝藏的门，将结束游戏。如果选到另外的门，则返回重新选择。  
###设计思路  
用while True循环处理输入错误，再用if-elif-else判断用户选择。当正确选择时，break退出；而错误时循环继续。  


##如何运行  


##代码说明  
1.题目1代码  
```
print("男生征兵体检条件自查程序")
print("请根据提示输入您的个人信息进行条件检查\n")
age = int(input("请输入您的年龄（周岁）: "))
height = float(input("请输入您的身高（cm）: "))
weight = float(input("请输入您的体重（kg）: "))
blood_sugar = float(input("请输入您的空腹血糖值（mmol/L）: "))
print("\n检查结果")
passed_all = True
if 18 <= age <= 22:
    print("年龄条件符合要求")
else:
    print("年龄条件不符合要求（需18-22周岁）")
    passed_all = False
if height >= 160:
    print("身高条件符合要求")
else:
    print("身高条件不符合要求（需160cm以上）")
    passed_all = False
bmi = weight / ((height/100) ** 2)
if 17.5 <= bmi <= 30:
    print("BMI条件符合要求")
else:
    print("BMI条件不符合要求（需17.5-30之间）")
    passed_all = False
if blood_sugar < 7.0:
    print("空腹血糖条件符合要求")
else:
    print("空腹血糖条件不符合要求（需<7.0mmol/L）")
    passed_all = False
if passed_all:
    print("恭喜！您符合征兵的基本条件")
else:
    print("很遗憾，您目前不符合征兵条件")
```  
2.题目2代码  
```
print("简单寻宝游戏")
print("你在一个房间里，需要找到宝藏")
while True:
    print("\n你面前有三扇门：")
    print("1. 左边门")
    print("2. 中间门")
    print("3. 右边门")
    choice = input("请选择(1/2/3): ")
    if choice == "1":
        print("\n你进入了左边房间")
        print("这里只有一堵墙，游戏结束！")
        break
    elif choice == "2":
        print("\n你进入了中间房间")
        print("你看到一个宝箱！")
        print("恭喜你找到了宝藏！")
        break
    elif choice == "3":
        print("\n你进入了右边房间")
        print(“这里空空如也，游戏结束！”)
        break
    else:
        print(“\n输入错误，请重新选择”)
````

##学习心得与规划  
**浏览GitHub上其他Python项目，以及你完成本次任务的过程，对你管理个人项目、展示个人技能有何启发？  
1.
2.
3.

**你计划如何利用这个仓库记录你未来的学习？  
1.
2.
3.
