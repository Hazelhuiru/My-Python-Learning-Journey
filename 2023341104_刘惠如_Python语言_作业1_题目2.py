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
        print("这里空空如也，游戏结束！")
        break
    else:
        print("\n输入错误，请重新选择")