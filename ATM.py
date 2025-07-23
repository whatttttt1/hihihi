money=5000000
name=input('请输入您的姓名:')
print('您好，欢迎来到点心取款机，请选择操作：\n查询余额\t输入1\t\n存款\t输入2\t\n取款\t输入3\t\n退出\t输入4\t:')
x=int(input())
def func_main():
    if x!=4:
       print('您好，欢迎来到点心取款机，请选择操作：\n查询余额\t输入1\t\n存款\t输入2\t\n取款\t输入3\t\n退出\t输入4\t:')
    return x
def func_cha():
    if x==1:
        print(f'您的余额剩余：{money}')
    return func_main()
def func_cun(a):
    global money
    money+=a
    if x==2:
        print(f'{name},您存款50000元成功，{name}，您的余额剩余：{money}元')
    return func_cha()
def func_qu(b):
    if x==3:
        global money
        money-=b
        print(f'{name},您取款{b}元成功，您的余额剩余{money}元')
    return func_cha()
while True:
    if x==1:
        func_cha()

    elif x==2:
        num=int(input('存多少钱：'))
        func_cun(num)
    elif x==3:
        num=int(input('取多少钱：'))
        func_qu(num)
    else:
        print('退出')
        break
    x=int(input())
