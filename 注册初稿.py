import sys,os,getpass,time

while(1):
    print("您是否要注册账户？\n\t1(注册)2(不注册)3（退出）\n\t1 or 2 or 3")
    flog = input()
    if flog == str(1):
        print("开始注册")
        name = input("请输入你的用户名(注：用户名不能用‘3’)：")
        powerss = getpass.getpass("请输入你的密码：")
        print("注册成功！")
        break
    elif flog == str(2):
        print("再来一次，请输入1！！！")
        for daojishi in range(3,0,-1):
            print(daojishi)
            time.sleep(1)
        print("再问你最后一次！！")
        
    elif flog == str(3):
        print("再见")
        time.sleep(1)
        sys.exit()
    else:
            print("认真来好吗宝贝，选1啊")
            time.sleep(0.8)


while(1):
    print("开始登录")
    dl = input("用户名:")
    while(1):
        if dl == str(3):
            while(1):
                print("要退出吗 \n\t1（确定退出）2（按错了）")
                a = input()
                if a == str(1):
                    sys.exit()
                else:
                    print("别乱按宝贝")
                    dl = input("用户名:")
                    break
            else:
                break
        break
   
    if dl == str(88888888):
        print("亲爱的管理员，欢迎您！您一定是帅气的高威先生啦！")
        time.sleep(3.2)
        break
    mm = getpass.getpass("密码:")
    if dl == name:
        if(mm == powerss):
            print("登录成功！"+"游戏即将开始")
            time.sleep(1.5)
            break
        else:
                print("密码错误")
    else:
             print("用户名错误")

