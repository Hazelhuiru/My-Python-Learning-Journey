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
print("\n" + "="*30)
if passed_all:
    print("恭喜！您符合征兵的基本条件")
else:
    print("很遗憾，您目前不符合征兵条件")
