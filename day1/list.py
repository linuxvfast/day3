#-*- coding:utf-8-*- 
#__author__ = 'linux vfast'
#购物车列表显示
product_list = [
    ('iphone',5800),
    ('mac pro',9800),
    ('Bike',800),
    ('watch',10600),
    ('coffee',31),
    ('Alex python',120),
]

shopping_list = []
salary = input('input your salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        for i,item in enumerate(product_list):
            print(i,item)
        user_choice = input('请选择要购买的商品:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) + 1 and user_choice >= 0:
                price_item = product_list[user_choice]
                if price_item[1] <= salary:
                    shopping_list.append(price_item[0])
                    salary -= price_item[1]
                    print('Added %s into shopping cart,your current balance is %s'%(price_item[0],salary))
                    print(shopping_list)
            else:
                print('product code [%s] is not exist!'% user_choice)
        elif user_choice == 'q':
            print('\033[32m你当前的余额为 %s\033[0m' % salary)
            print('shopping list'.center(50,'*'))
            for shopp in shopping_list:
                print(shopp)
            exit()
        else:
            print('ivalid option!')
else:
    print('\033[34m输入错误，请输入数字！\033[0m')
    exit()



